<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">{{ profile && profile.username ? profile.username : '' }}님의 프로필</span>
    </h1>
  </section>
  <h1>{{ profile && profile.username ? profile.username : '' }} 프로필</h1>
  <div v-if="profile && profile.image">
    <img :src="imageUrl(profile.image)" class="profile-img" alt="프로필 이미지" />
  </div>
  <div v-if="profile">
    <p>👤 나이: {{ profile.age }}</p>
    <p>👫 성별: {{ profile.gender === 'M' ? '남성' : '여성' }}</p>
    <p>📊 투자성향: {{ profile.risk_profile }}</p>
    <p>💰 유동자산: {{ profile.liquid_assets }}만원</p>
    <p>💼 연봉: {{ profile.annual_income }}만원</p>
    <button @click="goEdit">프로필 수정</button>
  </div>
  <div v-else>
    <p>프로필 정보가 없습니다.</p>
    <button @click="goEdit">프로필 작성</button>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const profile = ref(null)
const userId = localStorage.getItem('user_pk')  // 로그인 후 pk 저장 필수!
const username = ref(localStorage.getItem('username') || '')
const imageUrl = (img) => {
  if (!img) return ''
  return `http://127.0.0.1:8000${img.startsWith('/') ? img : '/' + img}?v=${Date.now()}`
}

onMounted(async () => {
  const token = localStorage.getItem('token')
  const res = await fetch('http://127.0.0.1:8000/api/v1/user/profile/me/', {
    headers: { 'Authorization': `Token ${token}` }
  })
  if (res.ok) {
    profile.value = await res.json()
  }
})

const goEdit = () => {
  router.push({ name: 'profileSetup' })  // profileSetup 라우터 이름을 맞춰주세요!
}

const logout = () => {
  localStorage.removeItem('token')
  // 필요하다면 username 등도 같이 제거
  localStorage.removeItem('username')
  // ...다른 사용자 관련 데이터도 있으면 같이 삭제

  router.push({ name: 'MainPage' }) // MainPage에 맞게 name 지정!
}
</script>

<style scoped>
.profile-img {
  width: 120px;
  height: 120px;
  object-fit: cover;
  border-radius: 50%;
  /* 동그라미 */
  border: 3px solid #ddd;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
  margin-bottom: 16px;
}
</style>