<template>
  <div class="sendbox">
    <div class="input-box">
      <div class="input">
        <input type="text" placeholder="输入消息..." v-model="newMessage">
        <button class="btn-right" open-type="" hover-class="button-hover" @click="sendMessage()">
          发送
        </button>
        <div class="more">
          <i class="mui-icon mui-icon-paperplane"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'sendbox',
  props: {},
  setup() {
    const newMessage = ref("")
    const messages = ref()

    const sendMessage = () => {
      if (newMessage.value) {
        messages.value.push(newMessage.value);
        newMessage.value = '' // Clear input box
      }
    }
    return {
      newMessage,
      messages,
      sendMessage,
    }
  }
})
</script>

<style scoped>
.input-box {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #fff;
  padding: 10px;
  box-shadow: 0 -1px 2px rgba(0, 0, 0, 0.15);
}

.input {
  display: flex;
  justify-content: center;
}

.btn-right {
  margin-left: 10px;
  width: 80px;
  height: 40px;
  border-radius: 20px;
  background-color: #50ca83;
  color: #fff;
  border: none;
  outline: none;
  font-size: 16px;
  cursor: pointer;
}
</style>