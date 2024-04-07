<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="">
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
      <div class="form-floating mb-3">
        <input v-model="email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Email address</label>
      </div>
      <div class="form-floating">
        <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
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
      <button @click="login" class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
      <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2024</p>
      <button @click="test" class="btn btn-primary w-100 py-2" type="submit">test</button>
    </form>
  </main>
</template>

<script setup>
import axios from 'axios';
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex'
const store = useStore()
const router = useRouter();
const email = ref('')
const password = ref('')
const formData = reactive({
  email,
  password
});

const formDataJson = computed(() => {
  return JSON.stringify(formData);
})

const login = async () => {
  const response = await axios.post('http://127.0.0.1:5000/auth/login', formDataJson.value, {
    headers: { 'Content-Type': 'application/json' },
  });
  if (response.data.status === "success" && response.data.user_type === "client") {
    alert("Successfully Logged in");
    store.commit("SET_USER_TYPE_CUSTOMER")
    router.push('/')
  }
  else if (response.data.status === "success" && response.data.user_type === "sales") {
    alert("Sales Successfully Logged in");
    store.commit("SET_USER_TYPE_SALES")
    router.push('sales_home_page')
  }
  else if (response.data.status === "success" && response.data.user_type === "service") {
    alert("Service Successfully Logged in");
    store.commit("SET_USER_TYPE_SERVICE")
    router.push('service_home_page')
    alert(store.state.user.userType)
  }
  else {
    alert(response.data.error);
  }
}

function test() {
  alert(formDataJson.value)
}

</script>
