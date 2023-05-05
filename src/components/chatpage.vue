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
import Vue from 'vue';
export default Vue.extend({
  name: "chatpage",
  props: {},
  data() {
    return {
      messages: ['Hello', 'How are you?', 'I am fine, thanks.', 'What is your name?'] // Store chat messages here
    }
  },
  computed: {},
  methods: {

  },
  watch: {},

  // 组件周期函数--监听组件挂载完毕
  mounted() { },
  // 组件周期函数--监听组件数据更新之前
  beforeUpdate() { },
  // 组件周期函数--监听组件数据更新之后
  updated() { },
  // 组件周期函数--监听组件激活(显示)
  activated() { },
  // 组件周期函数--监听组件停用(隐藏)
  deactivated() { },
  // 组件周期函数--监听组件销毁之前
  beforeDestroy() { },
}) 
</script>

<style scoped>
.messages-list {
  display: block;
}
</style>