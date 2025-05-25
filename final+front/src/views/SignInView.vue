<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">로그인</h1>
  </section>

  <div class="container-content my-5" id="loginbox">
    <div class="py-5 text-center">
      <img class="d-block mx-auto mb-4" src="@/assets/logo.webp" width="150" height="150">
    </div>

    <main class="form-signin" style="min-height:500px;">
      <form class="row gy-5 justify-content-center d-flex flex-column align-items-center"
            @submit.prevent="signin">
        <div class="form-floating" style="width: 70%;">
          <input type="text" class="form-control" id="floatingInput" placeholder="아이디" v-model="username">
          <label for="floatingInput">아이디</label>
        </div>

        <div class="form-floating" style="width: 70%;">
          <input type="password" class="form-control" id="floatingPassword" placeholder="비밀번호" v-model="password">
          <label for="floatingPassword">비밀번호</label>
        </div>

        <button class="w-50 btn btn-lg btn-primary fw-bold" type="submit">로그인</button>
        <button class="w-50 btn btn-lg btn-danger fw-bold" type="button" @click="SignUp">회원가입</button>
      </form>
    </main>
  </div>

  <hr>
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const username = ref('')
const password = ref('')

const router = useRouter()
const userStore = useUserStore()

// 로그인 함수
const signin = async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/v1/auth/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    })

    const data = await res.json()

    if (res.ok) {
      userStore.login(data.key)
      localStorage.setItem('token', data.key)
      localStorage.setItem('username', username.value)
      router.push({ name: 'MainPage' })
    } else {
      alert('로그인 실패: ' + (data.non_field_errors || JSON.stringify(data)))
    }
  } catch (err) {
    alert('서버 에러: ' + err)
  }
}

// 회원가입 이동
const SignUp = () => {
  router.push({ name: 'signup' })  // 라우터 name이 'SignUp'으로 설정되어 있어야 함
}
</script>