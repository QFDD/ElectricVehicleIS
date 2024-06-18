<template>
  <div class="chat-container">
    <ul>
      <li v-for="message in messages" :key="message.id">
        {{ message.user }}: {{ message.content }}
      </li>
    </ul>
    <input v-model="newMessage" @keyup.enter="send" placeholder="Type a message and press Enter" />
  </div>
</template>

<script setup>

</script>

<style>
.chat-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>