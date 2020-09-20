import requests as req
import time as tm
# import sys
from bs4 import BeautifulSoup as bs
from colorama import init,Fore
import csv
init()

def curl(page,query):
    return req.get('https://www.bukalapak.com/products?page='+page+'&search%5Bkeywords%5D=+query')

# def ani():
#     for i in range(10):
#         sys.stdout.write(" -")
#         tm.sleep(0.5)
#     print(" >")

# header = []

print (" ##########################")
print (" #                        #")
print (" #        Insomniac       #")
print (" #  https://insomniac.id  #")
print (" #    Lupabapak Scraper   #")
print (" #                        #")
print (" ##########################")
try:
    query = input(" Search keyword : ")
    page = '1'
    print(" Searching "+ query + " on bukalapak")
    get = curl(page,query)
    tm.sleep(0.5)
    sop = bs(get.text, 'html.parser')
    pg = sop.find("span", attrs={'class':'last-page'})
    print(Fore.YELLOW +"",pg.text,"Pages Found")
    begin = input(' Page start : ')
    page = input(' Page end   : ')
    file = open('Lupabapak.csv','w') # w untuk write/mengganti data sebelumnya 
                                     # a untuk menambah data tanpa menghapus data sebelumnya
    writer = csv.writer(file)
    writer.writerow(['Nama Barang', 'Toko', 'Harga'])
    # ani() 
    for i in range(int(begin),int(page)+1):
        get = curl(str(i),query)
        tm.sleep(0.5)
        sop = bs(get.text, 'html.parser') 
        go = sop.find_all("article", attrs={'class':'product-display'})
        print(Fore.RED + "[-] " +Fore.YELLOW + "Page",str(i),"searching items...")
        tm.sleep(2)
        print(Fore.RED + "[-]" +Fore.YELLOW ,len(go),"Items Found \n")
        tm.sleep(1)
        for p in go:
            name = p.find("a", attrs={'class':'product__name line-clamp--2 js-tracker-product-link qa-list'})
            seller = p.find("h5", attrs={'class':'user__name'})
            sell = seller.find("a",href=True)
            price = p.find("span", attrs={'class':'amount positive'})
            # img = p.find("source").get('data-src')
            print(Fore.GREEN + "[+] " +Fore.YELLOW + name.text )
            print(Fore.GREEN + "[+] " +Fore.YELLOW + sell.text )
            print(Fore.GREEN + "[+] " +Fore.YELLOW + "Rp" + price.text + "\n")
            # print(name.text, sell.text, price.text) # Bisa pakai ini aja kalau gak mau warna warni
            writer.writerow([name.text, sell.text, price.text.replace('.','')])
            # print(Fore.GREEN + "[+] " +Fore.YELLOW + img + "\n")
            tm.sleep(1)
        else:
            print(Fore.RED + "[-] " +Fore.YELLOW + "Page",str(i),"Done!\n")
    file.close()
except:
    print(" There was an error!")
