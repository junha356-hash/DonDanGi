<template>
  <Line :data="chartData" :options="options" />
</template>

<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  CategoryScale,
  Tooltip,
  Legend
} from 'chart.js'

ChartJS.register(LineElement, PointElement, LinearScale, Title, CategoryScale, Tooltip, Legend)

defineProps(['chartData'])

const options = {
  responsive: true,
  plugins: {
    legend: { position: 'top' },
    tooltip: { mode: 'index' }
  },
  scales: {
    y: { beginAtZero: false }
  }
}
</script>