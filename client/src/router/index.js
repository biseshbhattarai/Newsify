import Vue from 'vue'
import Router from 'vue-router'
import Register from '@/components/Register'
import Login from '@/components/Login'
import NewsBoard from '@/components/NewsBoard'



Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login    
    },
    {
      path: '/newsboard',
      name: 'NewsBoard',
      component: NewsBoard    
    }
  ]
})
