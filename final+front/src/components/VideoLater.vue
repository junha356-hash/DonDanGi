<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/Video.jpg" alt="Vidoe_img" data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">나중에 볼 영상</h1>
  </section>

  <!-- 저장된 동영상 없을 경우 -->
  <RouterLink :to="{ name: 'search' }" class="text-decoration-none text-dark">기업 검색으로 돌아가기</RouterLink>
  <hr>
  <p v-if="savedVideos.length === 0" class="text-muted">등록된 비디오가 없습니다.</p>

  <!-- 저장된 동영상 리스트 -->
  <div class="row" v-else>
    <div class="col-md-4 mb-4" v-for="video in savedVideos" :key="video.id">
      <div class="card h-100" @click="$router.push({
        name: 'detail',
        params: { id: video.id },
        query: {
          title: video.title,
          description: video.description
        }
      })" style="cursor: pointer;">
        <iframe class="card-img-top" :src="`https://www.youtube.com/embed/${video.id}`" allowfullscreen></iframe>
        <div class="card-body">
          <h5 class="card-title">{{ video.title }}</h5>
          <p class="card-text">{{ video.description }}</p>
          <button class="btn btn-danger" @click.stop="removeVideo(video.id)">삭제</button>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'

const savedVideos = ref([])

const loadVideos = () => {
  const data = JSON.parse(localStorage.getItem('savedVideos') || '[]')
  savedVideos.value = data
}

const removeVideo = (id) => {
  const updated = savedVideos.value.filter(video => video.id !== id)
  localStorage.setItem('savedVideos', JSON.stringify(updated))
  savedVideos.value = updated
}

onMounted(() => {
  loadVideos()
})
</script>

<style scoped>
iframe {
  width: 100%;
  height: 180px;
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
