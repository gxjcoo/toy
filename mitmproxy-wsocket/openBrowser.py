import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 设置代理服务器
proxy = "127.0.0.1:8080"
# 设置ChromeDriver的可执行文件路径
chrome_driver_path = "D:\chrome_headless\chromedriver.exe"
# # 设置ChromeDriver的可执行文件路径
# chrome_driver_path = "/usr/local/bin/chromedriver"  # ChromeDriver 的路径
# 配置Chrome选项
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # 启动无头模式
chrome_options.add_argument("--no-sandbox")  # 可选项，解决部分环境的问题
chrome_options.add_argument("--disable-dev-shm-usage")  # 可选项，解决部分环境的问题
chrome_options.add_argument("--ignore-certificate-errors")  # 忽略证书错误
chrome_options.add_argument(f'--proxy-server=http://{proxy}')

# 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

def openBrowser():
      print('打开浏览器')
    # 访问指定的URL
      driver.get("http://djjy8.com/")
    
    # 打印页面标题
      print("Page title:", driver.title)

    # 打印页面内容
      # print(driver.page_source)

    # 让浏览器一直存在
      print("Press Ctrl+C to exit and close the browser.")
      while True:
        time.sleep(1)

openBrowser()