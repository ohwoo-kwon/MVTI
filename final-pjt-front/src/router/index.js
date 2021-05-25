import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/accounts/Login.vue'
import Signup from '../components/accounts/Signup.vue'
import Movies from '../components/movies/Movies.vue'
import Carousel3d from 'vue-carousel-3d'


Vue.use(VueRouter)
Vue.use(Carousel3d)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/',
    name: 'Movies',
    component: Movies,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
