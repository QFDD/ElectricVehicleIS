<template>
    <div class="card mb-3">
      <div class="card-body">
        <h5 class="card-title">{{ task.customerName }} - {{ task.appointmentTime }}</h5>
        <p class="card-text">{{ task.description }}</p>
        <a href="#" class="btn btn-primary">处理</a>
        <button @click="$emit('remove')" class="btn btn-secondary">完成</button>
      </div>
    </div>
  </template>
  
<script setup>
import { defineProps, defineEmits } from 'vue'
defineProps(['task'])
defineEmits(['remove'])
</script>
  