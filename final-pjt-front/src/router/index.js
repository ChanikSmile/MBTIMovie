import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import MovieView from '../views/MovieView.vue'
import CommunityView from '../views/CommunityView.vue'
import CommunityDetailView from '../views/CommunityDetailView.vue'
import CommunityCreateView from '../views/CommunityCreateView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/detail',
    name: 'CommunityDetailView',
    component: CommunityDetailView
  },
  {
    path: '/create',
    name: 'CommunityCreateView',
    component: CommunityCreateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
