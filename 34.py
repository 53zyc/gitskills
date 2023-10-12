import csv
import re
import time
import random
from time import sleep

import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# url = 'https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA'
# # wb_data = requests.get(url, headers={'User-Agent': str(UserAgent().random)}).text
# # soup = BeautifulSoup(wb_data, "lxml")
# # url = f'https://search.jd.com/search?keyword=手机&wq=手机&ev=exbrand_{brand} %&psort=4'
# wb_data = requests.get(url, headers={'User-Agent': str(UserAgent().random)}, verify=False).text
# soup = BeautifulSoup(wb_data, "lxml")
# lis = soup.find_all(class_='gl-item')
# id_brand = []
# sleep(2)
#
# for i in lis:
#     id = []
#     id.append(i.attrs["data-sku"])
#     id_brand.append(id)
# print(lis)
# print(len(lis))

brand='荣耀（HONOR）'
print(f"开始{brand}")
for i in range(1,5):
    url = f'https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&ev=exbrand_{brand}%5E&psort=4&click=0'
    wb_data = requests.get(url, headers={'User-Agent': str(UserAgent().random)}, timeout=5, verify=False).text
    soup = BeautifulSoup(wb_data, "lxml")
    id_list = []
    lis = soup.find(class_='crumb-select-item')
    print((lis))

    print("获取商品id")

    print(lis.attrs["title"])
    # print(len(id_list))



# for productId in id_list:
#     # 一个商品的好评中评差评
#     for score in [3, 2, 1]:
#         link = f'https://club.jd.com/comment/productPageComments.action?' \
#                f'callback=fetchJSON_comment98&productId={productId}&score={score}&sortType=5' \
#                f'&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'
