import { createApp } from 'vue'
import './style.css' // Esta linha é OBRIGATÓRIA para o Tailwind funcionar
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')