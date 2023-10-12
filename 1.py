import  re
str1='https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E'
str2='https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&ev=exbrand_vivo%5E'
pattern=re.compile("exbrand_(.+)%5E")
brand1=re.findall(pattern,str1)
print(brand1)

