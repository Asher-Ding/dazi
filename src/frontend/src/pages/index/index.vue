<template>
  <div class="index">
    <!-- 导航栏，点击导航后，左侧弹出抽屉 -->
    <uni-nav-bar :fixed="true" shadow :leftText="nickName" :leftIcon="avatar" statusBar="true" @clickLeft="showDrawer">
    </uni-nav-bar>

    <!-- 左侧抽屉菜单 -->
    <uni-drawer ref="showLeft" mode="left" :width="280" :mask-click="ture">
      <scroll-view style="height: 60%;" scroll-y="true">
        <!-- 占位符 -->
        <view style="margin-top: 16%"></view>
        <!-- 个人信息 -->
        <view style="display: flex; align-items: center; padding: 8px; border-bottom: 1px solid gray;">
          <!-- 图标 -->
          <uni-icons type="chatboxes" size="20"></uni-icons>
          <!-- 标题内容 -->
          <text style="margin-left: 10px; font-size: 14px;">我的搭子</text>
        </view>
        <!-- 搭子列表 -->
        <!-- TODO 从服务端获取对话列表 -->
        <uni-list :border="true">
          <!-- 显示圆形头像 -->
          <!-- <uni-list-chat :avatar-circle="true" title="uni-app"
              avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png" note="您收到一条新的消息"
              time="2020-02-02 20:20"></uni-list-chat> -->
          <!-- 右侧带角标 -->
          <!-- <uni-list-chat title="uni-app" avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png"
              note="您收到一条新的消息" time="2020-02-02 20:20" badge-text="12"></uni-list-chat> -->
          <!-- 头像显示圆点 -->
          <!-- <uni-list-chat title="uni-app" avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png"
              note="您收到一条新的消息" time="2020-02-02 20:20" badge-positon="left" badge-text="dot"></uni-list-chat> -->
          <!-- 头像显示角标 -->
          <!-- <uni-list-chat title="uni-app" avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png"
              note="您收到一条新的消息" time="2020-02-02 20:20" badge-positon="left" badge-text="99"></uni-list-chat> -->
          <!-- 显示多头像 -->
          <!-- <uni-list-chat title="uni-app" :avatar-list="avatarList" note="您收到一条新的消息" time="2020-02-02 20:20"
              badge-positon="left" badge-text="dot"></uni-list-chat> -->
          <!-- 自定义右侧内容 -->
          <!-- <uni-list-chat title="uni-app" :avatar-list="avatarList" note="您收到一条新的消息" time="2020-02-02 20:20"
              badge-positon="left" badge-text="dot">
              <view class="chat-custom-right">
                <text class="chat-custom-text">刚刚</text>
                <uni-icons type="star-filled" color="#999" size="18"></uni-icons>
              </view>
            </uni-list-chat> -->
        </uni-list>
        <!-- <view v-for="item in 1" :key="item">可滚动内容 {{ item }}</view> -->
      </scroll-view>
    </uni-drawer>

    <!-- 对话内容 -->
    <!-- 从服务端获取本页数据 -->
    <scroll-view class="" scroll-x="false" scroll-y="false" upper-threshold="50" lower-threshold="50" scroll-top="0"
      scroll-left="0" scroll-into-view="" scroll-with-animation="false" enable-back-to-top="false" bindscrolltoupper=""
      bindscrolltolower="" bindscroll="">
      <!-- [ ]从服务器获取聊天数据
                1. 基于LBS定位信息获取，所以需要上传位置信息
      -->
      <uni-card title="基础卡片" sub-title="副标题" extra="额外信息" :thumbnail="avatar" @click="onClick">
        <text class="uni-body">这是一个带头像和双标题的基础卡片，此示例展示了一个完整的卡片。</text>
      </uni-card>

      <uni-card title="基础卡片" sub-title="副标题" extra="额外信息" :thumbnail="avatar" @click="onClick">
        <text class="uni-body">这是一个带头像和双标题的基础卡片，此示例展示了一个完整的卡片。</text>
      </uni-card>

      <Bulletin></Bulletin>

    </scroll-view>
    <Entry></Entry>
  </div>
</template>

<script lang="ts" setup>
import Bulletin from '@/components/card/bulletin.vue';
import Entry from '@/components/entry.vue'
// Vue3 不再支持this的用法
import { getCurrentInstance, onBeforeMount, ref } from 'vue';

// import { login } from '@/api/user'
import { message } from '@/api/index'

// 这里的ctx等于vue2里面的 this
// BUG
const ctx = getCurrentInstance().ctx
const nickName = ref('')
const avatar = ref('')
const messageList = ref([])

// 获取当前的位置信息 https://uniapp.dcloud.net.cn/api/location/location.html
uni.getLocation({
  type: 'wgs84',
  success: (res) => {
    const pos = String(res)
    message.getMessageList('pos').then((res: any) => {
      console.log(res)
      messageList.value = res.data
    })
  },
})


uni.login({
  provider: "weixin",
  onlyAuthorize: true,
  success: (res) => {
    console.log(res);
    const code = res.code // 临时登录凭证
    console.log("[CODE] " + code)
  },
  fail: (fail) => {
    console.log("[FAIL] " + fail)
  },
});

// https://uniapp.dcloud.net.cn/api/plugins/login.html#getuserinfo
uni.getUserInfo({
  success(result) {
    console.log(result);
    nickName.value = result.userInfo.nickName // 用户昵称
    avatar.value = result.userInfo.avatarUrl // 用户头像图片 url
    // console.log('nickname: ' + nickName.value);
  },
});

// [ ] 上传服务器当前位置信息，并拉取附近的聊天记录 



// [x] 解决导航栏的按键绑定问题
function showDrawer() {
  // 打开抽屉
  ctx.$refs.showLeft.open()
}

// [ ] 测试数据
// const avatarList = [{
//   url: 'https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png'
// }, {
//   url: 'https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png'
// }, {
//   url: 'https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png'
// }]


</script>

<style lang="scss" scoped>
.status_bar {
  height: var(--status-bar-height);
  width: 100%;
  background-color: #F8F8F8;
}

.top_view {
  height: var(--status-bar-height);
  width: 100%;
  position: fixed;
  background-color: #F8F8F8;
  top: 0;
  z-index: 999;
}
</style>