/**
 * @fileOverview API接口
 * @author asherding@icloud.com
 * @version 1.0
 */

// import instance from './index'
const baseURL = process.env.NODE_ENV === 'production' ? 'https://api.example.com' : 'https://d391b1a3-5728-4973-97d3-9ced6a5b20cd.mock.pstmn.io';

// [ ] 定义api接口
export const message = {
    getMessageList(position: string) {
        uni.request({
            url: baseURL + `/message?location=${position}`, //仅为示例，并非真实接口地址。
            method: 'GET' ,
            success: (res) => {
                // console.log(res.data);
                // 打印： {code:1,...}
                return res.data
            }
        })
    }
}