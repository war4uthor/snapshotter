#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import argparse
from socket import gethostbyname, gaierror

def enum_urls(urls):
    print("(+) Enumerating URLs")
    urls = open(urls, 'r+')
    for url in urls:
        url = url.strip()
        if check_live(url):
            take_screenshot(url)

def check_live(url):
    try:
        r = requests.get(url='https://{}'.format(url), timeout=30)
        if r.status_code == 200:
            return True
        elif r.status_code == 301:
            print("Redirected to HTTPS")
    #Page not served over HTTPS
    except requests.ConnectionError as e:
        url = 'http://{}'.format(url)
        try:
            r = requests.get(url=url, timeout=30)
            if r.status_code == 200:
                return True
        except:
            return False
    except:
        print("(-) EXITING")
        return False

def take_screenshot(url):
    print("(+) Taking snapshot of {}".format(url))
    options = Options()
    options.headless=True
    driver = webdriver.Firefox(options=options)
    try:
        driver.get('https://{}'.format(url))
    except WebDriverException as ex:
        driver.get('http://{}'.format(url))
    except:
        driver.quit()
        return
    
    try:
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'), S('Height'))
        driver.find_element_by_tag_name('body').screenshot('snapshots/{}.png'.format(url))
        driver.quit()
    except:
        driver.quit()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', help='File containing list of URLs to enumerate', required=True)
    args = parser.parse_args()

    urls = args.urls
    enum_urls(urls)

    print("(+) Complete!")

if __name__ == "__main__":
    main()
