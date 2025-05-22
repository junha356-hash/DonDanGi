<template>
  <div>
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">로그인</span>
      </h1>
    </section>
    <h2>로그인</h2>
    <form @submit.prevent="signin">
      <input v-model="username" type="text" placeholder="아이디" required />
      <input v-model="password" type="password" placeholder="비밀번호" required />
      <button type="submit">로그인</button>
    </form>
    <hr>
    <RouterLink :to="{ name: 'signup' }">
      회원가입
    </RouterLink>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '@/stores/user'

const emit = defineEmits(['auth-change'])
const username = ref('')
const password = ref('')
const router = useRouter()
const userStore = useUserStore()

const signin = async () => {
  const res = await fetch('http://127.0.0.1:8000/api/v1/auth/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: username.value,
      password: password.value
    })
  });
  const data = await res.json();
  if (res.ok) {
    userStore.login(data.key) 
    // 토큰 저장
    localStorage.setItem('token', data.key);
    // **username도 저장!**
    localStorage.setItem('username', username.value);   // 이 코드가 중요!
    // 라우터 이동
    router.push({ name: 'MainPage' });
  } else {
    alert('로그인 실패: ' + (data.non_field_errors || JSON.stringify(data)));
  }
}
</script>
