<template>
  <div class="chatpage">
    <div class="messages-list">
      <div v-for="(message, index) in messages" :key="index" class="message">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: "chatpage",
  data() {
    return {
      messages: ['Hello', 'How are you?', 'I am fine, thanks.', 'What is your name?'] // Store chat messages here
    }
  }
})
</script>

<style scoped>
.messages-list {
  display: block;
}
</style>