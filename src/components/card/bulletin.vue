<!-- 公告卡片，所有用户可以进行留言 -->
<template>
  <div class="bulletin" @longpress="showEmojiSelector">
    <div class="sender">{{ sender }}</div>
    <div class="content">{{ content }}</div>
    <div class="time">{{ time }}</div>
    <div v-show="showSelector" class="emoji-selector">
      <img src="/static/like.png" alt="like" @click="onEmojiSelect('like')" />
      <img src="/static/dislike.png" @click="onEmojiSelect('dislike')" />
      <img src="/static/good.png" @click="onEmojiSelect('good')" />
      <img src="/static/bad.png" @click="onEmojiSelect('bad')" />
    </div>
    <button v-if="showButton" @click="showMessageForm">Leave a message {{ showButton }}</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: "bulletin",
  props: {},
  data() {
    return {
      showSelector: false,
      showButton: true,
      sender: 'John Doe',
      content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      time: '2021-09-01 10:30',
      showForm: false,
      message: ''
    }

  },
  computed: {
    showButton() {
      const route = this.$route
      return this.$route
    }
  },
  methods: {
    showEmojiSelector() {
      console.log('show emoji selector')
      this.showSelector = true
    },
    onEmojiSelect(emoji) {
      console.log(`Selected Emoji: ${emoji}`);
      // TODO: send emoji to server or update local state
      this.showSelector = false; // hide selector after selecting emoji
    },
    showMessageForm() {
      uni.navigateTo({
        url: '/pages/messages'
      })
      this.showButton = false
    },
  },
  watch: {},

  // 组件周期函数--监听组件挂载完毕
  mounted() {
    console.log("this.route")
    console.log(this.$mp.page.route)
  },
  // 组件周期函数--监听组件数据更新之前
  beforeUpdate() { },
  // 组件周期函数--监听组件数据更新之后
  updated() { },
  // 组件周期函数--监听组件激活(显示)
  activated() {

  },
  // 组件周期函数--监听组件停用(隐藏)
  deactivated() { },
  // 组件周期函数--监听组件销毁之前
  beforeDestroy() {
  },
}) 
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
}

.sender {
  font-weight: bold;
  margin-bottom: 5px;
}

.content {
  margin-bottom: 10px;
}

.time {
  color: #999;
  margin-bottom: 10px;
}


.emoji-selector {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 240px;
  height: 80px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
}

.emoji-selector img {
  width: 40px;
  height: 40px;
  cursor: pointer;
  transition: all 200ms ease-in-out;
}

.emoji-selector img:hover {
  transform: scale(1.2);
}
</style>