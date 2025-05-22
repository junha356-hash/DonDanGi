<template>
  <div>
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">{{ editTitle }}</span>
      </h1>
    </section>
    <h2>게시글 수정</h2>
    <form @submit.prevent="updateArticle">
      <input v-model="editTitle" required />
      <textarea v-model="editContent" required />
      <button type="submit">저장</button>
    </form>
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
</script>
