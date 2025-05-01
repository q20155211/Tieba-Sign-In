# Tieba-Sign-In
基于Python的aiotieba库并使用Github Action实现贴吧每日自动签到

### 今日签到状态

![Baidu Tieba Auto Sign](https://github.com/gwtak/TieBaSign/workflows/Baidu%20Tieba%20Auto%20Sign/badge.svg)

## 使用说明

Fork 本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加一个库秘密变量。其中 `BDUSS` 存放你的 BDUSS。支持同时添加多个帐户，BDUSS 之间用 `#` 隔开即可。
### 如何获取BDUSS：
  在网页中登录上贴吧，然后按下`F12`打开调试模式，在`cookie`中找到`BDUSS`，并复制其`Value`值。
or登录tieba lite，在 设置 - 账号管理 中复制BDUSS

#### 注意
使用BDUSS可以完成一切不需要手机/邮箱验证码的操作，包括发帖/发私信/获取账号上的所有历史发言
BDUSS的过期时间长达数年，一般只能通过退出登录或修改密码使其失效
因此将BDUSS泄露给不受信任的人可能导致长期的账号安全风险和隐私泄露风险