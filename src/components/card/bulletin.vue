<!-- 公告卡片，所有用户可以进行留言 -->
<template>
  <div class="bulletin" @longpress="showEmojiSelector">
    <uni-card title="基础卡片" sub-title="副标题" extra="额外信息" :thumbnail="avatar" @click="showEmojiSelector">
      <text class="uni-body">这是一个带头像和双标题的基础卡片，此示例展示了一个完整的卡片。</text>
      <template v-slot:actions>
        <view class="card-actions">
          <div v-show="showSelector" class="emoji-selector">
            <uni-icons type="star-filled" size="30"></uni-icons>
            <!-- <img src="/static/like.png" alt="like" @click="onEmojiSelect('like')" />
            <img src="/static/dislike.png" alt="dislike" @click="onEmojiSelect('dislike')" />
            <img src="/static/good.png" alt="good" @click="onEmojiSelect('good')" />
            <img src="/static/bad.png" alt="bad" @click="onEmojiSelect('bad')" /> -->
          </div>
          <button type="default" plain="true" @click="showMessageForm">留言</button>
        </view>
      </template>

    </uni-card>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: "Bulletin",
  props: {},
  data() {
    return {
      showSelector: false,
      showFormButton: true,
      sender: 'John Doe',
      content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      time: '2021-09-01 10:30',
    }
  },
  computed: {

  },
  methods: {
    showEmojiSelector() {
      console.log('show emoji selector');
      this.showSelector = true;
    },
    onEmojiSelect(emoji: string) {
      console.log(`Selected Emoji: ${emoji}`);
      // TODO: send emoji to server or update local state
      this.showSelector = false; // hide selector after selecting emoji
    },
    showMessageForm() {
      uni.navigateTo({
        url: '/pages/messages'
      })
    },
  }
})
</script>

<style lang="scss" scoped>
.emoji-selector {
  width: 100%;
  height: 4em;
  // position: absolute;
  // display: flex;
  // align-items: center;
  // justify-content: space-between;
  // width: 240px;
  // height: 80px;
  // background-color: #fff;
  // border: 1px solid #ccc;
  // border-radius: 5px;
  // padding: 5px;
  // box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
  // bottom: calc(100% + 10px);
  // left: 50%;
  // transform: translateX(-50%);
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