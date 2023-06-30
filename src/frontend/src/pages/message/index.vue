<template>
  <div class="message">message</div>
</template>

<script lang="ts">

export default {
  onLoad: function (option: any) {
    console.log('message onLoad')
    console.log(option.id)

    const baseURL = process.env.NODE_ENV === 'production' ? 'https://api.example.com' : 'https://d391b1a3-5728-4973-97d3-9ced6a5b20cd.mock.pstmn.io';

    uni.request({ // 获取信息列表
      url: baseURL + `/message/detail?id=` + option.id, //仅为示例，并非真实接口地址。
      method: 'GET',
      success: (res) => {
        const data: any = res.data
        console.log(data);
      }
    })
  },

  methods: {

  }
}

</script>

<style scoped></style>