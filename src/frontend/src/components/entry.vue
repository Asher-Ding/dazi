<!-- 
  https://github.com/BoBoooooo/Tyloo-Chat/blob/main/client/src/components/Entry.vue
 -->
<template>
  <div class="entry">
    <uni-icons type="mic" size="30"></uni-icons>
    <input class="uni-input" focus placeholder="" confirm-type="send" />
    <uni-icons type="fire-filled" size="30"></uni-icons>
    <uni-icons type="plus" size="30"></uni-icons>



    <!-- <div class="message-tool">
      <a-popover placement="topLeft" trigger="click" class="message-popver">
        <template slot="content">
          <emoji></emoji>
        </template>
        <div class="message-tool-item">
          <div class="messagte-tool-icon">😃</div>

        </div>
      </a-popover>
    </div> -->

    <!-- <a-input v-if="mobile" autocomplete="off" type="text" autoFocus placeholder="say hello..." v-model="text" ref="input"
      style="color: #000" @pressEnter="throttle(preSendMessage)" />
    <a-textarea v-else autocomplete="off" v-model="text" ref="input" autoFocus style="color: #000" @pressEnter="(e) => {
      // 此处拦截enter后光标换行
      e.preventDefault();
      throttle(preSendMessage);
    }
      " /> -->
    <!-- <img class="message-input-button" v-if="mobile" @click="throttle(preSendMessage)" src="~@/assets/send.png" alt="" /> -->
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
export default defineComponent({
  name: 'entry',
  setup() {
    const value = ref('')
    function input(e) {
      console.log('请输入内容', e)
    }
  }

})
</script>
<style lang="scss" scoped>
// @import '@/styles/theme';

.entry {
  display: flex;
  align-content: center;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4em;
  background-color: #efefef;
  padding: 10px;
  box-shadow: 0 -1px 2px rgba(0, 0, 0, 0.15);

  input {
    width: 64%;
    height: 2.4em;
    margin: 0 6px 0 6px;
    padding: 0 6px 0 6px;
    border-radius: 4px;
    background: #fff;
    display: block;

  }



  // textarea {
  //   border-left: none !important;
  //   border-top-left-radius: 0;
  //   border-top-right-radius: 0;
  //   border-bottom-left-radius: 0;
  // }

  // .message-input-button {
  //   width: 30px;
  //   cursor: pointer;
  //   position: absolute;
  //   right: 10px;
  //   top: 4px;
  // }
}

//输入框样式
// .ant-input {
//   padding: 50px 10px 0 20px !important;
//   height: 180px;
//   border-top: 1px solid #d6d6d6;
//   // background: $message-bg-color;
//   border-left: none;
//   border-right: none;
//   border-bottom: none;
//   border-radius: 0;

//   &:focus {
//     box-shadow: none !important;
//   }
// }

// 移动端样式
// @media screen and (max-width: 768px) {
//   .ant-input {
//     padding: 0 50px 0 35px !important;
//     height: 40px;
//   }

//   .message-tool {
//     right: unset !important;
//     padding: 0 0 0 10px !important;

//     .message-tool-item {
//       .anticon {
//         margin-right: 0 !important;
//       }
//     }
//   }
// }

// // 消息工具样式
// .message-tool {
//   position: absolute;
//   left: 0;
//   right: 0;
//   display: flex;
//   align-items: center;
//   height: 50px;
//   line-height: 42px;
//   font-size: 22px;
//   padding: 0 20px;
//   z-index: 99;
//   color: #828282;

//   .message-tool-item {
//     .anticon {
//       margin-right: 25px;
//     }
//   }
// }
</style>