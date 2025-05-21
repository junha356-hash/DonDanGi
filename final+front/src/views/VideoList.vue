<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/Video.jpg" alt="Vidoe_img" data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">검색 기업 영상</h1>
  </section>
  <!-- <RouterLink :to="{ name: 'later' }" class="text-decoration-none text-dark">
    <button>나중에 볼 동영상</button>
  </RouterLink> -->
  <hr>

  <!-- 🔍 검색창 -->
  <form class="d-flex mb-4" @submit.prevent="fetchVideos">
    <input v-model="searchKeyword" class="form-control me-2" type="text" placeholder="검색어를 입력하세요" />
    <button class="btn btn-success" type="submit">검색</button>
  </form>
  <hr>

  <!-- 📋 결과 리스트 -->
  <div class="row">
    <div class="col-md-4 mb-4" v-for="video in videos" :key="video.id.videoId">
      <div class="card h-100"
        @click="$router.push({ name: 'detail', params: { id: video.id.videoId }, query: { title: video.snippet.title, description: video.snippet.description } })">
        <img :src="video.snippet.thumbnails.medium.url" class="card-img-top" alt="썸네일" />
        <div class="card-body">
          <h5 class="card-title">{{ video.snippet.title }}</h5>
          <p class="card-text">{{ video.snippet.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

// 📌 검색 키워드
const searchKeyword = ref('')
const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
const videos = ref([])
const fetchVideos = async () => {
  if (!searchKeyword.value.trim()) return

  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=9&q=${encodeURIComponent(
    searchKeyword.value
  )}&key=${API_KEY}`

  try {
    const response = await fetch(url)
    const data = await response.json()
    videos.value = data.items
  } catch (error) {
    console.error('YouTube API 요청 실패:', error)
  }
}
</script>

<style scoped>
.card-img-top {
  height: 180px;
  object-fit: cover;
}
.card-body {
  overflow: hidden;
}

.card-title,
.card-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
