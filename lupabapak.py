import requests as req
import time as tm
import sys
from bs4 import BeautifulSoup as bs
from colorama import init,Fore
init()

def curl(url,query):
	return req.get(url+query)
def ani():
	for i in range(10):
		sys.stdout.write(" -")
		tm.sleep(0.5)
	print(" >")

print (" ##########################")
print (" #                        #")
print (" #      Insomniac.ID      #")
print (" #  https://insomniac.id  #")
print (" #                        #")
print (" ##########################")

print (" Lupabapak Scraper")

uri = "Bukalapak"
url = "https://www.bukalapak.com/products?utf8=✓&source=navbar&from=omnisearch&search_source=omnisearch_organic&from_keyword_history=false&search%5Bkeywords%5D="
query = input(" Search keyword : ")
print(" Searching "+ query + " on " + uri)
try:
	get = curl(url,query)
	tm.sleep(0.5)
	sop = bs(get.text, 'html.parser')
	go = sop.find_all("article", attrs={'class':'product-display'})
	print(Fore.YELLOW +"",len(go),"Items Found")
	ani()
	for p in go:
		name = p.find("a", attrs={'class':'product__name line-clamp--2 js-tracker-product-link qa-list'})
		seller = p.find("h5", attrs={'class':'user__name'})
		sell = seller.find("a",href=True)
		price = p.find("span", attrs={'class':'amount positive'})
		# img = p.find("source").get('data-src')
		print(Fore.GREEN + "[+] " +Fore.YELLOW + name.text )
		print(Fore.GREEN + "[+] " +Fore.YELLOW + sell.text )
		print(Fore.GREEN + "[+] " +Fore.YELLOW + "Rp" + price.text + "\n")
		# print(Fore.GREEN + "[+] " +Fore.YELLOW + img + "\n")
		tm.sleep(1)
	else:
		print("   [Done!]	")
except:
	print(" There was an error")
