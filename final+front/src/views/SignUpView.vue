<template>
  <div class="container mt-4">
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/community.jpg" alt="community_img" 
      data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">커뮤니티</span>
      </h1>
    </section>
    <h2>회원가입</h2>
    <hr>
    <form @submit.prevent="signup">
      <input v-model="username" type="text" placeholder="아이디" required />
      <hr>
      <input v-model="password1" type="password" placeholder="비밀번호" required />
      <hr>
      <input v-model="password2" type="password" placeholder="비밀번호 확인" required />
      <hr>

      <input v-model="age" type="number" placeholder="나이" />
      <hr>
      <select v-model="gender">
        <option disabled value="">성별 선택</option>
        <option value="M">남성</option>
        <option value="F">여성</option>
      </select>
      <hr>

      <input v-model="riskProfile" type="text" placeholder="투자성향 (예: 안정형)" />
      <hr>
      <input v-model="liquidAssets" type="number" placeholder="보유 유동자산 (만원)" />
      <hr>
      <input v-model="annualIncome" type="number" placeholder="연봉 (만원)" />
      <hr>

      <button type="submit">회원가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password1 = ref('')
const password2 = ref('')
const age = ref('')
const gender = ref('')
const riskProfile = ref('')
const liquidAssets = ref('')
const annualIncome = ref('')

const signup = async () => {
  const res = await fetch('http://127.0.0.1:8000/api/v1/auth/registration/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: username.value,
      password1: password1.value,
      password2: password2.value
    })
  })

  const data = await res.json()

  if (res.ok) {
    const token = data.key
    localStorage.setItem('token', token)

    // ✅ 프로필 정보 저장
    await fetch('http://127.0.0.1:8000/api/v1/user/profile/', {
      method: 'PUT',
      headers: {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        age: age.value,
        gender: gender.value,
        risk_profile: riskProfile.value,
        liquid_assets: liquidAssets.value,
        annual_income: annualIncome.value
      })
    })

    router.push({ name: 'MainPage' })
  } else {
    alert('회원가입 실패: ' + JSON.stringify(data))
  }
}
</script>
