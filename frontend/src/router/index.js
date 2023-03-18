import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Chat from '@/views/Chat.vue'
import Register from '@/views/Register.vue'
import Login from '@/views/Login.vue'
import Css from '@/views/Css.vue'
import Marketplace from '@/views/Marketplace.vue'
import Inventory from '@/views/Inventory.vue'
import Listing from '@/views/Listing.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
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
      path: '/home',
      name: 'home',
      component: Home
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
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: Inventory
    },
    {
      path: '/listing',
      name: 'listing',
      component: Listing
    },
    
  ]
})

export default router
