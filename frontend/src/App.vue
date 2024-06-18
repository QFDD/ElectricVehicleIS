<template>
  <component :is="currentNavBar"></component>
  <div class="container">
    <RouterView />
    <footer>
        <p>&copy; 2024 新能源汽车客户关系管理系统. 保留所有权利。</p>
    </footer>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { RouterView} from 'vue-router';
import { useStore } from 'vuex';
import NavBar from './components/NavBar.vue'
import SalesNavBar from './components/SalesNavBar.vue';
import ServiceNavBar from './components/ServiceNavBar.vue'

const store = useStore()
const userType = computed(() => store.state.user.userType) 
const currentNavBar = computed(() => {
  if(userType.value === 'sales'){
    return SalesNavBar
  }
  else if (userType.value === 'service'){
    return ServiceNavBar
  }
  else {
    return NavBar;
  } 
});
</script>
