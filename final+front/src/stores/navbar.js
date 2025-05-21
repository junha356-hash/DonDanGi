import { defineStore } from 'pinia'
import * as bootstrap from 'bootstrap'

export const useNavbarStore = defineStore('navbar', () => {
  const closeMenu = () => {
  const menu = document.getElementById('navbarMenu')
  if (menu.classList.contains('show')) {
    const bsCollapse = bootstrap.Collapse.getInstance(menu) || new bootstrap.Collapse(menu)
    bsCollapse.hide()
    }
  }
  return {
    closeMenu,
  }
})