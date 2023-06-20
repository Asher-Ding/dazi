<template>
  <div class="drawer"> <!-- 抽屉 -->
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
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'drawer',
  setup(){
    
  }
})
</script>

<style scoped></style>