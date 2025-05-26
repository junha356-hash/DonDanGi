<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/community.jpg" alt="main_img" data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">회원가입</h1>
  </section>
  <div class="container-content d-flex justify-content-center align-items-center">
      <main>
        <div class="py-5 text-center" id="errorContainer">
          <img class="d-block mx-auto mb-4" src="@/assets/logo.png" width="150" height="150">
          <h2 class="fw-bold mb-5" style="font-size: 50px;">회원 가입</h2>
        </div>
        <div class="row g-5" style="margin-bottom: 100px; max-width: 1200px;">
          <div class="col-lg-12">
            <h4 class="mb-3">회원 정보 입력</h4>
            <p class="mb-3 text-muted">
              <span style="color:red; font-size: larger;">&nbsp;*</span>는 필수 입력 항목입니다.
            </p>
            <div v-if="errormsg" class="row">
              <p class="text-danger mb-2" v-for="err in errormsg">
                {{ err }}
              </p>
            </div>
            <hr>
            <form class="mt-5" @submit.prevent="submitEvent">
              <div class="row g-4">
                <div class="col-12">
                  <label for="id" class="form-label">아이디<span style="color:red; font-size: larger;">&nbsp;*</span></label>
                  <div class="input-group">
                    <input type="text" class="form-control" id="id" placeholder="아이디" required v-model="username">
                  </div>
                </div>
                <div class="col-12">
                  <label for="password" class="form-label">비밀번호<span
                    style="color:red; font-size: larger;">&nbsp;*</span></label>
                  <div class="input-group">
                    <input type="password" class="form-control" id="password" required v-model="password1">
                  </div>
                </div>
                <div class="col-12">
                  <label for="password2" class="form-label">비밀번호 확인<span
                    style="color:red; font-size: larger;">&nbsp;*</span></label>
                  <div class="input-group">
                    <input type="password" class="form-control" id="password2" required v-model="password2">
                  </div>
                </div>
                <div class="col-12">
                  <label for="email" class="form-label">Email</label>
                  <input type="email" class="form-control" id="email" placeholder="이메일" v-model="email">
                </div>
              </div>
            <hr>
            <div class="text-center">
              <button class="w-50 btn btn-primary btn-lg fs-4 fw-bold" type="submit">회원 가입</button>
            </div>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password1 = ref('')
const password2 = ref('')
const email = ref('')
const errormsg = ref([])

const submitEvent = async () => {
  errormsg.value = []  // 에러 초기화

  if (password1.value !== password2.value) {
    errormsg.value.push('비밀번호를 다시 확인해주세요!')
    return
  }
    if (password1.length < 6) {
    errormsg.value.push('비밀번호가 너무 짧습니다 !')
    return
  }

  try {
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

    let data = null
    try {
      data = await res.json()
    } catch (e) {
      data = null
    }

    if (res.ok && (data === null || data.key)) {
      router.push({ name: 'MainPage' })
    } else {
      if (data) {
        errormsg.value = Object.values(data).flat()
      } else {
        alert('회원가입 실패: 응답 없음')
      }
    }
  } catch (err) {
    alert('회원가입 요청 실패: 네트워크 에러 또는 서버 다운')
    console.error(err)
  }
}
</script>