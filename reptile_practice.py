'''
通过selenium完成微博的自动关注、评论和发微博功能，方案如下：
加关注：1.通过微博域名和用户ID获取想要关注用户的个人界面  2.获取关注按键位置并点击
写评论：1.获取想要评论的微博的界面  2.获取评论按键位置并点击  3.获取评论栏位置并输入内容  4.获取提交按键位置并点击
发微博：1.获取个人界面  2.获取微博栏位置并输入内容  3.获取发布按键位置并点击
'''


#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import time

if __name__ == '__main__':
    weibo_login()
    add_follow()
    unfollow()
    write_comment()
    write_weibo()
    
browser = webdriver.Chrome()
browser.get('https://www.weibo.com/login.php')

# 验证码n次尝试登录函数
def verify_login(n):
    for i in range(n):
        verification_area = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input')
        verification_area.send_keys(input("输入验证码： "))
        time.sleep(3)
        login_button = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span')
        login_button.click()
    

# 登陆微博
def weibo_login(username, password, n):
    browser.get('https://www.weibo.com/login.php')
    time.sleep(1)
    # 输入用户名
    username_area = browser.find_element_by_xpath('//*[@id="plc_unlogin_home_main"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input')
    username_area.send_keys(username)
    time.sleep(1)
    # 输入密码
    password_area = browser.find_element_by_xpath('//*[@id="plc_unlogin_home_main"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input')
    password_area.send_keys(password)
    time.sleep(1)
    verify_login(n)
    
    
# 加关注
def add_follow(uid):
    browser.get('https://m.weibo.com/u/' + str(uid))
    time.sleep(1)
    follow_button = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a')
    follow_button.click()
    time.sleep(1)

#取消关注
def unfollow(uid):
    browser.get('https://www.weibo.com/u/' + str(uid))
    time.sleep(1)
    follow_button = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a')
    follow_button.click()
    time.sleep(3)
    unfollow_button = browser.find_element_by_xpath('//div[@class="layer_menu_list_b "]/div[1]/div[1]/ul[1]/li[4]/a')
    unfollow_button.click()
    time.sleep(1)

# 写评论
def write_comment(uid, content):
    browser.get('https://www.weibo.com/u/' + str(uid))
    time.sleep(1)
    # 点击评论按钮
    content_button1 = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/a]')
    content_button1.click()
    time.sleep(1)
    # 输入评论内容
    content_area = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/textarea')
    content_area.send_keys(content)
    time.sleep(1)
    # 点击提交按钮
    comment_button = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/a')
    comment_button2.click()
    time.sleep(1)

    
# 发微博
def write_weibo(content):
    browser.get('https://weibo.com')
    time.sleep(1)
    # 输入微博内容
    content_area = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/textarea')
    content_area.send_keys(content)
    time.sleep(1)
    # 点击提交按钮
    write_button = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/a')
    write_button.click()
    time.sleep(1)

    
if __name__ == '__main__':
    weibo_login('297088546@qq.com', 'gyxlzy03271230', 3)
    browser.implicitly_wait(10)
    add_follow('5746403289')
    browser.implicitly_wait(5)
    unfollow('5746403289')
    browser.implicitly_wait(5)
    write_comment('5746403289', 'haha')
    browser.implicitly_wait(5)
    write_weibo('haha')
