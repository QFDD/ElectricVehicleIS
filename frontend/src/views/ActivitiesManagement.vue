<template>
  <div>
    <h1>创建营销活动</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">活动名称</label>
        <input type="text" id="name" v-model="event.name" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="description">活动描述</label>
        <textarea id="description" v-model="event.description" class="form-control" required></textarea>
      </div>
      <div class="form-group">
        <label for="start_date">开始日期</label>
        <input type="date" id="start_date" v-model="event.start_date" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="end_date">结束日期</label>
        <input type="date" id="end_date" v-model="event.end_date" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="budget">预算</label>
        <input type="number" id="budget" v-model="event.budget" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary">创建活动</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const event = ref({
      name: '',
      description: '',
      start_date: '',
      end_date: '',
      budget: 0
    });

    const submitForm = () => {
      axios.post('http://10.193.160.177:5000/sales/marketing_events', event.value)
        .then(() => {
          alert('successfully market events');
        })
        .catch(error => {
          console.error("There was an error creating the marketing event:", error);
        });
    };

    return {
      event,
      submitForm
    };
  }
};
</script>

<style scoped>

</style>
