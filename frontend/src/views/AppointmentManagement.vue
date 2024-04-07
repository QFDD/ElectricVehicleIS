<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <h2>待处理的维修任务</h2>
        <TaskItem v-for="(task, index) in tasks" :key="task.id" :task="task" @remove="tasks.splice(index,1)"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import TaskItem from '@/components/TaskItem.vue';
import { ref } from 'vue'
const tasks = ref([
  {
    id: 1,
    customerName: '张三',
    appointmentTime: '2024-04-12 14:00',
    description: '空调不制冷',
    status: '待处理'
  },
  {
    id: 2,
    customerName: '李四',
    appointmentTime: '2024-04-13 10:00',
    description: '洗衣机漏水',
    status: '待处理'
  },
  // 更多任务...
])
</script>