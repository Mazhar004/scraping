from bs4 import BeautifulSoup as bbs
import requests as rq
import os


def generate(filename):
    proxy_root = os.path.split(os.path.abspath(__file__))[0]
    res = rq.get('https://spys.me/proxy.txt')

    proxies = []
    for i in res.text.split('\n\n')[-1].split('\r')[0].split('\n'):
        try:
            ip, val, _ = i.split()
            val = val.split('-')[-1]
            if 'S' in val:
                proxies.append('https://'+ip)
            else:
                proxies.append('http://'+ip)
        except:
            pass
    with open(proxy_root+'/'+filename, 'w') as fh:
        fh.write('\n'.join(proxies))
