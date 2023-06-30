<template>
  <div class="message">
    <scroll-view class="" scroll-x="false" scroll-y="false" upper-threshold="50" lower-threshold="50" scroll-top="0"
      scroll-left="0" scroll-into-view="" scroll-with-animation="false" enable-back-to-top="false" bindscrolltoupper=""
      bindscrolltolower="" bindscroll="">
      <uni-card :title="message.title" :sub-title="message.username" :extra="message.extra" :thumbnail="message.avatar">
        <text class="uni-body">{{ message.content }}</text>
      </uni-card>
      <!-- Comments start-->
      <uni-card v-for="(item, index) in message.comments" :key="index" :title="item.title" :sub-title="item.username"
        :extra="item.extra" :thumbnail="item.avatar" @click="msgDetail(item.message_id)">
        <text class="uni-body">{{ item.content }}</text>
      </uni-card>
    </scroll-view>
    <Entry></Entry>
  </div>
</template>

<script lang="ts">
import Entry from '@/components/entry.vue'

export default {
  data() {
    return {
      message: {},
      comments: []
    }
  },
  components: {
    Entry
  },
  onLoad: function (option: any) {
    console.log('message onLoad')
    console.log(option.id)

    const baseURL = process.env.NODE_ENV === 'production' ? 'https://api.example.com' : 'https://d391b1a3-5728-4973-97d3-9ced6a5b20cd.mock.pstmn.io';

    uni.request({ // 获取信息列表
      url: baseURL + `/message/detail?id=` + option.id, //仅为示例，并非真实接口地址。
      method: 'GET',
      success: (res) => {
        this.message = res.data
        console.log(this.message);
        this.comments = this.message.comments
        console.log(this.message.comments)
      }
    })
  },

  methods: {

  }
}

</script>

<style scoped></style>