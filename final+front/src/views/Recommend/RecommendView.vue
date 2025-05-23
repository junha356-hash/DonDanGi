<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/recommend.jpg" alt="recommend_img" data-aos="zoom-out" data-aos-duration="600"
      style="filter:brightness(0.5)">
    <h1 data-aos="fade-down" data-aos-duration="1500">상품 추천 서비스</h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">GPT-4o-mini를 사용한</h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">금융 상품 추천 서비스를 제공합니다.</h4>
  </section>
  <div class="container-content d-flex flex-column align-items-center" style="max-width: 1400px;">
    <h1 class="fw-bold">금융 상품 추천 서비스</h1>
    <hr>

    <div class="ms-4 mt-5" style="min-width:1000px;">
      <div class="row" style="height: 60px; border:2px gray solid;">
        <div 
          class="d-flex justify-content-center" 
          :style="[ 
            { backgroundColor: isSelected === 'ai' ? '#0d6efd' : 'transparent' },
            { color: isSelected === 'ai' ? 'white' : 'black' } 
          ]" 
          @click="goBoard('ai')"
        >
          <div class="d-flex align-items-center justify-content-center">
            <p class="fs-3 fw-bold mb-0" style="text-decoration: none;">
              AI 상품 추천
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <RecommendAiView />

</template>

<script setup>
import { useProductStore } from '@/stores/D_S'
import { ref, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import RecommendAiView from './RecommendAiView.vue'

const store = useProductStore()
const userStore = useUserStore()
const router = useRouter()
const isSelected = ref('ai')

const goBoard = (type) => {
  isSelected.value = type
  if (type === 'ai') {
    router.push({ name: 'ai', params: { 'username': userStore.username } })
  } else {
    router.push({ name: 'cosine' })
  }
}

</script>