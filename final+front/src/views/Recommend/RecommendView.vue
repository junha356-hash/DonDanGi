<template>
  <div>
    <section style="position:relative;" class="mb-5 ">
      <img src="@/assets/recommend.jpg" alt="recommend_img" data-aos="zoom-out" data-aos-duration="800">
      <h1 data-aos="fade-down" data-aos-duration="1500">
        <span class="brand-name">커뮤니티</span>
      </h1>
    </section>
    <h1>AI 금융 상품 추천</h1>
    <button @click="onClickRecommend">추천 받기</button>
    <hr>
    <div v-if="store.aiProducts">
      <h2>예금 추천</h2>
      <div>
        <span>상품명: {{ store.aiProducts['예금']['상품 이름'] }}</span><br>
        <span>은행: {{ store.aiProducts['예금']['은행'] }}</span><br>
        <span>금리: {{ store.aiProducts['예금']['금리'] }}%</span><br>
        <span>저축기간: {{ store.aiProducts['예금']['저축 기간'] }}개월</span><br>
        <span>추천 이유: {{ store.aiProducts['예금']['추천 이유'] }}</span>
      </div>
      <hr>
      <h2>적금 추천</h2>
      <div>
        <span>상품명: {{ store.aiProducts['적금']['상품 이름'] }}</span><br>
        <span>은행: {{ store.aiProducts['적금']['은행'] }}</span><br>
        <span>금리: {{ store.aiProducts['적금']['금리'] }}%</span><br>
        <span>저축기간: {{ store.aiProducts['적금']['저축 기간'] }}개월</span><br>
        <span>추천 이유: {{ store.aiProducts['적금']['추천 이유'] }}</span>
      </div>
    </div>
    <div v-else>
      <p>아직 추천 데이터가 없습니다. 버튼을 눌러주세요.</p>
    </div>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/products'
import { useRouter } from 'vue-router'

const store = useProductStore()
const router = useRouter()

const onClickRecommend = () => {
  const token = localStorage.getItem('token')
  if (!token) {
    router.push({ name: 'signin' })   // 로그인 페이지로 이동
    return
  }
  store.fetchAiProducts()   // 로그인 상태면 추천 기능 실행
}
</script>
