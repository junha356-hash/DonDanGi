<template>
  <div>
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/community.jpg" alt="community_img" 
      data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">커뮤니티</span>
      </h1>
    </section>
    <h1>게시글 목록 페이지</h1>
    <!-- <button @click="logout" v-if="token">로그아웃</button> -->
    <hr>
    <button @click="router.push({name: 'create'})">게시글 생성</button>
    <br>
    <!-- <p v-if="token">로그인 상태입니다.</p>
    <p v-else>비로그인 상태입니다.</p> -->
    <ArticleList />
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

<style lang="scss" scoped>

</style>