<template>
  <div class="container-fluid">
    <header :class="['navbar-custom', { 'navbar-scrolled': isScrolled, 'navbar-dark': !isScrolled }]">
      <nav class="navbar navbar-expand-lg px-5" data-aos="fade-up" data-aos-duration="1500">
        <div class="container-custom d-flex flex-nowrap">
          <ul class="navbar-nav d-flex flex-row flex-nowrap">
            <li class="nav-item">
              <RouterLink :to="{ name: 'MainPage' }" class="navbar-brand" @click="navbarStore.closeMenu"
                :style="{ color: isScrolledColor }">
                <!-- <h1>메인 페이지</h1> -->
                <img src="@/assets/logo.webp" alt="logo_img" class="navbar-logo">
              </RouterLink>
            </li>
          </ul>

          <!-- 햄버거 버튼 -->
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMenu"
            aria-controls="navbarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <!-- 햄버거로 접힐 영역 -->
          <div class="collapse navbar-collapse" id="navbarMenu">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item" v-if="!isLoggedIn">
                <RouterLink :to="{ name: 'signin' }" class="nav-link" :style="{ color: isScrolledColor }">
                  로그인
                </RouterLink>
              </li>
                <li class="nav-item" v-else>
                  <button class="nav-link btn btn-link" @click="logout" :style="{ color: isScrolledColor }">
                    로그아웃
                  </button>
                </li>
              <li class="nav-item">
                <RouterLink :to="{
                  name: 'product',
                  params: { 'type': 'deposit', 'bank': 'all', 'trm': '1000' }
                }" class="nav-link" :style="{ 'color': isScrolledColor }">
                  예금/적금 비교
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'search' }" class="nav-link" :style="{ color: isScrolledColor }">
                  검색 기업 영상
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'gold_silver' }" class="nav-link" :style="{ color: isScrolledColor }">
                  국제 금/은 시세
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'bank' }" class="nav-link" @click="navbarStore.closeMenu"
                  :style="{ color: isScrolledColor }">
                  주변 은행 찾기
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'profile' }" class="nav-link">
                  내 프로필
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'home' }" class="nav-link" :style="{ color: isScrolledColor }">
                  커뮤니티
                </RouterLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>

    <footer class="row">
      <h3 class="fs-5 fw-bold">SSAFY Final Project</h3>
      <p class="mb-0">Park-junha, Kim-taegyun - Service &nbsp;&nbsp;🏁</p>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
import { onMounted, onUnmounted, ref, computed } from 'vue'
import { useNavbarStore } from './stores/navbar'
import { useUserStore } from './stores/user'
// import VideoList from '@/views/VideoList.vue'
// import VideoListDetail from '@/components/VideoListDetail.vue'
// import {}

const router = useRoute()
const userStore = useUserStore()
const navbarStore = useNavbarStore()
const isScrolled = ref(false)
const isScrolledColor = ref('')
const isLoggedIn = computed(() => userStore.isLogin)

const logout = () => {
  userStore.logout()
  router.push({ name: 'signin' })
}

const handleScroll = () => {
  isScrolled.value = window.scrollY > 0
  isScrolledColor.value = isScrolled.value ? 'black' : 'white'
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const isSearchVisible = ref(false)
function toggleSearch() {
  isSearchVisible.value = !isSearchVisible.value
} 
</script>

<style scoped>
* {
  white-space: nowrap;
  overflow: visible;
}

.container-custom {
  display: flex;
  align-items: center;
  justify-content: end;
}

.navbar-custom {
  width: 100%;
  position: fixed;
  top: 0;
  z-index: 1000;
  padding-top: 20px;
  border-bottom: 1px solid #818a92;
  font-weight: bold;
}

.navbar-scrolled {
  background-color: white;
}

.navbar-custom .navbar-brand img {
  width: 50px;
  height: 50px;
}

.navbar-custom .navbar-nav {
  display: flex;
  flex-direction: row;
}

.navbar-custom .navbar-nav .nav-link {
  color: #ffffff;
  margin-right: 50px;
  font-size: 27px;
}

.navbar-custom .navbar-nav .nav-link:hover {
  text-decoration: underline;
  text-underline-offset: 10px;
}

.nav-link-scrolled {
  color: black;
  margin-right: 50px;
  font-size: 27px;
}

footer {
  margin-top: 30px;
  margin-bottom: 0px;
  padding-top: 20px;
  background-color: whitesmoke;
  height: 100px;
  width: 100%;
  border-top: 2px solid whitesmoke;
  text-align: center;
  display: flex;
  align-content: start;
}

.navbar-toggler {
  background-color: rgba(240, 240, 240, 0.1);
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
}

/* 네비바가 흰색일때 햄버거 버튼 줄을 검은색으로 변경 */
.navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='black' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

/* 네비바가 이미지로 어두울때 햄버거 버튼 줄을 흰색으로 변경 */
.navbar-dark .navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='white' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar-scrolled .navbar-toggler {
  background-color: rgba(240, 240, 240, 0.9);
  /* border: none;
  padding: 6px 10px;
  border-radius: 4px; */
}

.navbar-logo {
  height: 40px;
  width: auto;
  object-fit: contain;
  margin-right: 10px;
}
</style>