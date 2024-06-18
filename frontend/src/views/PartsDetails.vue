<template>
    <div class="part-details">
      <h2>零配件详情</h2>
      <div v-if="part" class="details">
        <p><span class="label">零配件ID:</span> {{ part.PartID }}</p>
        <p><span class="label">名称:</span> {{ part.Name }}</p>
        <p><span class="label">车辆型号:</span> {{ part.VehicleModel }}</p>
        <p><span class="label">库存数量:</span> {{ part.StockQuantity }}</p>
      </div>
      <div v-else>
        <p>正在加载...</p>
      </div>
      <button class="back-button">处理</button>
      <button @click="goBack" class="back-button">返回</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        part: {}
      };
    },
    created() {
      this.fetchPartDetails();
    },
    methods: {
      fetchPartDetails() {
        const id = this.$route.params.id;
        fetch(`/api/parts/${id}`)
          .then(response => response.json())
          .then(data => {
            this.part = data;
          });
      },
      goBack() {
        this.$router.push('/');
      }
    }
  };
  </script>
  
  <style scoped>
  .part-details {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
  }
  
  .details p {
    font-size: 18px;
    margin: 10px 0;
    color: #555;
  }
  
  .label {
    font-weight: bold;
    color: #333;
  }
  
  .back-button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    font-size: 16px;
    color: #fff;
    background-color: #007BFF;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .back-button:hover {
    background-color: #0056b3;
  }
  </style>
  