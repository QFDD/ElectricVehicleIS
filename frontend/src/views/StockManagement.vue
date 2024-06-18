<template>
  <div class="inventory-management">
    <h2>零配件库存管理</h2>

    <div class="parts-list">
      <table>
        <thead>
          <tr>
            <th>名称</th>
            <th>车辆型号</th>
            <th>库存数量</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="part in parts" :key="part.PartID">
            <td>{{ part.Name }}</td>
            <td>{{ part.VehicleModel }}</td>
            <td>{{ part.StockQuantity }}</td>
            <td>
              <button @click="openModal(part)">编辑</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <EditPartModal
      v-if="showModal"
      :part="editablePart"
      @close="closeModal"
      @save="savePart"
    />
  </div>
</template>

<script>
import { getParts } from '@/api/service';
import EditPartModal from '@/components/EditPartModal.vue';

export default {
  components: {
    EditPartModal
  },
  data() {
    return {
      parts: [],
      showModal: false,
      editablePart: null
    };
  },
  mounted() {
    this.fetchParts();
  },
  methods: {
    fetchParts() {
      getParts()
        .then(response => {
          this.parts = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching the records:', error);
        });
    },
    openModal(part) {
      this.editablePart = { ...part };
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    savePart(updatedPart) {
      const index = this.parts.findIndex(p => p.PartID === updatedPart.PartID);
      if (index !== -1) {
        this.parts.splice(index, 1, updatedPart);
      }
      this.closeModal();
    }
  }
};
</script>
  
<style>
  .inventory-management {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  h2, h3 {
    text-align: center;
    color: #333;
  }
  
  .parts-list, .form-section, .monitor-section {
    margin-bottom: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  table, th, td {
    border: 1px solid #ccc;
  }
  
  th, td {
    padding: 10px;
    text-align: left;
  }
  
  button {
    padding: 10px 20px;
    font-size: 14px;
    color: #fff;
    background-color: #007BFF;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  form label {
    display: block;
    margin: 10px 0 5px;
    color: #333;
  }
  
  form input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
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
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 4px;
  width: 300px;
}

.close {
  float: right;
  font-size: 20px;
  cursor: pointer;
}
</style>
  