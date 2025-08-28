# Tieba-Sign-In
基于Python的aiotieba库并使用Github Action实现贴吧每日自动签到

[原项目lumina37/aiotieba](https://github.com/lumina37/aiotieba)快去点star！

### 今日签到状态

[![Tieba Sign-In](https://github.com/q20155211/Tieba-Sign-In/actions/workflows/main.yml/badge.svg)](https://github.com/q20155211/Tieba-Sign-In/actions/workflows/main.yml)

## 使用说明

Fork 本仓库，然后在你 Fork 的仓库的 Settings 中，找到 Secrets and Variables 这一项，添加一个 Secret ，名字为 `BDUSS` ，值为你的 BDUSS，支持同时添加多个BDUSS，多个BDUSS 之间用 `#` 隔开即可

上方签到状态为`[![Tieba Sign-In](https://github.com/q20155211/Tieba-Sign-In/actions/workflows/main.yml/badge.svg)](https://github.com/q20155211/Tieba-Sign-In/actions/workflows/main.yml)`，在不改变项目名称的情况下，将其中的两处`q20155211`改为你的github名称即可显示运行状态，但是显示`passing`不一定代表签到成功，因为是基于python程序是否报错退出来显示`passing`或`failed`，建议看日志确认是否有问题

### 如何获取BDUSS：
在网页中登录[贴吧](https://tieba.baidu.com)，然后按下`F12`打开调试模式，在`cookie`中找到`BDUSS`，并复制其`Value`值

或者登录tieba lite，在 设置 - 账号管理 中复制BDUSS

## 注意
使用BDUSS可以完成一切不需要手机/邮箱验证码的操作，包括发帖/发私信/获取账号上的所有历史发言

BDUSS的过期时间长达数年，一般只能通过退出登录或修改密码使其失效

因此将BDUSS泄露给不受信任的人可能导致长期的账号安全风险和隐私泄露风险

#### *于`2025年8月28日22:54:16`验证可用，若时间过长请自行斟酌风险
