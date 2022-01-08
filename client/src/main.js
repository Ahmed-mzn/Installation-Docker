import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = 'http://0.0.0.0:8000/api/v1'

createApp(App).use(router, axios).mount('#app')
