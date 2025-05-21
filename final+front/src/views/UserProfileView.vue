<template>
  <div class="container mt-4">
    <h1>내 프로필</h1>
    <div v-if="profile">
      <p>👤 나이: {{ profile.age }}</p>
      <p>👫 성별: {{ profile.gender === 'M' ? '남성' : '여성' }}</p>
      <p>📊 투자성향: {{ profile.risk_profile }}</p>
      <p>💰 유동자산: {{ profile.liquid_assets }}만원</p>
      <p>💼 연봉: {{ profile.annual_income }}만원</p>
    </div>
    <div v-else>
      <p>프로필 정보를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const profile = ref(null)

onMounted(async () => {
  const token = localStorage.getItem('token')  // 로그인 시 저장한 토큰
  const res = await fetch('http://127.0.0.1:8000/api/v1/user/profile/', {
    headers: {
      'Authorization': `Token ${token}`,
      'Content-Type': 'application/json'
    }
  })
  if (res.ok) {
    profile.value = await res.json()
  } else {
    alert('프로필 정보를 불러올 수 없습니다.')
  }
})
</script>
