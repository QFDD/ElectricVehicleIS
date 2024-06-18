<template>
    <div id="app">
      <h1>客户线索挖掘</h1>
      <form @submit.prevent="addLead">
        <div>
          <label for="name">姓名:</label>
          <input type="text" v-model="newLead.name" required />
        </div>
        <div>
          <label for="email">电子邮件:</label>
          <input type="email" v-model="newLead.email" required />
        </div>
        <div>
          <label for="phone">电话:</label>
          <input type="tel" v-model="newLead.phone" required />
        </div>
        <div>
          <label for="interests">兴趣:</label>
          <input type="text" v-model="newLead.interests" />
        </div>
        <button type="submit">添加客户线索</button>
      </form>
  
      <h2>已添加客户线索</h2>
      <ul>
        <li v-for="lead in leads" :key="lead.id">
          <strong>{{ lead.name }}</strong> - {{ lead.email }} - {{ lead.phone }} - {{ lead.interests }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newLead: {
          name: '',
          email: '',
          phone: '',
          interests: ''
        },
        
        leads: [],
        nextId: 1
      };
    },
    methods: {
      
      addLead() {
        const newLead = { ...this.newLead, id: this.nextId++ };
        this.leads.push(newLead);
        this.newLead.name = '';
        this.newLead.email = '';
        this.newLead.phone = '';
        this.newLead.interests = '';
      }
    }
  };
  </script>
  
  <style scoped>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    text-align: center;
    margin-top: 60px;
  }
  
  form {
    margin-bottom: 20px;
  }
  
  form div {
    margin-bottom: 10px;
  }
  
  form label {
    margin-right: 10px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    padding: 5px 0;
  }
</style>
  