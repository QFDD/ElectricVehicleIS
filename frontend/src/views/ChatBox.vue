<template>
  <div class="chatbox">
    <div class="messages">
      <div v-for="message in messages" :key="message.message_id" class="message">
        <strong>{{ message.sender_id }}:</strong> {{ message.message_text }}
      </div>
    </div>
    <div class="input">
      <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
      <button @click="sendMessage">Send</button>
      <button @click="test">test</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      messages: [],
      newMessage: '', 
      conversationId: null,
      userID: this.$route.params.id,
      currentUserId: this.$store.state.user.id, 
    };
  },
  mounted() {
    this.checkOrCreateConversation();
  },
  methods: {
    fetchMessages() {
      if (this.conversationId) {
        axios.get(`http://localhost:5000/chat/${this.conversationId}/messages`)
          .then(response => {
            this.messages = response.data;
          });
      }
    },
    sendMessage() {
      if (this.newMessage.trim() === '') return;

      const message = {
        conversation_id: this.conversationId,
        sender_id: this.currentUserId,
        message_text: this.newMessage,
      };

      axios.post(`http://localhost:5000/chat/send_messages`, message)
        .then(response => {
          this.messages.push(response.data);
          this.newMessage = '';
        });
    },
    checkOrCreateConversation() {
      axios.get(`http://localhost:5000/chat/check_conversation?user1=${this.currentUserId}&user2=${this.userID}`)
        .then(response => {
            this.conversationId = response.data.conversation_id;
            this.messages = response.data.messages;
            console.log(this.messages)
        });
    },test(){
      alert(this.userID)
    }
  }
    
}
</script>

<style>
.chatbox {
  border: 1px solid #ccc;
  padding: 10px;
  width: 100%;
}
.messages {
  height: 200px;
  overflow-y: scroll;
  border-bottom: 1px solid #ccc;
  margin-bottom: 10px;
}
.message {
  margin-bottom: 5px;
}
.input {
  display: flex;
}
.input input {
  flex: 1;
  padding: 5px;
}
.input button {
  padding: 5px;
}
</style>
