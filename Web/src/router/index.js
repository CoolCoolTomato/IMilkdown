import { createRouter, createWebHistory } from 'vue-router'
import MainWindow from "@/views/MainWindow.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: MainWindow
    },
  ]
})

export default router
