<template>
  <div v-if="isVisible" class="modal-overlay">
    <div class="modal-container">
      <div class="modal-header">
        <h3>{{ title }}</h3>
      </div>
      <div class="modal-body">
        <form @submit.prevent="confirmAction">
          <div class="mb-3">
            <label for="cost" class="form-label">费用：</label>
            <input type="number" v-model="cost" id="cost" class="form-control" required>
          </div>
          <div class="mb-3">
            <label for="description" class="form-label">服务描述：</label>
            <textarea v-model="description" id="description" class="form-control" required></textarea>
          </div>
          <div class="mb-3">
            <label for="repair-staff-id" class="form-label">维修人员ID：</label>
            <input type="text" v-model="repairStaffId" id="repair-staff-id" class="form-control" required>
          </div>
          <div class="modal-footer">
            <button @click="closeModal" class="btn">取消</button>
            <button type="submit" class="btn btn-primary">确认</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isVisible: Boolean,
    title: String
  },
  data() {
    return {
      cost: '',
      description: '',
      repairStaffId: ''
    };
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
    confirmAction() {
      const record = {
        cost: this.cost,
        description: this.description,
        repairStaffId: this.repairStaffId
      };
      this.$emit('confirm', record);
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-container {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.modal-body {
  padding: 10px 0;
}
.modal-footer {
  display: flex;
  justify-content: flex-end;
  border-top: 1px solid #ccc;
  padding-top: 10px;
}
.btn {
  margin: 0 5px;
}
</style>
