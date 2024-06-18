<template>
    <div class="card mb-3">
      <div class="card-body">
        <h5 class="card-title">{{ task.VehicleID }} - {{ task.Date }}</h5>
        <p class="card-text">{{ task.Description }}</p>
        <a @click="goToServiceRecord(task.RecordID)" class="btn btn-primary text-white">处理</a>
      </div>
    </div>
  </template>
  
<script setup>
import { defineProps, defineEmits } from 'vue'
import { useRouter } from 'vue-router';
defineProps(['task']);
defineEmits(['remove']);
const router = useRouter();

function goToServiceRecord(id) {
  router.push(`/service-records/${id}`);
}
</script>
  