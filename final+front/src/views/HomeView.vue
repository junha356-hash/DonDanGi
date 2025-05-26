<template>
  <div>
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">커뮤니티</span>
      </h1>
    </section>
    <h1 style="text-align: center;">게시글 목록 페이지</h1>
    <hr>
    <div class="container" style="max-width:1100px;">
      <!-- 버튼을 왼쪽에 두고 리스트는 아래에 두기 -->
      <div class="row mb-2">
        <div class="col-auto ps-0">
          <button class="btn btn-primary px-4 py-2 fw-bold" @click="router.push({ name: 'create' })">
            <i class="bi bi-pencil-square me-2"></i> 게시글 생성
          </button>
        </div>
      </div>
      <!-- 리스트 -->
      <ArticleList />
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import ArticleList from '../components/ArticleList.vue';
import { ref, onMounted } from 'vue'

const token = ref(localStorage.getItem('token'))
const router = useRouter()
const articles = ref([])

const logout = () => {
  localStorage.removeItem('token')
  location.reload()
}

onMounted(async () => {
  const res = await fetch('http://127.0.0.1:8000/api/v1/articles/')
  const data = await res.json()
  articles.value = data
})
</script>

<style lang="scss" scoped></style>