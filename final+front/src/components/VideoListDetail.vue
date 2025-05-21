<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/Video.jpg" alt="Vidoe_img" data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">영상 상세 정보</h1>
  </section>
  <h2>영상 상세 정보</h2>

  <!-- ✅ 영상 재생 -->
  <RouterLink :to="{ name: 'search' }" class="text-decoration-none text-dark">기업 검색으로 돌아가기</RouterLink>
  <hr>
  <div class="ratio ratio-16x9 mb-4">
    <iframe :src="`https://www.youtube.com/embed/${videoId}`" title="YouTube video player" allowfullscreen></iframe>
  </div>

  <!-- ✅ 영상 제목 & 설명 -->
  <h4>{{ videoTitle }}</h4>
  <p>{{ videoDescription }}</p>

  <!-- ✅ 저장/저장취소 버튼 -->
  <!-- <button class="btn" :class="isSaved ? 'btn-danger' : 'btn-primary'" @click="toggleSave">
    {{ isSaved ? '저장 취소' : '동영상 저장' }}
  </button> -->
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const videoId = ref('')
const videoTitle = ref('')
const videoDescription = ref('')
const isSaved = ref(false)

// ✅ 상세 정보 URL에서 받아오기
onMounted(() => {
  videoId.value = route.params.id
  videoTitle.value = route.query.title || '제목 없음'
  videoDescription.value = route.query.description || '설명 없음'

  const savedVideos = JSON.parse(localStorage.getItem('savedVideos') || '[]')
  isSaved.value = savedVideos.some(v => v.id === videoId.value)
})

// ✅ 저장/취소 토글
const toggleSave = () => {
  const saved = JSON.parse(localStorage.getItem('savedVideos') || '[]')
  const videoData = {
    id: videoId.value,
    title: videoTitle.value,
    description: videoDescription.value,
  }

  if (isSaved.value) {
    // 삭제
    const updated = saved.filter(v => v.id !== videoId.value)
    localStorage.setItem('savedVideos', JSON.stringify(updated))
    isSaved.value = false
  } else {
    // 저장
    saved.push(videoData)
    localStorage.setItem('savedVideos', JSON.stringify(saved))
    isSaved.value = true
  }
}
</script>

<style scoped>
iframe {
  width: 100%;
  height: 100%;
}
</style>
