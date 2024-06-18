<template>
    <div>
      <h1>发表帖子</h1>
      <form @submit.prevent="createPost">
        <div>
          <label for="title">标题：</label>
          <input type="text" id="title" v-model="title" required>
        </div>
        <div>
          <label for="content">内容：</label>
          <textarea id="content" v-model="content" required></textarea>
        </div>
        <button type="submit">发表</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        title: '',
        content: ''
      }
    },
    methods: {
      async createPost() {
        try {
          await axios.post('http://10.193.160.177:5000/blog/posts', {
            title: this.title,
            content: this.content,
            user_id: 1 // 假设当前用户ID为1，可以根据实际情况调整
          });
          alert('发表成功')
          this.$router.push('/forum');
        } catch (error) {
          console.error("Error creating post:", error);
        }
      }
    }
  }
  </script>
  