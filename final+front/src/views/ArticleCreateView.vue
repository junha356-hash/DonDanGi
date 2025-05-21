<template>
  <div>
      <section style="position:relative;" class="mb-5 ">
        <img src="@/assets/community.jpg" alt="community_img" 
        data-aos="zoom-out" data-aos-duration="800">
        <h1 data-aos="fade-down" data-aos-duration="1500">
          <span class="brand-name">커뮤니티</span>
        </h1>
      </section>
    <h2>게시글 생성 페이지</h2>
    <form @submit.prevent="createArticle">
      <input v-model="title" placeholder="제목" />
      <textarea v-model="content" placeholder="내용" />
      <button type="submit">작성</button>
    </form>
    <hr>
    <RouterLink :to="{ name: 'home'}">뒤로 가기</RouterLink>
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
