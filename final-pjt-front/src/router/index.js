import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: () => import('../views/SignUpView.vue')
  },
  {
    path: '/login',
    name: 'LogInView',
    component: () => import('../views/LogInView.vue')
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
