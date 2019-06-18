import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/views/HomePage'
import Login from '@/views/Login'
import Signup from '@/views/Signup'
import DetailPage from '@/views/DetailPage'
import SearchResult from '@/views/SearchResult'
import  Profile from '@/views/Profile'
import AddProperty from '@/views/AddProperty'

Vue.use(Router)

export default new Router({

  mode:'history',//remove the '#' in the url
  routes: [

    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
      meta:{
        isLogin:false
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta:{
        isLogin:false//do not need login
      }
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup,
      meta:{
        isLogin:false//do not need login
      }
    },
    {
      path: '/detailpage',
      name: 'DetailPage',
      component: DetailPage,
      meta:{
        isLogin:false//do not need login
      }
    },
    {
      path: '/searchresult',
      name: 'SearchResult',
      component: SearchResult,
      meta:{
        isLogin:false//do not need login
      }
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      meta: {
        isLogin: false//do not need login
      }
    },
    {
      path: '/addproperty',
      name: 'AddProperty',
      component: AddProperty,
      meta: {
        isLogin: false//do not need login
      }
    }
  ]
})


