<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/recommend.jpg" alt="recommend_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">AI 금융 상품 추천</span>
    </h1>
  </section>
  <div>
    <h1>AI 금융 상품 추천</h1>
    <hr>
    <textarea v-model="purpose" placeholder="예) 전세집 마련, 첫 적금, 목돈 모으기 등 목적을 입력해주세요"></textarea>
    <button @click="onClickRecommend">추천 받기</button>
    <div v-if="result">
      <pre>{{ result }}</pre>
    </div>
  </div>
  <hr>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useProductStore } from '@/stores/products'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const purpose = ref('')
const result = ref('')
const store = useProductStore()
const router = useRouter()
const userStore = useUserStore()


const onClickRecommend = async () => {
  const token = localStorage.getItem('token')
  if (!token) {
    router.push({ name: 'signin' })   // 로그인 페이지로 이동
    return
  }
  const res = await axios.post(
    'http://localhost:8000/api/v1/recommendAi/ai_product/',
    { purpose: purpose.value },
    { headers: { Authorization: `Token ${token}` } }
  )
  result.value = res.data.result
}
</script>
