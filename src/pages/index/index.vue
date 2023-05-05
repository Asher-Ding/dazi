<template>
  <div class="index">
    <Navbar></Navbar>
    <Chatpage></Chatpage>
    <!-- <Bulletin></Bulletin> -->
    <SendBox></SendBox>
  </div>
</template>

<script setup lang="ts" >
import SendBox from '@/components/sendbox.vue';
import Navbar from '@/components/navbar.vue';
import Chatpage from '@/components/chatpage.vue';

</script>

<style lang="less" scoped></style>