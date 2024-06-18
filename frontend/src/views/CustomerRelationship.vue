<template>
    <div>
      <h1>客户关系管理</h1>
      <ul>
        <li v-for="user in users" :key="user.UserID">
          <p><strong>用户名：</strong> {{ user.Name }}</p>
          <p><strong>角色：</strong> {{ user.Role }}</p>
          <p><strong>邮件：</strong> {{ user.Email }}</p>
          <p><strong>电话：</strong> {{ user.Phone }}</p>
          <p><strong>汽车：</strong>
            <ul>
              <li v-for="car in user.Cars" :key="car.LicensePlate">{{ car.Model }} - {{ car.LicensePlate }}</li>
            </ul>
          </p>
          <button @click="goToChat(user.UserID)">Chat</button>
        </li>
      </ul>
      <button v-if="hasMoreUsers" @click="loadMoreUsers">Load More</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        users: [],
        currentPage: 1,
        hasMoreUsers: false
      }
    },
    created() {
      this.fetchUsers();
    },
    methods: {
      async fetchUsers() {
        try {
          const response = await axios.get(`http://10.193.160.177:5000/sales/users?page=${this.currentPage}&limit=10`);
          this.users = response.data.users;
          this.hasMoreUsers = response.data.hasMoreUsers;
        } catch (error) {
          console.error("Error fetching users:", error);
        }
      },
      async loadMoreUsers() {
        this.currentPage += 1;
        try {
          const response = await axios.get(`http://10.193.160.177:5000/users?page=${this.currentPage}&limit=10`);
          this.users = [...this.users, ...response.data.users];
          this.hasMoreUsers = response.data.hasMoreUsers;
        } catch (error) {
          console.error("Error loading more users:", error);
        }
      },
        goToChat(userID) {
    this.$router.push(`/chat_box/${userID}`);
  }
    }
  }
  </script>
  