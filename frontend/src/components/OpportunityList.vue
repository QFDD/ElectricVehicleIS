<template>
    <div>
      <h1>销售机会管理</h1>
      <router-link to="/opportunity/new" class="btn btn-primary">新增机会</router-link>
      <table class="table">
        <thead>
          <tr>
            <th>名称</th>
            <th>描述</th>
            <th>状态</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="opportunity in opportunities" :key="opportunity.id">
            <td>{{ opportunity.name }}</td>
            <td>{{ opportunity.description }}</td>
            <td>{{ opportunity.status }}</td>
            <td>
              <router-link :to="`/opportunity/edit/${opportunity.id}`" class="btn btn-warning">编辑</router-link>
              <button @click="deleteOpportunity(opportunity.id)" class="btn btn-danger">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    computed: {
      opportunities() {
        return this.$store.state.opportunities;
      }
    },
    created() {
      this.$store.dispatch('fetchOpportunities');
    },
    methods: {
      deleteOpportunity(id) {
        this.$store.dispatch('deleteOpportunity', id);
      }
    }
  };
  </script>
