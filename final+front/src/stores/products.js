import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const aiProducts = ref(null)

  const fetchAiProducts = async () => {
    try {
      const token = localStorage.getItem('token')
      if (!token) {
        alert('로그인이 필요합니다!')
        return
      }
      const res = await axios.get('http://127.0.0.1:8000/api/v1/recommendAi/recommend/ai/', {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
      aiProducts.value = res.data
      console.log('[추천 데이터]', aiProducts.value)
    } catch (err) {
      // 에러가 발생할 경우 콘솔 출력!
      console.error('[추천 에러]', err)
      alert('추천 API 호출 실패: ' + (err?.response?.status || '') + '\n' + (err?.response?.data?.detail || err.message))
    }
  }

  return { aiProducts, fetchAiProducts }
})
