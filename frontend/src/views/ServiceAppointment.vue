<template>
    <div class="root-element">
      <div class="container">
        <h2 class="mt-5">服务预约表单</h2>
        <form @submit.prevent="submitAppointment" class="mt-3">
          <div class="mb-3">
            <label for="service-type" class="form-label">服务类型：</label>
            <select id="service-type" v-model="serviceType" class="form-select">
              <option value="充电">充电</option>
              <option value="维修">维修</option>
              <option value="换电">换电</option>
            </select>
          </div>
  
          <div class="mb-3">
            <label for="appointment-date" class="form-label">预约日期：</label>
            <input type="date" id="appointment-date" v-model="appointmentDate" class="form-control">
          </div>
  
          <div class="mb-3">
            <label for="vehicle-info" class="form-label">车辆信息：</label>
            <input type="text" id="vehicle-info" v-model="vehicleInfo" class="form-control" placeholder="车牌号或VIN">
          </div>

          <div class="mb-3">
            <label for="vehicle-info" class="form-label">预约描述</label>
            <input type="text" id="description" v-model="description" class="form-control" placeholder="请输入本次预约情况">
          </div>

          <button type="submit" class="btn btn-primary">提交预约</button>
        </form>
      </div>
      <div class="container">
        <h2 class="mt-5">我的预约</h2>
        <div id="appointments-list" class="mt-3">
          <div v-for="appointment in appointments" :key="appointment.id" class="appointment mb-3 p-3 border rounded">
            <p>服务类型：{{ appointment.serviceType }}</p>
            <p>预约时间：{{ appointment.date }}</p>
            <p>预约描述：{{ appointment.description }}</p>
            <button @click="editAppointment(appointment.id)" class="btn btn-secondary btn-sm">修改</button>
            <button @click="cancelAppointment(appointment.id)" class="btn btn-danger btn-sm">取消</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        serviceType: '',
        appointmentDate: '',
        vehicleInfo: '',
        appointments: [],
        description: '',
      };
    },
    mounted() {
    this.fetchPendingServices();
    },
    methods: {
      submitAppointment() {
        const newAppointment = {
          serviceType: this.serviceType,
          appointmentDate: this.appointmentDate,
          vehicleInfo: this.vehicleInfo,
          description: this.description,
        };
  
        axios.post('http://10.193.160.177:5000/user/appointments', newAppointment)
          .then(response =>{if (response.status === 201) {
            alert('Appointment created successfully!');}}
          )
          .catch(error => {
            console.error('Error submitting appointment:', error);
          });
      },
      
      async fetchPendingServices() {
      try {
        const response = await fetch('http://10.193.160.177:5000/api/get_pending_services', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ userID: this.$store.state.user.id })
        });
        const data = await response.json();
        if (response.ok) {
          this.appointments = data;
        } else {
          console.error('Error fetching records:', data.error);
        }
      } catch (error) {
        console.error('Error fetching records:', error);
      }
    }
  }
    }

  </script>
  
  <style scoped>
  .root-element {
    padding: 20px;
  }
  </style>
  