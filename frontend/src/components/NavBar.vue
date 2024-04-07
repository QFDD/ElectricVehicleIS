<template>
    <div class="container-fluid text-primary" style="background-color: #5b5b5b;">
      <header class="border-bottom lh-1 py-3">
        <div class="row flex-nowrap justify-content-between align-items-center">
          <div class="col-4 pt-1">
            <RouterLink to="/staff_login" class="link-secondary" href="#">工作人员入口</RouterLink>
          </div>
          <div class="col-4 text-center">
            <RouterLink to="/" class="blog-header-logo text-body-emphasis text-decoration-none ">新能源汽车客户关系管理信息系统</RouterLink>
          </div>
          <div class="col-4 d-flex justify-content-end align-items-center">
            <a class="link-secondary" href="#" aria-label="Search">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="mx-3" role="img" viewBox="0 0 24 24"><title>Search</title><circle cx="10.5" cy="10.5" r="7.5"/><path d="M21 21l-5.2-5.2"/></svg>
            </a>
            <RouterLink to="/signin" class="btn btn-sm btn-outline-secondary text-white" href="#">Sign in</RouterLink>
          </div>
        </div>
      </header>
  
      <div class="nav-scroller py-1 mb-3 border-bottom">
        <nav class="nav nav-underline justify-content-between">
          <RouterLink to="/" class="nav-item nav-link link-body-emphasis active" href="#">首页</RouterLink>
          <RouterLink to="forum" class="nav-item nav-link link-body-emphasis" href="#">车友论坛</RouterLink>
          <RouterLink to="appointment" class="nav-item nav-link link-body-emphasis" href="#">服务预约</RouterLink>
          <RouterLink to="activities" class="nav-item nav-link link-body-emphasis" href="#">营销活动</RouterLink>
          <RouterLink to="customer_service" class="nav-item nav-link link-body-emphasis" href="#">智能客服</RouterLink>
        </nav>
      </div>
    </div>
</template>

<script setup>
</script>
<script>export default {
  name: 'NavBar'
}   
</script>

