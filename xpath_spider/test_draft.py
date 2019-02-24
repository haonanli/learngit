import numpy as np
import preparation_spyder as gf
import wangyi_spider as sw

# ip_list=np.load("ip.npy")
# print(ip_list)
# ip=np.random.choice(ip_list)
# print(ip)
# us_ag=gf.get_user_agent()
# print(type(us_ag))
# print(us_ag)
# proxies={"http":np.random.choice(ip_list)}
# print(proxies)

#通过phantomjs来传送信息，如输入用户名、密码、点击登录按钮实现模拟登陆
driver =webdriver.PhantomJS(executable_path="phantomjs.exe")
driver.get("https://www.shanbay.com/accounts/login/")
elem_user = driver.find_element_by_xpath('//*[@id="id_username"]')
elem_user.send_keys('用户名')
elem_pwd = driver.find_element_by_xpath('//*[@id="id_password"]')
elem_pwd.send_keys('密码')
elem_sub = driver.find_element_by_xpath('//*[@id="loginform"]/div[3]/button')
elem_sub.click()




# a=gf.main()
# print(a)

# user_agent=gf.get_user_agent()
# print(user_agent)

# a=[1,2]
# np.save("a.npy",a)
# b=np.load("a.npy")
# print(b)