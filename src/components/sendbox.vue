<template>
  <div class="sendbox">
    <div class="input-box">
      <div class="input">
        <input type="text" placeholder="输入消息...">
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
import Vue from 'vue';
export default Vue.extend({
  name: "sendbox",
  props: {},
  data() {
    return {}
  },
  computed: {},
  methods: {
    sendMessage() {
      if (this.newMessage) {
        this.messages.push(this.newMessage)
        this.newMessage = '' // Clear input box
      }
    }
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