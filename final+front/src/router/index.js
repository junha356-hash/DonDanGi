import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import Gold_SilverView from '@/views/Gold_SilverView.vue'
import NearBankView from '@/views/MapView.vue'
import ProductSearchView from '@/views/D_S_Product/ProductSearchView.vue'
import ProductDetailView from '@/views/D_S_Product/ProductDetailView.vue'
import ProductView from '@/views/D_S_Product/ProductView.vue'

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
      path:'/gold_silver',
      name:'gold_silver',
      component:Gold_SilverView
    },
    {
      path:'/bank',
      name:'bank',
      component:NearBankView
    },
//     {
//       path:'/community',
//       component:CommunityView,
//       children:[
//         {path:':board/', name:'community', component:BoardView},
//         {path:':board/:articleId', name:'articleDetail', component:ArticleDetailView},
//         {path:':board/create', name:'createArticle', component:CreateArticleView},
//         {path:':board/:articleId/update', name:'updateArticle', component:UpdateArticleView},
//       ]
//     },
//     {
//       path:'/profile',
//       component:ProfileView,
//       children:[
//         {path:':username/', name:'profile', component:ProfileHomeView},
//         {path:':username/update', name:'updateProfile', component:UpdateProfileView},
//       ]
//     },
//     {
//       path:'/recommend',
//       component:RecommendView,
//       children:[
//         {path:'cosine', name:'cosine', component:RecommendCosineView},
//         {path:'ai/', name:'ai', component:RecommendAiView},
//       ]
//     },
//     {
//       path:'/login',
//       name:'login',
//       component:LoginView
//     },
//     {
//       path:'/signup',
//       name:'signup',
//       component:SignUpView
//     },
  ]
})


// router.beforeEach((to, from) => {
//   const store = useUserStore()
//   if ( (to.name === 'createArticle' || to.name === 'updateArticle' || to.name === 'cosine' || to.name === 'ai') && !store.isLogin ) {
//     window.alert('로그인이 필요합니다')
//     return {name:'login'}
//   }
// })

export default router