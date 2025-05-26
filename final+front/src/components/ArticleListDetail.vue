<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">커뮤니티</span>
    </h1>
  </section>
  <div class="container py-4">
    <div class="col-lg-8 mx-auto">
      <!-- 썸네일 및 타이틀 영역 -->
      <div class="article-header mb-4 p-0">
        <h1 class="article-title display-5 fw-bold text-primary border-bottom border-3 pb-2 mt-3 text-center">
          {{ article.title }}
        </h1>
      </div>

      <!-- 본문 및 버튼 영역 -->
      <div class="bg-white border rounded-3 p-4 shadow-sm mb-4">
        <p class="fs-5 mb-2">{{ article.content }}</p>
        <div class="d-flex gap-2 mb-3" v-if="isMyArticle">
          <button class="btn btn-outline-primary btn-sm" @click="editArticle">수정</button>
          <button class="btn btn-outline-danger btn-sm" @click="deleteArticle">삭제</button>
        </div>
      </div>

      <!-- 댓글 영역 -->
      <div class="comment-section p-4 border rounded-3 shadow-sm mb-4 bg-light">
        <h4 class="mb-3 text-primary border-bottom pb-2">댓글</h4>
        <div v-if="!isLoggedIn">
          <p class="text-secondary">댓글은 로그인 시 볼 수 있습니다.</p>
        </div>
        <div v-else>
          <ul class="list-unstyled">
            <li v-for="comment in comments" :key="comment.id" class="mb-3 border-bottom pb-2">
              <b class="text-primary">{{ comment.user.username }}</b>
              <span v-if="editingId !== comment.id" class="ms-2">{{ comment.content }}</span>
              <input v-else v-model="editContent" @keyup.enter="updateComment(comment.id)"
              class="form-control d-inline w-auto ms-2" style="max-width:300px;" />
              <small class="text-secondary ms-2" style="font-size: 0.9em;">
                {{ comment.created_at }}
              </small>

              <div class="d-inline ms-3" v-if="isMyComment(comment)">
                <button v-if="editingId !== comment.id" class="btn btn-link btn-sm p-0 text-primary"
                  @click="startEdit(comment)">수정</button>
                <button v-if="editingId === comment.id" class="btn btn-link btn-sm p-0 text-success"
                  @click="updateComment(comment.id)">저장</button>
                <span v-if="editingId !== comment.id">|</span>
                <button class="btn btn-link btn-sm p-0 text-danger" @click="deleteComment(comment.id)">삭제</button>
              </div>
            </li>
          </ul>
          <form @submit.prevent="createComment" class="d-flex align-items-center mt-3 gap-2">
            <input v-model="newComment" placeholder="댓글 입력" required class="form-control" style="max-width:350px;" />
            <button type="submit" class="btn btn-primary btn-sm">작성</button>
          </form>
        </div>
      </div>

      <div class="text-center">
        <RouterLink :to="{ name: 'home' }" class="btn btn-outline-primary mt-3 px-4">뒤로 가기</RouterLink>
      </div>
    </div>
  </div>
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
    fetchComments().then(() => { })
  }
})

</script>
