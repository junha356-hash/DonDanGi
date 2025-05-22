<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
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

  console.log('회원가입 응답 status:', res.status)
  let data = null
  try {
    data = await res.json()
  } catch (e) {
    data = null
  }
  console.log('회원가입 응답 데이터:', data)

  if (res.ok && (data === null || (data && data.key))) {
    // 204(바디없음) or 200/201(바디 있음, data.key 있을 때) 모두 성공 처리
    // 예시: 204라면 data === null
    router.push({ name: 'MainPage' });
  } else {
    alert('회원가입 실패: ' + JSON.stringify(data));
  }
}

</script>
