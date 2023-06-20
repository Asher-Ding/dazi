/**
 * @fileOverview 基础文件，对axios进行封装，添加拦截器等
 * @author asherding@icloud.com
 * @version 1.0
 */

const baseURL = process.env.NODE_ENV === 'production' ? 'https://api.example.com' : 'http://localhost:3000';

// [ ] 封装拦截器API接口
const instance = uni.create({
    baseURL,
    timeout: 1000, //set timeout
})

function errorHandler(error: any) {
    if (error.response) {
        console.error('error.response', error.response)
    } else if (error.request) {
        console.error('error.request', error.request)
    }
    return Promise.reject(error)
}
// request interceptor
instance.interceptors.request.use(config => {
    // do something before request is sent
    return config
}, errorHandler)

// response interceptor
instance.interceptors.response.use(response => {
    // do something with response data
    return response
}, errorHandler)

export default instance