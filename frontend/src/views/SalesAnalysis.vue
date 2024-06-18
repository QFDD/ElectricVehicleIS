<template>
  <div>
    <button @click="fetchSalesData('1year')" :disabled="disableButton">1年</button>
    <button @click="fetchSalesData('3years')" :disabled="disableButton">3年</button>
    <button @click="fetchSalesData('5years')" :disabled="disableButton">5年</button>
    <button @click="fetchSalesData('all')" :disabled="disableButton">全部</button>
    <canvas id="sales-chart"></canvas>
  </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  name: 'SalesChart',
  data() {
    return {
      salesData: [],
      chart: null,
      disableButton: false,
    };
  },
  methods: {
    async fetchSalesData(period) {
      try {
        this.disableButton = true;
        setTimeout(() => {
          this.disableButton = false;
        }, 1100);//防抖动
        const response = await axios.get(`http://10.193.160.177:5000/sales/sales_records?period=${period}`, {
      headers: {
        'ngrok-skip-browser-warning': 69420
      }
    });
        console.log(response)
        this.salesData = response.data;
        this.renderChart();
      } catch (error) {
        console.error("Error fetching sales data:", error);
        this.error = "Failed to fetch sales data. Please try again later.";
      }
      finally {
        this.loading = false;
      }
    },
    renderChart() {
      try {
      if (this.chart) {
        this.chart.destroy();
        this.chart = null;
      }

      const ctx = document.getElementById('sales-chart').getContext('2d');
      // 按日期对数据进行排序
      const sortedData = this.salesData.sort((a, b) => new Date(a.SaleDate) - new Date(b.SaleDate));
      const dates = sortedData.map(item => item.SaleDate);
      const prices = sortedData.map(item => item.SalePrice);      

      this.chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: dates,
          datasets: [{
            label: 'Sales Price',
            data: prices,
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: false,
          }]
        },
        options: {
          responsive: true,
          scales: {
            x: {
              type: 'category',
              title: {
                display: true,
                text: 'Date'
              }
            },
            y: {
              title: {
                display: true,
                text: 'Price'
              }
            }
          }
        }
      });} catch (error) {
        console.error("Error rendering chart:", error);
        this.error = "Failed to render chart. Please try again later.";
      }
    },
  },
  async mounted() {
    await this.fetchSalesData('all');
  }
};
</script>

<style>
#sales-chart {
  max-width: 100%;
  height: auto;
}
</style>
