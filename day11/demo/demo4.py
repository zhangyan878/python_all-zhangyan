'''
   人类：
       姓名，性别，身高，年龄，体重，体色，地址
   地址类：
       国籍，省份，街道，门牌号
'''
class People:
    username = None
    address = None
class Address:
    country = None
    province = None
    street = None
    gate = None

adr = Address()
adr.country = "中国"
adr.province = "内蒙古"
adr.street = "古城街"
adr.street = "5003"

p = People()
p.username = "旺财"
p.address = adr

print(p.username,"，我居住在",p.address.country) # p.address --> adr