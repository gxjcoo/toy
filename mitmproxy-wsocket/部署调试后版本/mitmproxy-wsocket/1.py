from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--no-sandbox")  # 可选项，解决部分环境的问题
chrome_options.add_argument("--disable-dev-shm-usage")  # 可选项，解决部分环境的问题
chrome_driver_path = "/usr/local/bin/chromedriver"  # ChromeDriver 的路径
service = Service(chrome_driver_path)

# 启动 Chrome 浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)

# 访问网页示例
driver.get("https://www.baidu.com")

# 打印页面标题
print("Page title:", driver.title)

# 关闭浏览器
driver.quit()

