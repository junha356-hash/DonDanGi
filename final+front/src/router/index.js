import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import Gold_SilverView from '@/views/Gold_SilverView.vue'
import NearBankView from '@/views/MapView.vue'
import ProductSearchView from '@/views/D_S_Product/ProductSearchView.vue'
import ProductDetailView from '@/views/D_S_Product/ProductDetailView.vue'
import ProductView from '@/views/D_S_Product/ProductView.vue'
import VideoList from '@/views/VideoList.vue'
import VideoListDetail from '@/components/VideoListDetail.vue'
import VideoLater from '@/components/VideoLater.vue'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInView from '@/views/SignInView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import UserProfileSetupView from '@/views/UserProfileSetupView.vue'
import ArticleListDetail from '@/components/ArticleListDetail.vue'

const isAuthenticated = () => {
  return !!localStorage.getItem('token')
}
const publicPages = ['signin', 'signup']
const authPages = ['profile', 'profileSetup']

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPageView
    },
    {
      path: '/product/:type/:bank/:trm',
      component: ProductView,
      children: [
        {
          path: '',
          name: 'product',
          component: ProductSearchView
        },
        {
          path: 'detail/:productId',
          name: 'productDetail',
          component: ProductDetailView
        }
      ]
    },
    {
      path: '/gold_silver',
      name: 'gold_silver',
      component: Gold_SilverView
    },
    {
      path: '/bank',
      name: 'bank',
      component: NearBankView
    },
    {
      path: '/search',
      name: 'search',
      component: VideoList,
    },
    {
      path: '/later',
      name: 'later',
      component: VideoLater,
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: VideoListDetail,
    },
    {
      path: '/community',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView,
      meta: { requiresAuth: true },
      beforeEnter: (to, from, next) => {
        if (isAuthenticated()) next()
        else next({ name: 'signin' })  // 로그인 안했으면 로그인 페이지로 이동
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: (to, from, next) => {
        if (isAuthenticated()) next({ name: 'home' })
        else next()
      }
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignInView,
      beforeEnter: (to, from, next) => {
        if (isAuthenticated()) next({ name: 'home' })
        else next()
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: UserProfileView
    },
    {
      path: '/profile/setup',
      name: 'profileSetup',
      component: UserProfileSetupView
    },
    {
      path: '/articles/:articleId',
      name: 'articleDetail',
      component: ArticleListDetail,
    },
  ]
})

router.beforeEach((to, from, next) => {
  // 1. 프로필/프로필수정 등은 로그인 필요
  if (authPages.includes(to.name) && !isAuthenticated()) {
    return next({ name: 'signin' })
  }
  // 2. 로그인/회원가입 페이지 접근 시, 로그인 중이면 메인페이지로 리다이렉트
  if (publicPages.includes(to.name) && isAuthenticated()) {
    return next({ name: 'MainPage' })
  }
  // 3. 그 외는 모두 통과
  next()
})

// router.beforeEach((to, from) => {
//   const store = useUserStore()
//   if ( (to.name === 'createArticle' || to.name === 'updateArticle' || to.name === 'cosine' || to.name === 'ai') && !store.isLogin ) {
//     window.alert('로그인이 필요합니다')
//     return {name:'login'}
//   }
// })

export default router