<template>
  <div>
    <ul>
      <div
        v-for="article in store.articles"
        :key="article.pk"
      >
      <RouterLink :to="{ name: 'articleDetail', params: { articleId: article.pk } }" class="text-decoration-none text-dark">
        <h2>{{ article.title }}</h2>
        <p>작성자 : {{ article.username }}</p>
        <p>내용 : {{ article.content }}</p>
      </RouterLink>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style lang="scss" scoped>

</style>