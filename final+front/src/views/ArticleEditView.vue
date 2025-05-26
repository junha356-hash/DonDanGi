<template>
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/community.jpg" alt="community_img" 
      data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">커뮤니티</span>
      </h1>
    </section>
    <div class="col-lg-8 mx-auto">
      <!-- 썸네일 및 타이틀 영역 -->
      <!-- 수정 폼 -->
      <div class="bg-white border rounded-3 p-4 shadow-sm mb-4">
        <form @submit.prevent="updateArticle">
          <div class="mb-3">
            <label class="form-label fw-semibold text-primary">제목</label>
            <input
              v-model="editTitle"
              placeholder="제목을 입력하세요"
              class="form-control"
              maxlength="100"
              required
            />
          </div>
          <div class="mb-3">
            <label class="form-label fw-semibold text-primary">내용</label>
            <textarea
              v-model="editContent"
              placeholder="내용을 입력하세요"
              rows="8"
              class="form-control"
              required
            />
          </div>
          <div class="d-flex justify-content-end gap-2">
            <button type="submit" class="btn btn-primary px-4">저장</button>
            <button type="button" class="btn btn-outline-secondary px-4" @click="goBack">취소</button>
          </div>
        </form>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
const articleId = route.params.articleId
const token = localStorage.getItem('token')
const editTitle = ref('')
const editContent = ref('')

// 기존 데이터 불러오기
onMounted(async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/`, {
    headers: { 'Authorization': `Token ${token}` }
  })
  if (res.ok) {
    const data = await res.json()
    editTitle.value = data.title
    editContent.value = data.content
  }
})

const updateArticle = async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/`, {
    method: 'PUT',
    headers: {
      'Authorization': `Token ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      title: editTitle.value,
      content: editContent.value
    })
  })
  if (res.ok) {
    router.push({ name: 'articleDetail', params: { articleId } })
  } else {
    alert('수정 실패')
  }
}

const goBack = () => {
  router.back()
}

</script>
