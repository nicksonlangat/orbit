import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',

    component: () => import('../views/Home.vue')
  },
  {
    path: '/issues',
    name: 'issues',

    component: () => import('../views/Github.vue')
  },
  {
    path: '/questions',
    name: 'questions',

    component: () => import('../views/Stackoverflow.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
