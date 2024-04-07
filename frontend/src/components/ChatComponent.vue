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
import io from 'socket.io-client';

const socket = io('http://127.0.0.1:5000');
const messages = ref([]);
const newMessage = ref('');
onMounted(() => {
  socket.on('newMessage', (message) => {
    messages.value.push(message);
  });
});

// 在组件卸载时断开WebSocket连接
onUnmounted(() => {
  socket.disconnect();
});
function send() {
  if (newMessage.value.trim()) {
    socket.emit('message', { user: 'Username', content: newMessage.value });
    newMessage.value = '';  // 清空输入框
  }
}
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