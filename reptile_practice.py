#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import time

    
browser = webdriver.Chrome()
browser.get('https://www.weibo.com/login.php')


# 登陆微博
def weibo_login(username, password):
    browser.get('https://www.weibo.com/login.php')
    time.sleep(1)
    username_area = browser.find_element_by_xpath('//*[@id="plc_unlogin_home_main"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input')
    username_area.send_keys(username)
    time.sleep(1)
    password_area = browser.find_element_by_xpath('//*[@id="plc_unlogin_home_main"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input')
    password_area.send_keys(password)
    time.sleep(1)
    login_button = browser.find_element_by_xpath('//*[@id="plc_unlogin_home_main"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[6]/div[1]/a')
    login_button.click()
    time.sleep(1)
    
    
# 加关注
def add_follow(uid):
    browser.get('https://www.weibo.com/u/' + str(uid))
    time.sleep(1)
    follow_button = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a')
    follow_button.click()
    time.sleep(1)
 

# 写评论
def write_comment(weibo, content):
    browser.get(weibo)
    time.sleep(1)
    content_button1 = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[3]/a')
    content_button1.click()
    time.sleep(1)
    content_area = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/textarea')
    content_area.send_keys(content)
    time.sleep(1)
    comment_button2 = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/a')
    comment_button2.click()
    time.sleep(1)

    
# 发微博
def write_weibo(content):
    browser.get('https://www.weibo.com/')
    time.sleep(1)
    content_area = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/textarea')
    content_area.send_keys(content)
    time.sleep(1)
    write_button = browser.find_element_by_xpath('//*[@id="plc_frame"]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/a')
    write_button.click()
    time.sleep(1)


    
if __name__ == '__main__':
    weibo_login()
    add_follow()
    write_comment()
    write_weibo()