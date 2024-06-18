import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import axios from 'axios';

// 配置全局请求头
axios.defaults.headers.common['ngrok-skip-browser-warning'] = 69420;
const app = createApp(App);
app.use(router);
app.use(store);

app.mount('#app'); 
