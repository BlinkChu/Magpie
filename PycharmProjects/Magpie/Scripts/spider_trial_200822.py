import requests
from lxml import etree
from lxml import html
import lxml
import json
from html.parser import HTMLParser

# req_test = request.Request('https://zhuanlan.zhihu.com/p/130454587')

# html = request.urlopen(req_test)

# title = etree.HTML(html).xpath('//*[@id="root"]/div/main/div/article')[0]
# title_en = title.encode('utf-8')

page = requests.get('https://product.suning.com/0000000000/617763437.html?srcpoint=utf-8_homepagev8_126606438732_prod03&safp=d488778a.homepagev8.126606438732.3&safc=prd.0.0&safpn=10001').content.decode('utf-8')
doc = lxml.html.document_fromstring(page)
res = doc.replace('\n','')
content = res.xpath('/html/body/script[4]/text()')
print(content)
