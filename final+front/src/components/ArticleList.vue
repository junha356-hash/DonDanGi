<template>
  <div class="container my-4">
    <ul class="list-unstyled">
      <li
        v-for="article in store.articles"
        :key="article.pk"
        class="mb-4"
      >
        <RouterLink
          :to="{ name: 'articleDetail', params: { articleId: article.pk } }"
          class="article-link d-block px-4 py-3 rounded-3 border border-2 border-primary shadow-sm transition"
        >
          <h5 class="fw-bold mb-2 text-primary">{{ article.title }}</h5>
          <p class="mb-1"><span class="fw-semibold text-secondary">작성자:</span> {{ article.username }}</p>
          <p class="mb-0 text-dark text-truncate" style="max-width: 100%;">내용: {{ article.content }}</p>
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.article-link {
  background: none;
  border-left-width: 4px !important;
  border-right-width: 4px !important;
  border-top-width: 2px !important;
  border-bottom-width: 2px !important;
  border-radius: 16px;
  text-decoration: none;
  transition: box-shadow 0.15s, border-color 0.15s;
}

.article-link:hover, .article-link:focus {
  border-color: #0d6efd !important;
  box-shadow: 0 2px 10px rgba(13, 110, 253, 0.15);
  background: rgba(13, 110, 253, 0.03);
  text-decoration: none;
}

.text-primary {
  color: #0d6efd !important;
}

.text-secondary {
  color: #4f5d75 !important;
}
</style>
