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
      const res = await axios.post('http://127.0.0.1:8000/api/v1/recommendAi/recommend/ai/', { purpose }, 
        { headers: {
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
  
  const resetProducts = () => {
    aiProducts.value = null
    // 필요한 경우, 다른 관련 상태도 초기화
  }

  return { aiProducts, fetchAiProducts, resetProducts, }
})
