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
      <!-- startDate select -->
      <select v-model="startDate" class="form-control" style="width: 200px;">
        <option disabled value="">시작 날짜 선택</option>
        <option
          v-for="row in rawData"
          :key="row.date"
          :value="row.date"
        >{{ row.date }}</option>
      </select>
      <!-- endDate select -->
      <select v-model="endDate" class="form-control" style="width: 200px;">
        <option disabled value="">종료 날짜 선택</option>
        <option
          v-for="row in rawData"
          :key="row.date + 'e'"
          :value="row.date"
        >{{ row.date }}</option>
      </select>

      <button class="btn btn-warning" @click="selectedType = 'gold'">GOLD</button>
      <button class="btn btn-secondary" @click="selectedType = 'silver'">SILVER</button>
    </div>


    <!-- 그래프 출력 -->
    <line-chart :chart-data="filteredChartData" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import * as XLSX from 'xlsx'
import LineChart from '@/components/Gold_SilverComponent.vue'

// Excel serial date → yyyy-mm-dd로 변환 함수
function excelDateToJSDate(serial) {
  const utc_days = Math.floor(serial - 25569)
  const utc_value = utc_days * 86400
  const date_info = new Date(utc_value * 1000)
  date_info.setDate(date_info.getDate() + 1) // Excel-UTC 보정
  return date_info.toISOString().slice(0, 10)
}

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
  // Gold
  const goldRes = await fetch('/data/Gold_prices.xlsx')
  const goldArrayBuffer = await goldRes.arrayBuffer()
  const goldWorkbook = XLSX.read(goldArrayBuffer, { type: 'array' })
  const goldSheet = goldWorkbook.Sheets[goldWorkbook.SheetNames[0]]
  const goldJson = XLSX.utils.sheet_to_json(goldSheet)

  // Silver
  const silverRes = await fetch('/data/Silver_prices.xlsx')
  const silverArrayBuffer = await silverRes.arrayBuffer()
  const silverWorkbook = XLSX.read(silverArrayBuffer, { type: 'array' })
  const silverSheet = silverWorkbook.Sheets[silverWorkbook.SheetNames[0]]
  const silverJson = XLSX.utils.sheet_to_json(silverSheet)

  // 날짜 변환: Excel serial number(숫자)면 변환, 문자열이면 그대로
  const merged = goldJson.map((row, i) => ({
    date: typeof row.Date === 'number'
      ? excelDateToJSDate(row.Date)
      : (typeof row.Date === 'string'
          ? row.Date.slice(0, 10)
          : ''),
    gold: Number(String(row['Close/Last']).replace(/,/g, '')),
    silver: Number(String(silverJson[i]['Close/Last']).replace(/,/g, ''))
  }));

  rawData.value = merged

  // 기본적으로 모든 날짜가 선택되어 있도록 초기화
  if (merged.length) {
    startDate.value = merged[0].date
    endDate.value = merged.at(-1).date
  }
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
