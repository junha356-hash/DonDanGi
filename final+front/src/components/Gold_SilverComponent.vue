<template>
  <div>
    <Line v-if="chartData" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const props = defineProps({
  data: Array, // [['2024-05-20', 2400.15], ...]
  label: String // 'Gold' or 'Silver'
})

const chartData = ref(null)

watch(() => props.data, (newData) => {
  if (!newData) return
  chartData.value = {
    labels: newData.map(d => d[0]),
    datasets: [
      {
        label: props.label,
        data: newData.map(d => d[1]),
        fill: false,
        tension: 0.1
      }
    ]
  }
}, { immediate: true })

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top'
    }
  },
  scales: {
    y: {
      beginAtZero: false
    }
  }
}
</script>

<style scoped>

</style>
