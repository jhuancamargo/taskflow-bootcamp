import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import UsuariosView from '../views/UsuariosView.vue'
import TarefasView from '../views/TarefasView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: DashboardView },
    { path: '/usuarios', name: 'usuarios', component: UsuariosView },
    { path: '/tarefas', name: 'tarefas', component: TarefasView }
  ]
})

export default router