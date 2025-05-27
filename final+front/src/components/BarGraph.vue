<script setup>
import { Bar } from 'vue-chartjs'
import { Chart, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js'
import { computed } from 'vue'

Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend)

const props = defineProps({
  products: Array, // [{fin_prdt_nm, options: [...]}, ...]
  getBestRate: Function // 상품별 최고 금리 추출 함수
})

const barData = computed(() => ({
  labels: props.products.map(p => p.fin_prdt_nm),
  datasets: [
    {
      label: '금리(%)',
      data: props.products.map(p => props.getBestRate ? props.getBestRate(p) : 0),
      backgroundColor: ['#0d6efd', '#20c997', '#ff9800'],
    }
  ]
}))

const barOptions = {
  responsive: true,
  plugins: {
    legend: { display: false }
  },
  scales: {
    y: { beginAtZero: true }
  }
}
</script>
<template>
  <Bar :data="barData" :options="barOptions" />
</template>
