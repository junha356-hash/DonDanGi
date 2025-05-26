<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">커뮤니티</span>
    </h1>
  </section>
  <div class="container py-4">
    <!-- 타이틀/썸네일 영역 -->
    <div class="article-header mb-4">
      <h1 class="display-6 fw-bold text-primary border-bottom border-3 pb-2 mt-3">
        커뮤니티
      </h1>
    </div>

    <!-- 본문 -->
    <div class="bg-white border rounded-3 p-4 shadow-sm mb-4">
      <h2 class="mb-4 text-primary fw-semibold border-bottom pb-2">게시글 생성</h2>
      <form @submit.prevent="createArticle">
        <div class="mb-3">
          <label class="form-label fw-semibold text-primary">제목</label>
          <input v-model="title" placeholder="제목을 입력하세요" class="form-control" maxlength="100" required />
        </div>
        <div class="mb-3">
          <label class="form-label fw-semibold text-primary">내용</label>
          <textarea v-model="content" placeholder="내용을 입력하세요" rows="7" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary px-4">작성</button>
        <RouterLink :to="{ name: 'home' }" class="btn btn-outline-primary ms-3 px-4">뒤로 가기</RouterLink>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { RouterLink } from 'vue-router'

const title = ref('')
const content = ref('')
const router = useRouter()

const createArticle = async () => {
  const token = localStorage.getItem('token')

  const res = await fetch('http://127.0.0.1:8000/api/v1/articles/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    },
    body: JSON.stringify({
      title: title.value,
      content: content.value
    })
  })

  if (res.ok) {
    router.push({ name: 'home' })  // ✅ 작성 후 홈으로 이동
  } else {
    alert('글 작성 실패')
  }
}
</script>

<style scoped>
.article-header {
  position: relative;
}

.article-thumbnail {
  max-height: 220px;
  object-fit: cover;
}
</style>
