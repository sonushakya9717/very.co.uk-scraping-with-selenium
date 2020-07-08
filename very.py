
# import selenium,time,json
# import requests
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from pprint import pprint
# a="https://www.very.co.uk/women/e/b/1589.end"
# browser = webdriver.Chrome("/home/banner/Downloads/chromedriver")
# browser.maximize_window()

# browser.get(a)
# time.sleep(9)
# soup = BeautifulSoup(browser.execute_script("return document.documentElement.outerHTML"),"html.parser")

# data = soup.find("form",id="endecaNavigation")

# uli=data.find_all("ul")
# h3=data.find_all("h3")


# dictonary={}
# for i in range(len(uli)):
# 	liu=uli[i].find_all("li")
# 	dictonary[h3[i].get_text()]={}
# 	for j in liu:
		
# 		dictonary[h3[i].get_text()][j.get_text()]=j.find("a")["href"]
# # create=open("BeautifulSoup.json","w+")
# # json.dump(dictonary,create,indent=8)
# browser.quit()

# import requests,selenium,time,json
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from pprint import pprint
# create=open("BeautifulSoup.json","r")
# dictionary=json.load(create)

# for i in dictionary:

# 	for j in dictionary[i]:
# 		file=open("BeautifulSoup2.json","r")
# 		prevfile=json.load(file)
# 		lsit=[]

# 		if j.split(" product ")[0] not in prevfile:
# 			for count1 in range(1,(int(j.split(" product ")[1])//99)+2):
# 				browser = webdriver.Chrome("/home/banner/Downloads/chromedriver")
# 				browser.maximize_window()
# 				browser.get(dictionary[i][j]+"?"+"pageNumber="+str(count1)+"&"+"numProducts=99")
# 				soup = BeautifulSoup(browser.execute_script("return document.documentElement.outerHTML"),"html.parser")
# 				browser.quit()
# 				time.sleep(10)
# 				data = soup.find("ul",class_="productList")
# 				lii=data.find_all("li",class_="product")
# 				for li in lii:
# 					dicdict={}
# 					branddisc=li.find("span",class_="productBrandDesc").get_text()
# 					productimg=li.find("a",class_="productMainImage").img["src"]
# 					producturl=li.find("a",class_="productMainImage")["href"]
# 					brand=li.find("em",class_="productBrand").get_text()
# 					print(branddisc,productimg,producturl,brand)

# 					dicdict["productBrandDescription"]=branddisc
# 					dicdict["productImage"]=productimg
# 					dicdict["productUrl"]=producturl
# 					dicdict["productBrand"]=brand
# 					lsit.append(dicdict)



# 			prevfile[j.split(" product ")[0]]=lsit
# 		file=open("BeautifulSoup2.json","w+")
# 		json.dump(prevfile,file,indent=4)



# import requests,selenium,time,json
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from pprint import pprint
# create=open("BeautifulSoup4.json","r")
# dictionary=json.load(create)
# for i in range(len(dictionary)):
# 	create=open("BeautifulSoup4.json","r")
# 	dictionary=json.load(create)
# 	if "description" not in dictionary[i]:
# 		browser = webdriver.Chrome("/home/banner/Downloads/chromedriver")
# 		browser.maximize_window()
# 		browser.get(dictionary[i]["productUrl"])
# 		soup = BeautifulSoup(browser.execute_script("return document.documentElement.outerHTML"),"html.parser")
# 		browser.quit()
# 		dictionary[i]["description"]=soup.find("span",itemprop="description").get_text().split(soup.find("span",itemprop="description").h2.get_text())[1]

# 		create=open("BeautifulSoup4.json","w+")
# 		json.dump(dictionary,create,indent=2)

	
import requests,selenium,time,json,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# from pprint import pprint
# count=0
# create=open("BeautifulSoup4.json","r")
# dictionary=json.load(create)
# for i in range(len(dictionary)):
# 	count+=1
# 	fileName="product_html/"+dictionary[i]["productUrl"][-14:-3]+".txt"
# 	if os.path.exists(fileName):
# 		print(count , "file exists")
# 		# create=open(fileName,"r")
# 		# data=create.read()
# 		# soup = BeautifulSoup(data,"html.parser")
# 		# print(soup.find("span",itemprop="description").get_text().split(soup.find("span",itemprop="description").h2.get_text())[1])
# 	else:
browser = webdriver.Chrome("/home/banner/Downloads/chromedriver")
browser.maximize_window()
browser.get('https://www.facebook.com')
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
# 		browser.get(dictionary[i]["productUrl"])
# 		create=open(fileName,"w+")
# 		create.write(browser.execute_script("return document.documentElement.outerHTML"))
# 		browser.quit()
# 		print(count,"created")
#


