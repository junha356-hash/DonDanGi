// stores/user.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', {
  state: () => ({
    isLogin: !!localStorage.getItem('token'), // 초깃값 설정
    depositList: [],  // 내가 추가한 예금 상품 리스트
    savingList: [],   // 내가 추가한 적금 상품 리스트
  }),
  actions: {
    login(token) {
      localStorage.setItem('token', token)
      this.isLogin = true
    },
    logout() {
      localStorage.removeItem('token')
      this.isLogin = false
      this.depositList = []
      this.savingList = []
    },
    checkLogin() {
      this.isLogin = !!localStorage.getItem('token')
    },
    // [1] 내 상품 리스트 조회
    async fetchMyProducts() {
      try {
        const token = localStorage.getItem('token')
        const res = await axios.get('http://127.0.0.1:8000/api/v1/user/products/', {
          headers: { 'Authorization': `Token ${token}` }
        })
        // 예시: {deposits: [...], savings: [...]}
        this.depositList = res.data.deposits || []
        this.savingList = res.data.savings || []
      } catch (e) {
        this.depositList = []
        this.savingList = []
      }
    },
    // [2] 내 상품 추가
    async addMyProduct(type, fin_prdt_cd) {
      const token = localStorage.getItem('token')
      await axios.post('http://127.0.0.1:8000/api/v1/user/products/', {
        type, fin_prdt_cd
      }, {
        headers: { 'Authorization': `Token ${token}` }
      })
      await this.fetchMyProducts()
    },
    // [3] 내 상품 제거
    async removeMyProduct(type, fin_prdt_cd) {
      const token = localStorage.getItem('token')
      // 백엔드 API에 따라 params 전달방식 조정 (REST라면 URL, 아니면 body/query 등)
      await axios.delete(`http://127.0.0.1:8000/api/v1/user/products/${fin_prdt_cd}/`, {
        headers: { 'Authorization': `Token ${token}` },
        params: { type }
      })
      await this.fetchMyProducts()
    }
  }
})
