import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import MovieView from '../views/MovieView.vue'
import CommunityView from '../views/CommunityView.vue'
import CommunityDetailView from '../views/CommunityDetailView.vue'
import CommunityCreateView from '../views/CommunityCreateView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import GenreListView from '../views/GenreListView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
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
    path: '/genre',
    name: 'Genre',
    component: GenreListView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/comments',
    name: 'CommunityDetailView',
    component: CommunityDetailView
  },
  {
    path: '/create',
    name: 'CommunityCreateView',
    component: CommunityCreateView
  },
  {
    path: '/:id',
    name: 'MovieDetail',
    component: MovieDetailView,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
