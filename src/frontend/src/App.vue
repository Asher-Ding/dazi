<script setup lang="ts">
import { onLaunch, onShow, onHide } from "@dcloudio/uni-app";
onLaunch(() => {
  console.log("App Launch");
  // uni.login({
  //   provider: "weixin",
  //   onlyAuthorize: true,
  //   success: (res) => {
  //     console.log(res);
  //     const code = res.code // 临时登录凭证
  //     console.log("[CODE] " + code)
  //   },
  //   fail:(fail)=>{
  //     console.log("[FAIL] " +  fail)
  //   },
  // });
  // https://uniapp.dcloud.net.cn/api/plugins/login.html#getuserinfo
  // uni.getUserInfo({
  //   success(result) {
  //     console.log(result);
  //     const rawData = result.rawData // 不包括敏感信息的原始数据字符串，用于计算签名。
      
  //   },
  // });
});
onShow(() => {
  console.log("App Show");
});
onHide(() => {
  console.log("App Hide");
});
</script>
<style></style>
