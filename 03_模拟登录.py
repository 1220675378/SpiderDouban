import requests
from fake_useragent import UserAgent

my_cookie = 'll="118250"; bid=ZhIlK6eFmDs; _pk_id.100001.8cb4=f6fe3016096c2911.1665592546.; _pk_ref.100001.8cb4=["",' \
            '"",1684222261,"https://accounts.douban.com/"]; _pk_ses.100001.8cb4=1; ap_v=0,6.0; push_noty_num=0; ' \
            'push_doumail_num=0; __utma=30149280.1533177260.1683467829.1683767114.1684222261.4; __utmc=30149280; ' \
            '__utmz=30149280.1684222261.4.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ' \
            '__utmv=30149280.27070; __yadk_uid=1XdOF5DT60vSejkEWcUaFS5vwu3oAFZW; ' \
            '__gads=ID=d47ec574dca34dbb-22af16eca7df006c:T=1684222267:RT=1684222267:S' \
            '=ALNI_MZij2cUN5oX8B9zLhsvxRMRD9XGnw; ' \
            '__gpi=UID=00000c06ed268407:T=1684222267:RT=1684222267:S=ALNI_MYjR94Ya3MIkTqf0NgbRNjNmDfqDQ; ' \
            'dbcl2="270709356:1ZCfzssk+mA"; ck=qStT; __utmt=1; __utmb=30149280.11.10.1684222261'
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'cookie': my_cookie
}
url = 'https://www.douban.com/people/270709356/?_i=4223564ZhIlK6e'
data = requests.get(url, headers)
print(data.status_code)
print(data.request.headers)
print(data.text)
