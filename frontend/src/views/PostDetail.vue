<template>
    <div>
      <h1>{{ post.title }}</h1>
      <p>{{ post.content }}</p>
      <h3>评论</h3>
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>{{ comment.content }}</p>
          <small>{{ comment.created_at }}</small>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        post: {},
        comments: []
      };
    },
    created() {
      this.fetchPostDetails();
    },
    methods: {
      async fetchPostDetails() {
        const postId = this.$route.params.id;
        try {
          const postResponse = await axios.get(`http://10.193.160.177:5000/blog/posts/${postId}`);
          const commentsResponse = await axios.get(`http://10.193.160.177:5000/blog/posts/${postId}/comments`);
          this.post = postResponse.data.post;
          this.comments = commentsResponse.data.comments;
        } catch (error) {
          console.error("Error fetching post details:", error);
        }
      }
    }
  }
  </script>
  