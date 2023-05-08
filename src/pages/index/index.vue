<template>
  <div class="index">
    <!-- 导航栏 -->
    <uni-nav-bar :fixed="true" shadow leftText="列表" leftIcon="chatboxes-filled" statusBar="true" @clickLeft="showDrawer">
    </uni-nav-bar>

    <!-- 抽屉 -->
    <uni-drawer ref="showLeft" mode="left" :width="280" :mask-click="ture">
      <scroll-view style="height: 60%;" scroll-y="true">
        <!-- 占位符 -->
        <view style="margin-top: 16%"></view>
        <!-- 个人信息 -->
        <view style="display: flex; align-items: center; padding: 8px; border-bottom: 1px solid gray;">
          <uni-icons type="vip-filled" size="30"></uni-icons>
          <text style="margin-left: 10px; font-size: 18px;">搭子</text>
        </view>
        <uni-list>
          <uni-list :border="true">
            <!-- 显示圆形头像 -->
            <uni-list-chat :avatar-circle="true" title="uni-app"
              avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png" note="您收到一条新的消息"
              time="2020-02-02 20:20"></uni-list-chat>
            <!-- 右侧带角标 -->
            <uni-list-chat title="uni-app" avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png"
              note="您收到一条新的消息" time="2020-02-02 20:20" badge-text="12"></uni-list-chat>
            <!-- 头像显示圆点 -->
            <uni-list-chat title="uni-app" avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png"
              note="您收到一条新的消息" time="2020-02-02 20:20" badge-positon="left" badge-text="dot"></uni-list-chat>
            <!-- 头像显示角标 -->
            <uni-list-chat title="uni-app" avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png"
              note="您收到一条新的消息" time="2020-02-02 20:20" badge-positon="left" badge-text="99"></uni-list-chat>
            <!-- 显示多头像 -->
            <uni-list-chat title="uni-app" :avatar-list="avatarList" note="您收到一条新的消息" time="2020-02-02 20:20"
              badge-positon="left" badge-text="dot"></uni-list-chat>
            <!-- 自定义右侧内容 -->
            <uni-list-chat title="uni-app" :avatar-list="avatarList" note="您收到一条新的消息" time="2020-02-02 20:20"
              badge-positon="left" badge-text="dot">
              <view class="chat-custom-right">
                <text class="chat-custom-text">刚刚</text>
                <!-- 需要使用 uni-icons 请自行引入 -->
                <uni-icons type="star-filled" color="#999" size="18"></uni-icons>
              </view>
            </uni-list-chat>
          </uni-list>
        </uni-list>
        <!-- <view v-for="item in 1" :key="item">可滚动内容 {{ item }}</view> -->
      </scroll-view>
    </uni-drawer>
    <!-- <Navbar></Navbar> -->
    <!-- <Chatpage></Chatpage> -->

    <uni-card title="基础卡片" sub-title="副标题" extra="额外信息" :thumbnail="avatar" @click="onClick">
      <text class="uni-body">这是一个带头像和双标题的基础卡片，此示例展示了一个完整的卡片。</text>
    </uni-card>

    <uni-card title="基础卡片" sub-title="副标题" extra="额外信息" :thumbnail="avatar" @click="onClick">
      <text class="uni-body">这是一个带头像和双标题的基础卡片，此示例展示了一个完整的卡片。</text>
    </uni-card>


    <Bulletin></Bulletin>
    <!-- <SendBox></SendBox> -->
    <Entry></Entry>
  </div>
</template>

<script lang="ts" setup>
// import SendBox from '@/components/sendbox.vue';
// import Navbar from '@/components/navbar.vue';
// import Chatpage from '@/components/chatpage.vue';
import Bulletin from '@/components/card/bulletin.vue';
import Entry from '@/components/entry.vue'
import { getCurrentInstance } from 'vue';

const ctx = getCurrentInstance().ctx
// 这里的ctx等于vue2里面的 this



// TODO: 需要解决导航栏的按键绑定问题
function showDrawer(e) {
  ctx.$refs.showLeft.open()
  // console.log(instance.ctx.$refs.showRight)
  // console.log('showDrawer')
}
function closeDrawer() {
  console.log('closeDrawer')
}

const avatarList = [{
  url: 'https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png'
}, {
  url: 'https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png'
}, {
  url: 'https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png'
}]


// onUnload(() => {
//   // 多端发布时，请进行判断
//   uni.navigateTo({
//     url: '/pages/list/list'
//   })
// })

// onNavigationBarButtonTap(() => {
//   console.log('click')
// })

// onBackPress(() => {
//   console.log(e)
// })


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