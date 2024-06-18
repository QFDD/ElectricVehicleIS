<template>
  <div>
    <button @click="goToCreatePostPage">Create Post</button>
    <h1>车友论坛</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <h2 @click="goToPostDetail(post.id)">{{ post.title }}</h2>
        <p>{{ post.content }}</p>
      </li>
    </ul>
    <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
    <button @click="nextPage" :disabled="!hasMorePosts">下一页</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      currentPage: 1,
      postsPerPage: 10,
      hasMorePosts: true,
    };
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    goToCreatePostPage() {
      this.$router.push('/create_post');
    },
    async fetchPosts() {
      try {
        const response = await axios.get(`http://10.193.160.177:5000/blog/posts?page=${this.currentPage}&limit=${this.postsPerPage}`,
        {
      headers: {
        "ngrok-skip-browser-warning": "69420",
      }
    }
        );
        this.posts = response.data.posts;
        this.hasMorePosts = response.data.hasMorePosts;
      } catch (error) {
        console.error("Error fetching posts:", error);
      }
    },
    nextPage() {
      this.currentPage++;
      this.fetchPosts();
    },
    prevPage() {
      this.currentPage--;
      this.fetchPosts();
    },
    goToPostDetail(postId) {
      this.$router.push({ name: 'PostDetail', params: { id: postId } });
    },
  }
};
</script>

<style scoped>
h1 {
  text-align: center;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  border: 1px solid #ccc;
  margin: 10px 0;
  padding: 10px;
}
button {
  margin: 10px;
}
</style>
