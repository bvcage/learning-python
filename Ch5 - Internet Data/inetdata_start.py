# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request

def main():
    web_url = urllib.request.urlopen("http://www.google.com")
    print(web_url.getcode())
    data = web_url.read()
    print(data)

if __name__ == "__main__":
    main()
