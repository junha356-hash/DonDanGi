<template>
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
    <input v-model="email" type="email" placeholder="이메일" required />
    <hr>


    <button type="submit">회원가입</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password1 = ref('')
const password2 = ref('')
const email = ref('')

const signup = async () => {
  const res = await fetch('http://127.0.0.1:8000/api/v1/auth/registration/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      email: email.value
    })
  })

  // 데이터 파싱
  let data = null
  if (res.headers.get('content-type')?.includes('application/json')) {
    data = await res.json()
  }

  if (res.ok && data && data.key) {
    const token = data.key
    localStorage.setItem('token', token)

    // 프로필 정보 저장
    const profileRes = await fetch('http://127.0.0.1:8000/api/v1/user/profile/', {
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

    // 프로필 저장 응답도 content-type 체크!
    let profileData = null
    if (profileRes.headers.get('content-type')?.includes('application/json')) {
      profileData = await profileRes.json()
    }

    // 메인페이지 이동!
    router.push({ name: 'MainPage' }) // 또는 home
  } else {
    alert('회원가입 실패: ' + JSON.stringify(data))
  }
}
</script>
