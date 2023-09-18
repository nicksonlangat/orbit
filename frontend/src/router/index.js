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

    component: () => import('../views/Github.vue'),
    async beforeEnter(to, from, next) {
      try {
        const hasPermission = localStorage.getItem("hasOrbitPermission")
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/questions',
    name: 'questions',

    component: () => import('../views/Stackoverflow.vue'),
    async beforeEnter(to, from, next) {
      try {
        const hasPermission = localStorage.getItem("hasOrbitPermission")
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/login',
    name: 'login',

    component: () => import('../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'signup',

    component: () => import('../views/Signup.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
