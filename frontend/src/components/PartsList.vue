<template>
    <div>
      <h2>零配件列表</h2>
      <table>
        <thead>
          <tr>
            <th>型号</th>
            <th>库存量</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="part in parts" :key="part.id">
            <td>{{ part.model }}</td>
            <td>{{ part.stock }}</td>
            <td><button @click="viewDetails(part.id)">查看详情</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        parts: [{model:'1',stock:1}]
      };
    },
    created() {
      this.fetchParts();
    },
    methods: {
      fetchParts() {
        // 假设我们有一个API端点来获取零配件列表
        fetch('/api/parts')
          .then(response => response.json())
          .then(data => {
            this.parts = data;
          });
      },
      viewDetails(id) {
        this.$router.push(`/parts/${id}`);
      }
    }
  };
  </script>
  