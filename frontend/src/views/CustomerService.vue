<template>
  <div id="chatbot">
    <div class="chatbox">
      <div v-for="(message, index) in messages" :key="index" :class="['message', message.sender]">
        {{ message.text }}
      </div>
    </div>
    <div class="input-box">
      <input v-model="userInput" @keyup.enter="sendMessage" placeholder="输入消息..." />
      <button @click="sendMessage">发送</button>
    </div>
  </div>
</template>

<script>
import Together from 'together-ai';

export default {
  data() {
    return {
      messages: [],
      userInput: '',
      apiKey: '' // 填写api密钥llama
    };
  },
  methods: {
    async sendMessage() {
      if (this.userInput.trim() === '') return;

      const userMessage = this.userInput;
      this.messages.push({ text: userMessage, sender: 'user' });
      this.userInput = '';

      try {
        const together = new Together({
          apiKey: this.apiKey
        });

        const response = await together.chat.completions.create({
          messages: [{ role: 'user', content: userMessage }],
          model: 'mistralai/Mixtral-8x7B-Instruct-v0.1'
        });

        const botMessage = response.choices[0].message.content;
        this.messages.push({ text: botMessage, sender: 'bot' });
      } catch (error) {
        console.error('Error:', error);
        this.messages.push({ text: '对不起，发生了错误。请稍后再试。', sender: 'bot' });
      }
    }
  }
};
</script>

<style>
#chatbot {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.chatbox {
  max-height: 400px;
  height: 300px;
  overflow-y: auto;
  margin-bottom: 20px;
}

.message {
  padding: 10px;
  margin: 10px 0;
  border-radius: 10px;
}

.message.user {
  background-color: #f1f1f1;
  text-align: right;
}

.message.bot {
  background-color: #e2e2ff;
  text-align: left;
}

.input-box {
  display: flex;
}

.input-box input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px 0 0 5px;
}

.input-box button {
  padding: 10px;
  border: 1px solid #ccc;
  border-left: none;
  border-radius: 0 5px 5px 0;
  background-color: #007bff;
  color: white;
}
</style>
