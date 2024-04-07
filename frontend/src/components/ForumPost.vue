<template>
    <div class="card row-hover pos-relative py-3 px-3 mb-3 border-primary">
      <div class="row align-items-center">
        <div class="col-md-8">
          <h5>
            <a href="#" class="text-primary">{{ post.title }}</a>
          </h5>
          <p class="text-sm">
            Posted <a class="text-black" href="#">{{ post.timeAgo }}</a> ago by <a class="text-black" href="#">{{ post.author }}</a>
          </p>
          <!-- Tags -->
          <div class="text-sm op-5">
            <a class="text-black mr-2" href="#" v-for="tag in post.tags" :key="tag">{{ tag }}</a>
          </div>
        </div>
        <div class="col-md-4">
          <div class="row text-center">
            <div class="col">
              <i class="ion-connection-bars icon-1x"></i>
              <span class="d-block text-sm">{{ post.votes }} Votes</span>
            </div>
            <div class="col">
              <i class="ion-ios-chatboxes-outline icon-1x"></i>
              <span class="d-block text-sm">{{ post.replies }} Replies</span>
            </div>
            <div class="col">
              <i class="ion-ios-eye-outline icon-1x"></i>
              <span class="d-block text-sm">{{ post.views }} Views</span>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script>
  export default {
    name: 'ForumPost',
    props: {
      post: {
        type: Object,
        required: true
      }
    }
  }
</script>
  