<template>
  <div>
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/gold_silver.webp" alt="gold_silver_img" data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">국제 금/은 시세</span>
      </h1>
    </section>
    <h2>금/은 시세 그래프</h2>
    <label>
      시작일: <input type="date" v-model="startDate">
      종료일: <input type="date" v-model="endDate">
    </label>
    <button @click="fetchPrices">시세 조회</button>

    <div v-if="goldData.length">
      <h3>금 시세</h3>
      <Gold_SilverComponent :data="goldData" xKey="date" yKey="price" />
    </div>
    <div v-if="silverData.length">
      <h3>은 시세</h3>
      <Gold_SilverComponent :data="silverData" xKey="date" yKey="price" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Gold_SilverComponent from '@/components/Gold_SilverComponent.vue'

const goldData = ref([])
const silverData = ref([])
const startDate = ref('2023-01-01')
const endDate = ref('2024-04-30')

const fetchPrices = async () => {
  // 금
  const goldRes = await fetch(`http://127.0.0.1:8000/api/v1/gold-prices/?start=${startDate.value}&end=${endDate.value}`)
  goldData.value = await goldRes.json()
  // 은
  const silverRes = await fetch(`http://127.0.0.1:8000/api/v1/silver-prices/?start=${startDate.value}&end=${endDate.value}`)
  silverData.value = await silverRes.json()
}
</script>
