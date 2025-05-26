<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/recommend.jpg" alt="recommend_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">AI 금융 상품 추천</span>
    </h1>
  </section>

  <div class="container" style="max-width: 700px;">
    <div class="card shadow-sm border-primary-subtle mb-4">
      <div class="card-body">
        <h3 class="fw-bold text-primary mb-3 text-center">맞춤형 금융 상품 추천</h3>
        <form @submit.prevent="onClickRecommend">
          <div class="mb-3">
            <label for="purpose" class="form-label fw-semibold">상품 사용 목적</label>
            <textarea
              v-model="purpose"
              id="purpose"
              class="form-control"
              rows="3"
              placeholder="예) 전세집 마련, 첫 적금, 목돈 모으기 등 목적을 입력해주세요"
              required
            ></textarea>
          </div>
          <div class="d-grid">
            <button type="submit" class="btn btn-primary btn-lg" :disabled="loading">
              <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
              추천 받기
            </button>
          </div>
        </form>
      </div>
    </div>

    <div v-if="result" class="card shadow-sm border-primary mb-3">
      <div class="card-header text-black bg-primary bg-opacity-10 fw-semibold fs-5">
        AI 추천 결과
      </div>
      <div class="card-body">
        <pre class="mb-0 text-dark" style="white-space:pre-wrap;">{{ result }}</pre>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useProductStore } from '@/stores/products'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const purpose = ref('')
const result = ref('')
const loading = ref(false)
const store = useProductStore()
const router = useRouter()
const userStore = useUserStore()

const onClickRecommend = async () => {
  const token = localStorage.getItem('token')
  if (!token) {
    router.push({ name: 'signin' })
    return
  }
  loading.value = true
  try {
    const res = await axios.post(
      'http://localhost:8000/api/v1/recommendAi/ai_product/',
      { purpose: purpose.value },
      { headers: { Authorization: `Token ${token}` } }
    )
    result.value = res.data.result
  } catch (e) {
    result.value = '추천 API 호출 실패: ' + (e.response?.status || '') + '\n' + (e.response?.data?.detail || e.message)
  } finally {
    loading.value = false
  }
}
</script>
