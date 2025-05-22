<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">{{ article.title }}</span>
    </h1>
  </section>
  <h2>{{ article.title }}</h2>
  <p class="mb-2">{{ article.content }}</p>
  <div class="mb-3">
    <button v-if="isMyArticle" @click="deleteArticle">삭제</button>
    <button v-if="isMyArticle" @click="editArticle">수정</button>
  </div>

  <hr>
  <h4>댓글</h4>
  <div v-if="!isLoggedIn">
    <p class="text-secondary">댓글은 로그인 시 볼 수 있습니다.</p>
  </div>
  <div v-else>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <b>{{ comment.user.username }}</b>:
        <span v-if="editingId !== comment.id">{{ comment.content }}</span>
        <input v-else v-model="editContent" @keyup.enter="updateComment(comment.id)" />
        <!-- 본인 댓글만 수정/삭제 버튼 노출 -->
         <br>
        <template v-if="isMyComment(comment)">
          <button v-if="editingId !== comment.id" @click="startEdit(comment)">수정</button>
          <button v-if="editingId === comment.id" @click="updateComment(comment.id)">저장</button>
          | <button @click="deleteComment(comment.id)">삭제</button>
        </template>
      </li>
    </ul>
    <form @submit.prevent="createComment">
      <input v-model="newComment" placeholder="댓글 입력" required />
      <button type="submit">작성</button>
    </form>
  </div>
  <hr>
  <RouterLink :to="{ name: 'home' }">뒤로 가기</RouterLink>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute()
const router = useRouter()
const articleId = route.params.articleId
const token = localStorage.getItem('token')
const username = localStorage.getItem('username') // 반드시 저장되어 있어야 함!
const isLoggedIn = computed(() => !!token)
const editingId = ref(null)
const editContent = ref('')
const article = ref({})
const comments = ref([])
const newComment = ref('')

// 게시글 상세 정보
const fetchArticle = async () => {
  const headers = {};
  if (token) {
    headers['Authorization'] = `Token ${token}`;
  }
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/`, { headers });
  if (res.ok) article.value = await res.json();
}


// 댓글 목록 (로그인 시에만 호출)
const fetchComments = async () => {
  if (!isLoggedIn.value) {
    comments.value = []
    return
  }
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/comments/`, {
    headers: { 'Authorization': `Token ${token}` }
  })
  if (res.ok) comments.value = await res.json()
}

// 댓글 작성
const createComment = async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/comments/`, {
    method: 'POST',
    headers: {
      'Authorization': `Token ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ content: newComment.value })
  })
  if (res.ok) {
    newComment.value = ''
    fetchComments()
  }
}

// 댓글 삭제
const deleteComment = async (commentId) => {
  if (!confirm('댓글을 삭제하시겠습니까?')) return
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/comments/${commentId}/`, {
    method: 'DELETE',
    headers: { 'Authorization': `Token ${token}` }
  })
  if (res.ok) fetchComments()
}

// 게시글 삭제
const deleteArticle = async () => {
  if (!confirm('게시글을 삭제하시겠습니까?')) return
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/`, {
    method: 'DELETE',
    headers: { 'Authorization': `Token ${token}` }
  })
  if (res.ok) router.push({ name: 'home' })
}

// 게시글 수정
const editArticle = () => {
  router.push({ name: 'articleEdit', params: { articleId } })
}

// 내 댓글인지 확인
const isMyComment = (comment) => {
  // user가 객체로 올 수도 있고, username만 올 수도 있음 (API 응답에 따라!)
  if (!username) return false
  return comment.user && comment.user.username === username
}

// 내 게시글인지 확인
const isMyArticle = computed(() => {
  return article.value.user && article.value.user.username === username
})

// 댓글 수정 상태
const startEdit = (comment) => {
  editingId.value = comment.id
  editContent.value = comment.content
}

// 댓글 저장(수정)
const updateComment = async (commentId) => {
  const res = await fetch(`http://127.0.0.1:8000/api/v1/articles/${articleId}/comments/${commentId}/`, {
    method: 'PUT',
    headers: {
      'Authorization': `Token ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ content: editContent.value })
  })
  if (res.ok) {
    editingId.value = null
    fetchComments()
  }
}

onMounted(() => {
  fetchArticle()
  if (isLoggedIn.value) {
    fetchComments().then(() => {})
  }
})

</script>
