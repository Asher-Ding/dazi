/**
 * @fileOverview 用户
 * @author asherding@icloud.com
 * @version 1.0
 */

import instance from './index'

// [ ] 定义api接口
export const user = {
    getUser(id: number) {
        return instance.get(`/user/${id}`)
    }
}


