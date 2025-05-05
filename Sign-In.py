import aiotieba as tb
import asyncio
import time
import os
import sys

BDUSS = os.getenv("BDUSS")
if not BDUSS:
    print("未设置环境变量 BDUSS , 程序退出")
    sys.exit()
BDUSS_SPLIT=BDUSS.split("#")
user_count=1

async def main(BDUSS):
    async with tb.Client(BDUSS=BDUSS) as client:
        
        user = await client.get_self_info()
        print(f"用户名: {user.user_name}")
        print(f"id：{user.user_id}")
        print(f"uid: {user.tieba_uid}")
        print(f"吧龄: {user.age} 年")
        print(f"昵称: {user.nick_name_new}")
        print(f"portrait: {user.portrait}")
        print("\n")

        print("获取关注贴吧列表并签到...")
        print("\n")
        followed_forums_pages=1
        followed_forums_count=0
        sign_in_success_count=0
        sign_in_already_count=0
        sign_in_failed_count=0
        while True:
            followed_forums=await client.get_follow_forums(id_=user.user_id,pn=followed_forums_pages)
            for x in followed_forums.objs:
                print(f"{x.fname} ({x.fid})",end=" ")
                
                sign_in_result=await client.sign_forum(x.fname)
                
                if not sign_in_result.err:
                    sign_in_success_count+=1
                    print(f"签到成功")
                elif sign_in_result.err.args[0]==160002:
                    sign_in_already_count+=1
                    print(f"已签到")
                else:
                    sign_in_failed_count+=1
                    print(f"签到失败，错误：{sign_in_result.err}")
                print("")

                followed_forums_count+=1
                time.sleep(5)
            followed_forums_pages+=1
            if not followed_forums.has_more:
                break

        print(f"总关注贴吧数: {followed_forums_count} 个")
        print(f"已签到: {sign_in_already_count} 个")
        print(f"签到成功: {sign_in_success_count} 个")
        print(f"签到失败: {sign_in_failed_count} 个")
        print(f"签到率: {(sign_in_success_count+sign_in_already_count)*100/followed_forums_count}%")

for i in BDUSS_SPLIT:
    print(f"\n\n\n使用第 {user_count} 个 BDUSS 进行签到...")
    print(f"获取第 {user_count} 个用户信息...")
    asyncio.run(main(i))
    if user_count<len(BDUSS_SPLIT) and user_count>1:
        print(f"第 {user_count} 个用户签到完成，等待 60 秒...")
        time.sleep(60)
        print("\n\n\n")
 
    user_count+=1

print("所有用户签到完成")
