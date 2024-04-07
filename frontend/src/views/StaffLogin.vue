<template>
    <main class="form-signin w-100 m-auto">
      <form>
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
    
        <div class="form-floating">
          <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
          <label for="floatingInput">Email address</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Password</label>
        </div>
    
        <div class="form-check text-start my-3">
          <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
          <label class="form-check-label" for="flexCheckDefault">
            Remember me
          </label>
        <RouterLink to="signup">
          Sign up
        </RouterLink>
        </div>
        <button @click="login"  class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
        <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2024</p>
      </form>
    </main>
  </template>
    
<script setup>
    import axios from 'axios';
    import { useRouter } from 'vue-router';
    import { ref } from 'vue';
    const credentials = ref({
      username: '',
      password: ''
    });
    const router = useRouter();

    const login = () => {
      axios.post('YOUR_SERVER_URL/auth/login', credentials.value)
        .then(response => {
          handleLoginSuccess(response)
        })
        .catch(error => {
          // 处理错误响应
          handleLoginError(error);
        });
    };

    // 处理登录成功
    const handleLoginSuccess = (response) => {
      if (response.userType === 'sales') {
            this.$store.commit('SET_USER_TYPE_SALES');
          } else if (response.userType === 'service') {
            this.$store.commit('SET_USER_TYPE_SERVICE');
          }
      router.push({ name: 'home' });
    };

    // 处理登录错误
    const handleLoginError = (error) => {
      // 显示错误消息
      alert('Login failed: ' + error.response.data.message);
    };
</script>
