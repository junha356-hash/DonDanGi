<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/gold_silver.webp" alt="gold_siver_img" data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">국제 금/은 시세</h1>
  </section>

  <div class="container-content" style="min-width: 1400px; min-height: 800px;">
    <h1 class="fw-bold">국제 금/은 시세 조회</h1>
    <hr>

    <div class="row">
      <div class="ms-4 col-8 mt-4">
        <div class="row" style="height: 60px; border:2px gray solid;">
          <div class="col-6 d-flex justify-content-center"
            :style="[{ backgroundColor: selectedMetal === 'gold' ? '#0d6efd' : 'transparent' },
                    { color: selectedMetal === 'gold' ? 'white' : 'black' }]"
            @click="selectMetal('gold')">
            <div class="d-flex align-items-center justify-content-center">
              <p class="fs-3 fw-bold mb-0">GOLD</p>
            </div>
          </div>

          <div class="col-6 d-flex justify-content-center" style="border-left: 2px gray solid;"
            :style="[{ backgroundColor: selectedMetal === 'silver' ? '#0d6efd' : 'transparent' },
                    { color: selectedMetal === 'silver' ? 'white' : 'black' }]"
            @click="selectMetal('silver')">
            <div class="d-flex align-items-center justify-content-center">
              <p class="fs-3 fw-bold mb-0">SILVER</p>
            </div>
          </div>
        </div>

        <!-- 시세 그래프 + 표 (공통) -->
        <div v-if="metalData.length > 0" class="mt-4">
          <MetalChart :data="metalData" :label="label" />
          <table class="table table-bordered text-center align-middle mt-4">
            <thead class="table-light">
              <tr>
                <th>금속 종류</th>
                <th>{{ label }}</th>
              </tr>
              <tr>
                <th>최근 시세</th>
                <th><span class="text-success">{{ latestPrice }} USD/oz</span></th>
              </tr>
              <tr>
                <th>기준일</th>
                <th>✔ {{ latestDate }}</th>
              </tr>
            </thead>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import MetalChart from '@/components/Gold_SilverComponent.vue'

const API_KEY = 'tiU6FJxNqUQeA6ywzyk6'

const selectedMetal = ref('gold') // gold 또는 silver
const metalData = ref([])
const label = ref('')
const latestPrice = ref(null)
const latestDate = ref('')

const formatDate = (d) => d.toISOString().split('T')[0]

const fetchMetal = async (type) => {
  const dataset = type === 'gold' ? 'LBMA/GOLD' : 'LBMA/SILVER'
  label.value = type === 'gold' ? 'Gold (USD/oz)' : 'Silver (USD/oz)'

  try {
    const endDate = new Date()
    const startDate = new Date()
    startDate.setFullYear(endDate.getFullYear() - 1)

    const { data } = await axios.get(`https://data.nasdaq.com/api/v3/datasets/${dataset}.json`, {
      params: {
        api_key: API_KEY,
        start_date: formatDate(startDate),
        end_date: formatDate(endDate),
        order: 'asc'
      }
    })

    const values = data.dataset.data.map(row => [row[0], row[1] || row[2]])
    metalData.value = values
    const last = values.at(-1)
    latestDate.value = last[0]
    latestPrice.value = last[1]
  } catch (err) {
    console.error(`시세 불러오기 실패 (${type})`, err)
  }
}

const selectMetal = (type) => {
  if (selectedMetal.value !== type) {
    selectedMetal.value = type
    fetchMetal(type)
  }
}

onMounted(() => {
  fetchMetal(selectedMetal.value)
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
