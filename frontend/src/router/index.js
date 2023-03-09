import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Chat from '@/views/Chat.vue'
import Register from '@/views/Register.vue'
import Login from '@/views/Login.vue'
import Css from '@/views/Css.vue'
import Marketplace from '@/views/Marketplace.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chat
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/css',
      name: 'css',
      component: Css
    },
    {
      path: '/marketplace',
      name: 'marketplace',
      component: Marketplace
    }
  ]
})

export default router
