<template>
  <div class="index">
    <!-- 导航栏 -->
    <uni-nav-bar :fixed="true" shadow leftText="列表" leftIcon="chatboxes-filled" statusBar="true" @click="showDrawer">
    </uni-nav-bar>
    <!-- 抽屉 -->
    <uni-drawer ref="showRight" mode="right" :mask-click="false">
      <scroll-view style="height: 100%;" scroll-y="true">
        <button @click="closeDrawer">关闭Drawer</button>
        <view v-for="item in 60" :key="item">可滚动内容 {{ item }}</view>
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

// TODO: 需要解决导航栏的按键绑定问题
function showDrawer() {
  // .$refs.showRight.open();
  console.log('showDrawer')
}
function closeDrawer() {
  console.log('closeDrawer')
}


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