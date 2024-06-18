import mitmproxy.http
from mitmproxy import ctx

class Counter:
  
    def request(self, flow: mitmproxy.http.HTTPFlow):

        ctx.log.info('白色标准输出:{}'.format(flow.request.url))
        # ctx.log.warn('黄色警告输出:{}'.format(flow.request.url))
        # ctx.log.error('红色异常输出:{}'.format(flow.request.url))

    def response(self, flow: mitmproxy.http.HTTPFlow):

        # 如果请求的url包含"wordEveryDay/list",则将返回的数据保存在
        if "wordEveryDay/list" in flow.request.url:
            with open("word_every_day.json", "a",encoding="utf-8") as f:
                f.write(flow.response.text)
                f.write("\n")
        
addons = [
    Counter()
]
# 1、运行命令
# mitmweb -s addons.py
# 2、打开手机wifi代理，设置代理ip和端口
# 3、打开app，进行操作
# 4、查看抓取的数据
