// stores/user.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', {
  state: () => ({
    isLogin: !!localStorage.getItem('token'), // 초깃값 설정
  }),
  actions: {
    login(token) {
      localStorage.setItem('token', token)
      this.isLogin = true
    },
    logout() {
      localStorage.removeItem('token')
      this.isLogin = false
    },
    checkLogin() {
      this.isLogin = !!localStorage.getItem('token')
    }
  },
  
})
