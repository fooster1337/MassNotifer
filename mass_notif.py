import requests
import sys
from colorama import Fore, init
init()
red = Fore.RED
reset = Fore.RESET
green = Fore.GREEN


headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
sess = requests.Session()

team = ''

def zoneh(defacer, url):
    payload = {
        'defacer': defacer,
        'domain1': url,
        'hackmode': '1',
        'reason': '1'
    }
    getCookies = sess.get('http://www.zone-h.org/notify/single', headers=headers)
    req = sess.post('http://www.zone-h.org/notify/single', data=payload, headers=headers).text
    if 'OK' in req:
        print(f'[ZONE-H] {url} => {green}Success{reset}')
    else:
        print(f'[ZONE-H] {url} => {red}Failed{reset}')

def haxorid(defacer, url):
    payload = {
        'defacer': defacer,
        'team': team,
        'vulntype': 1,
        'reason': 1,
        'webtarget': url,
        'submit': 'Notify'
    }
    req = requests.post('https://haxor.id/notify/single', data=payload, headers=headers).text
    if 'domain archived' in req:
        print(f'[HAXOR-ID] {url} => {green}Success{reset}')
    else:
        print(f'[HAXOR-ID] {url} => {red}Failed{reset}')

def zonexsec(defacer, url):
    payload = {
        'defacer': defacer,
        'team': team,
        'poc': 1,
        'reason': 1,
        'urls': url,
        'mirror': 'submit'
    }
    req = requests.post('https://zone-xsec.com/notify', data=payload, headers=headers).text
    if 'Success' in req:
        print(f'[ZONE-XSEC] {url} => {green}Success{reset}')
    else:
        print(f'[ZONE-XSEC] {url} => {red}Failed{reset}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage : python {sys.argv[0]} defacer_name team_name domain_list.txt\nNote : write None if there is no team"); sys.exit()

    defacer = sys.argv[1]
    tim = sys.argv[2]
    dom = sys.argv[3]
    try:
        team = tim if tim != "None" and tim != "none" else None
        a = open(dom, 'r', encoding='utf8').read().splitlines()
        for x in a:
            zoneh(defacer, x)
            haxorid(defacer, x)
            zonexsec(defacer, x)
        print("\nWell, All Done!.\nScript by github.com/fooster1337")
    except FileNotFoundError:
        print("Error: File Not Found."); exit()
    
    
    
