<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const role = ref('')
const name = ref('')
const email = ref('')
const password = ref('')
const phone = ref('')
const router = useRouter();

const register = async () => {
  const formData = {
    name: name.value,
    email: email.value,
    password: password.value,
    role: role.value,
    phone: phone.value
  };

  try {
    const response = await axios.post('http://10.193.160.177:5000/auth/register', JSON.stringify(formData), {
      headers: { 'Content-Type': 'application/json' },
    });

    if (response.data.status === "success") {
      alert("成功注册账号");
      router.push("/signin");
    } else {
      alert("请求失败：" + response.data.message);
    }
  } catch (error) {
    console.error("请求失败", error);
    alert("请求失败");
  }
}
</script>

<template>
  <section class="vh-100" style="background-color: #eee;">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black" style="border-radius: 25px;">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">注册</p>
                  <form class="mx-1 mx-md-4" @submit.prevent="register">
                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input v-model="name" type="text" id="form3Example1c" class="form-control" required />
                        <label class="form-label" for="form3Example1c">姓名</label>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input v-model="email" type="email" id="form3Example3c" class="form-control" required />
                        <label class="form-label" for="form3Example3c">邮箱</label>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input v-model="password" type="password" id="form3Example4c" class="form-control" required />
                        <label class="form-label" for="form3Example4c">密码</label>
                      </div>
                    </div>

                    

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input type="password" id="form3Example4cd" class="form-control" />
                        <label class="form-label" for="form3Example4cd">确认密码</label>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input v-model="phone" type="text" id="form3Example3d" class="form-control" required />
                        <label class="form-label" for="form3Example3d">电话</label>
                      </div>
                    </div>

                    <div class="col-md-6 mb-4">
                      <h6 class="mb-2 pb-1">Choose your role</h6>
                      <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="customer" v-model="role" value="customer" />
                        <label class="form-check-label" for="customer">客户</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="sales" v-model="role" value="sales" />
                        <label class="form-check-label" for="sales">销售</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="service" v-model="role" value="service" />
                        <label class="form-check-label" for="service">服务</label>
                      </div>
                    </div>

                    <div class="form-check d-flex justify-content-center mb-5">
                      <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3c" />
                      <label class="form-check-label" for="form2Example3">
                        我同意所有<a href="#!">服务条款</a>
                      </label>
                    </div>

                    <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                      <button type="submit" class="btn btn-primary btn-lg">注册</button>
                    </div>
                  </form>
                </div>
                <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">
                  <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp" class="img-fluid" alt="Sample image">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* 添加样式 */
</style>
