<!-- 菜单。用户可以在菜单上选择想要匹配的对象 -->
<!-- Demo：
  某某小姐：
    我们根据你的兴趣爱好，通过随机森林算法，为你推荐了这些人：
      <link>某某先生</link>
      <link>某某先生</link>
      <link>某某先生</link>
    你可以点击他们的名字，查看他们的详细信息；如果你对他们感兴趣，可以点击右上角的红心，将他们加入你的搭子列表。
    # 然后用户就可以在查看到她刚才新加的搭子，如果不喜欢，可以点击右上角的叉叉，将他们从搭子列表中移除。
    # 不使用文件夹对聊天对象进行分类，而是使用标签对聊天对象进行分类，这样可以让用户更加灵活的对聊天对象进行分类。
    # 可以根据标签对聊天对象进行筛选，比如：我想看看我的搭子列表中的所有女性，或者我想看看我的搭子列表中的所有男性。
 -->
<template>
  <div class="menu">menu</div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: "menu",
  props: {},
  data() {
    return {}
  },
  computed: {},
  methods: {},
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

<style scoped></style>