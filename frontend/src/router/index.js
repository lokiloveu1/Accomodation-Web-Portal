import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/views/HomePage'
import Login from '@/views/Login'
import Signup from '@/views/Signup'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    }
  ]
})
