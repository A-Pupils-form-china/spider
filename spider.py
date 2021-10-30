import json
import os
import time
from urllib import request

data = dict(json.load(open("../整活/data.txt", 'r')))

proxies = {
    'https': 'https://127.0.0.1:10809',
    'http': 'http://127.0.0.1:10809'
}
x = 0
for i in data.items():
    if i[0] == 'album':
        x += 1
        continue
    print("专辑 %s" % i[0].replace(' ', ''))
    os.system("cd origin")
    os.system("mkdir origin\\%s" % i[0].replace(' ', ''))
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/27.0.1453.94 Safari/537.36 '}
    opener = request.build_opener(request.ProxyHandler(proxies))
    request.install_opener(opener)
    for j in i[1].values():
        address = "https://www.azlyrics.com/lyrics/taylorswift/%s.html"
        if j.__contains__("Live Forever"):
            address = "https://www.azlyrics.com/lyrics/zaynmalik/%s.html"
        print("爬取 " + address
              % j.lower().replace(' ', '').replace("'", '').replace(
            '(', '').replace(')', '').replace('.', '').replace("?", '').replace("!", '').replace(',', ''))
        req = request.Request(address
                              % j.lower().replace(' ', '').replace("'", '').replace(
            '(', '').replace(')', '').replace('.', '').replace("?", '').replace("!", '').replace(',', ''), headers=head)
        response = request.urlopen(req)
        with open("origin/%s/%s.html" % (
                i[0].replace(' ', ''),
                j.replace(' ', '') if not j.__contains__('?') else j.replace(' ', '').replace('?', '')),
                  'w',
                  encoding='utf8') as f:
            f.write(response.read().decode("utf8"))
        time.sleep(3)

f = open("test.html", 'w', encoding='utf8')
