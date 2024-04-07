<template>
  <div class="forum">
    <div class="row">
      <!-- 左侧主内容区 -->
      <div class="col-lg-9 mb-3">
        <!-- 论坛过滤器 -->
        <ForumFilters />

        <!-- 论坛帖子列表 -->
        <!-- 假设 'posts' 是一个包含帖子数据的数组 -->
        <ForumPost v-for="post in posts" :key="post.id" :post="post" />

      </div>

      <!-- 右侧侧边栏 -->
      <div class="col-lg-3 mb-4 mb-lg-0">
        <SidebarWidget />
      </div>
    </div>
  </div>
</template>
<script>
import ForumPost from '../components/ForumPost.vue';
import ForumFilters from '../components/ForumFilters.vue';
import SidebarWidget from '../components/SidebarWidget.vue';
"https://code.jquery.com/jquery-1.10.2.min.js"
export default {
  name: 'ForumPage',
  components: {
    ForumFilters,
    ForumPost,
    SidebarWidget
  }, 
  data() {
    return {
      // 示例数据，实际应用中你可能需要从API获取
      posts: [
        {
          id: 1,
          title: 'Drupal 8 quick starter guide',
          timeAgo: '20 minutes',
          author: 'KenyeW',
          tags: ['#C++', '#AppStrap Theme', '#Wordpress'],
          votes: 141,
          replies: 122,
          views: 290
        },
        {
        id: 1,
        title: 'Vue.js 3.0 Overview',
        timeAgo: '30 minutes',
        author: 'VueMaster',
        tags: ['#Vue3', '#JavaScript'],
        votes: 100,
        replies: 50,
        views: 200
      },
      {
        id: 2,
        title: 'Understanding Vite Build Tool',
        timeAgo: '1 hour',
        author: 'DevJoe',
        tags: ['#Vite', '#Vue', '#BuildTools'],
        votes: 80,
        replies: 40,
        views: 150
      },
      {
        id: 3,
        title: 'Why Tailwind CSS is the Future',
        timeAgo: '2 hours',
        author: 'CSSGuru',
        tags: ['#TailwindCSS', '#CSS', '#Design'],
        votes: 75,
        replies: 30,
        views: 175
      },
      {
        id: 4,
        title: 'Introduction to Pinia for State Management',
        timeAgo: '3 hours',
        author: 'StateManager',
        tags: ['#Pinia', '#Vue', '#StateManagement'],
        votes: 90,
        replies: 60,
        views: 190
      },
      ]
    }
  }
}
</script>
<style>
@import "https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css";
.forum{
    margin-top:20px;
    background:#eee;
    color: #708090;
}
.icon-1x {
    font-size: 24px !important;
}
a{
    text-decoration:none;    
}
.text-primary, a.text-primary:focus, a.text-primary:hover {
    color: #00ADBB!important;
}
.text-black, .text-hover-black:hover {
    color: #000 !important;
}
.font-weight-bold {
    font-weight: 700 !important;
}
</style>