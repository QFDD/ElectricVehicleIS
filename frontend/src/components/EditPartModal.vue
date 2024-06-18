<template>
    <div class="modal">
      <div class="modal-content">
        <span class="close" @click="$emit('close')">&times;</span>
        <h3>编辑零配件</h3>
        <form @submit.prevent="save">
          <div>
            <label for="name">名称:</label>
            <input type="text" v-model="localPart.Name" disabled />
          </div>
          <div>
            <label for="vehicleModel">车辆型号:</label>
            <input type="text" v-model="localPart.VehicleModel" disabled />
          </div>
          <div>
            <label for="stockQuantity">库存数量:</label>
            <input type="number" v-model="localPart.StockQuantity" />
          </div>
          <button type="submit">保存</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      part: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        localPart: { ...this.part }
      };
    },
    methods: {
      save() {
        this.$emit('save', this.localPart);
      }
    }
  };
  </script>
  
  <style scoped>
  .modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
  
  .modal-content {
    background: #fff;
    padding: 20px;
    border-radius: 4px;
    width: 300px;
    position: relative;
  }
  
  .close {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
    cursor: pointer;
  }
  </style>
  