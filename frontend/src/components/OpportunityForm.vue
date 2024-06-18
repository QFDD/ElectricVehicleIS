<template>
    <div>
      <h1>{{ isEdit ? '编辑机会' : '新增机会' }}</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="name">名称</label>
          <input type="text" id="name" v-model="opportunity.name" class="form-control" required>
        </div>
        <div class="form-group">
          <label for="description">描述</label>
          <textarea id="description" v-model="opportunity.description" class="form-control" required></textarea>
        </div>
        <div class="form-group">
          <label for="status">状态</label>
          <select id="status" v-model="opportunity.status" class="form-control" required>
            <option value="新机会">新机会</option>
            <option value="跟进中">跟进中</option>
            <option value="已关闭">已关闭</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">{{ isEdit ? '更新' : '创建' }}</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    props: ['id'],
    data() {
      return {
        opportunity: {
          name: '',
          description: '',
          status: '新机会'
        }
      };
    },
    computed: {
      isEdit() {
        return this.id !== undefined;
      }
    },
    created() {
      if (this.isEdit) {
        const opportunity = this.$store.state.opportunities.find(op => op.id === parseInt(this.id));
        if (opportunity) {
          this.opportunity = { ...opportunity };
        }
      }
    },
    methods: {
      submitForm() {
        if (this.isEdit) {
          this.$store.dispatch('updateOpportunity', this.opportunity).then(() => {
            this.$router.push('/opportunity_list');
          });
        } else {
          this.$store.dispatch('addOpportunity', this.opportunity).then(() => {
            this.$router.push('/opportunity_list');
          });
        }
      }
    }
  };
  </script>
  
