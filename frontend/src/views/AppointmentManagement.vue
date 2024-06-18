<template>
  <div>
    <h1>待处理任务</h1>
    <TaskItem
      v-for="record in records"
      :key="record.RecordID"
      :task="record"
      @remove="removeRecord(record.RecordID)"
    />
    <button @click="prevPage" :disabled="page === 1">Previous</button>
    
    <span v-if="totalPages">第 {{ page }} 页/ 共 {{ totalPages }} 页</span>
    <button @click="nextPage">Next</button>
  </div>
</template>

<script>
import TaskItem from '@/components/TaskItem.vue';
import { getPendingServiceRecords, fetchTotalRecords } from '@/api/service';

export default {
  components: {
    TaskItem
  },
  data() {
    return {
      records: [],
      page: 1,
      limit: 10,
    };
  },
  mounted() {
    this.fetchRecords();
    this.fetchTotalRecords();
  },
  methods: {
    fetchRecords() {
      getPendingServiceRecords(this.page, this.limit)
        .then(response => {
          console.log('Received records:', response.data);
          this.records = response.data;
        })
        .catch(error => {
          console.error("There was an error fetching the records:", error);
        });
    },
    fetchTotalRecords() {
      fetchTotalRecords()
        .then((response) => {
          const totalRecords = response.data.total_records;
          this.totalPages = Math.ceil(totalRecords / this.limit);
          console.log('Total pages:', this.totalPages); // 打印总页数
        })
        .catch((error) => {
          console.error('There was an error fetching the total records:', error);
        });
    },
    nextPage() {
      if(this.page < this.totalPages){
        this.page += 1;
        this.fetchRecords();
      } 
    },
    prevPage() {
      if (this.page > 1) {
        this.page -= 1;
        this.fetchRecords();
      }
    },
  }
};
</script>