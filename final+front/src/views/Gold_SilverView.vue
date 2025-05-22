<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/gold_silver.webp" alt="gold_siver_img" data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">국제 금/은 시세</h1>
  </section>

  <div class="container-content" style="min-width: 1400px; min-height: 800px;">
    <h1 class="fw-bold">국제 금/은 시세 조회</h1>
    <hr>

    <!-- 날짜 및 종류 선택 -->
    <div class="d-flex gap-3 mb-4">
      <input type="date" v-model="startDate" class="form-control" style="width: 200px;">
      <input type="date" v-model="endDate" class="form-control" style="width: 200px;">
      <button class="btn btn-warning" @click="selectedType = 'gold'">GOLD</button>
      <button class="btn btn-secondary" @click="selectedType = 'silver'">SILVER</button>
    </div>

    <!-- 그래프 출력 -->
    <line-chart :chart-data="filteredChartData" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
// import * as XLSX from 'xlsx'
import LineChart from '@/components/Gold_SilverComponent.vue'

const rawData = ref([])
const startDate = ref('')
const endDate = ref('')
const selectedType = ref('gold')

const filteredChartData = computed(() => {
  const data = rawData.value.filter(row => {
    const date = row.date
    return (!startDate.value || date >= startDate.value) &&
           (!endDate.value || date <= endDate.value)
  })

  return {
    labels: data.map(row => row.date),
    datasets: [
      {
        label: selectedType.value === 'gold' ? 'Gold Price' : 'Silver Price',
        data: data.map(row => row[selectedType.value]),
        borderColor: selectedType.value === 'gold' ? 'gold' : 'gray',
        tension: 0.4
      }
    ]
  }
})

onMounted(async () => {
  const res = await fetch('/data/metal_prices.xlsx') // public 폴더에 저장된 파일
  const arrayBuffer = await res.arrayBuffer()
  const workbook = XLSX.read(arrayBuffer, { type: 'array' })
  const sheet = workbook.Sheets[workbook.SheetNames[0]]
  const json = XLSX.utils.sheet_to_json(sheet)

  rawData.value = json.map(row => ({
    date: row.Date.slice(0, 10),  // 'YYYY-MM-DD'
    gold: row.Gold,
    silver: row.Silver
  }))
})
</script>

<style scoped>
.converter {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
}
.input-group {
  position: relative;
}
.input-text-addon {
  position: absolute;
  right: 40px;
  top: 50%;
  transform: translateY(-50%);
  font-weight: bold;
  font-size: 20px;
  pointer-events: none;
}
.form-control {
  padding-right: 60px;
}
.table {
  font-size: 15px;
}
</style>
