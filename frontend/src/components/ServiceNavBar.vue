<template>
    <div class="container-fluid">
        <header class="border-bottom lh-1 py-3">
        <div class="row flex-nowrap justify-content-between align-items-center">
          <div class="col-4 pt-1">
          </div>
          <div class="col-4 text-center">
            <RouterLink to="/" class="blog-header-logo text-body-emphasis text-decoration-none ">新能源汽车客户关系管理信息系统</RouterLink>
          </div>
          <div class="col-4 d-flex justify-content-end align-items-center">
            <a class="link-secondary" href="#" aria-label="Search">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="mx-3" role="img" viewBox="0 0 24 24"><title>Search</title><circle cx="10.5" cy="10.5" r="7.5"/><path d="M21 21l-5.2-5.2"/></svg>
            </a>
            <button @click="logout" class="btn btn-sm btn-outline-secondary text-" href="#">登出</button>
          </div>
        </div>
      </header>
  
      <div class="nav-scroller py-1 mb-3 border-bottom">
        <nav class="nav nav-underline justify-content-between">
          <RouterLink :to="`/user_profile/${userId}`" class="nav-item nav-link link-body-emphasis active">个人信息</RouterLink>
          <RouterLink to="/appointment_management" class="nav-item nav-link link-body-emphasis">预约管理</RouterLink>
          <RouterLink to="/service_record" class="nav-item nav-link link-body-emphasis">维修记录</RouterLink>
          <RouterLink to="/stock_management" class="nav-item nav-link link-body-emphasis" href="#">库存管理</RouterLink>
        </nav>
      </div>
    </div>
  </template>
  <script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
const store = useStore()
const router = useRouter()
const logout = (()=>{
  store.commit("SET_USER_TYPE_NONE");
  router.push("/")
})  
  </script>