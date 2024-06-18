<template>
    <div class="service-record-details">
      <h2>维修记录详情</h2>
      <div v-if="record" class="details">
        <p><span class="label">记录ID:</span> {{ record.RecordID }}</p>
        <p><span class="label">服务类型:</span> {{ record.ServiceType }}</p>
        <p><span class="label">预约日期:</span> {{ record.Date }}</p>
        <p><span class="label">描述:</span> {{ record.Description }}</p>
        <h3>用户信息</h3>
        <p><span class="label">姓名:</span> {{ user.Name }}</p>
        <p><span class="label">角色:</span> {{ user.Role }}</p>
        <p><span class="label">邮箱:</span> {{ user.Email }}</p>
        <p><span class="label">电话:</span> {{ user.Phone }}</p>
        <h3>车辆信息</h3>
        <p><span class="label">车型:</span> {{ vehicle.Model }}</p>
        <p><span class="label">车牌号:</span> {{ vehicle.LicensePlate }}</p>
        <p><span class="label">车辆识别码 (VIN):</span> {{ vehicle.VIN }}</p>
        <p><span class="label">购买日期:</span> {{ vehicle.PurchaseDate }}</p>
      </div>   
      <PopBox
      :isVisible="isModalVisible"
      title="处理维修记录"
      @close="closeModal"
      @confirm="handleModalConfirm"
    ></PopBox>
      <button @click="openModal" class="back-button">处理</button>
      <button @click="goBack" class="back-button">返回</button>
    </div>
  </template>
  
<script>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import PopBox from '@/components/PopBox.vue';

export default {
  components: {
    PopBox
  },
  data() {
    return {
      isModalVisible: false,
    };
  },
  methods: {
    openModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
    handleModalConfirm(modalData) {
      const service = {
        vehicleLicense: this.vehicle.LicensePlate,
        serviceType: this.record.ServiceType,
        date: this.record.Date,
        ...modalData
      };
      this.submitRecord(service);
    },
    submitRecord(service) {
      // 提交维修记录到后端
      axios.post('http://10.193.160.177:5000/api/submit_processed_records', service)
        .then(response => {
          console.log(response)
          alert('维修记录已提交');
          this.closeModal();
        })
        .catch(error => {
          console.error('提交维修记录时出错:', error);
          alert('提交维修记录时出错');
        });
    }
  },
  setup() {
    const route = useRoute();
    const recordID = route.params.id; // 假设URL格式为 /record/:id
    const API_URL = 'http://10.193.160.177:5000/api'; 
    const router = useRouter();

    const record = ref({});
    const user = ref({});
    const vehicle = ref({});

    const fetchRecord = async () => {
      try {
        const response = await axios.get(`${API_URL}/pending_service_records/${recordID}`);
        console.log("record:", response.data)
        record.value = response.data.record;
        user.value = response.data.user;
        vehicle.value = response.data.vehicle;
      } catch (error) {
        console.error('There was an error fetching the record:', error);
      }
    };
    const goBack = () => {
      router.back();
    };
    onMounted(fetchRecord);

    return {
      record,
      user,
      vehicle,
      goBack
    };
  }
};
</script>
  
  <style scoped>
  .service-record-details {
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
  
  .details h3 {
    color: #333;
    margin-top: 20px;
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
    display: flex;
    align-items: center;
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
  