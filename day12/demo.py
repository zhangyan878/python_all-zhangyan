class OldPhone:
    phoneNumber = None
    vioce = None

    def call(self,number):
        print(self.phoneNumber,"正在给",number,"打电话......")

class NewPhone(OldPhone):
    place = None # 归属地
    picture = None # 大头贴
    ps = None # 备注

    def call(self,number):
        super().call(number)
        print("归属地：",self.place,"，图片：",self.picture,"，备注：",self.ps)

phone = NewPhone()
phone.phoneNumber = "13489076522"
phone.vioce = "月亮之上"
# 给新手机的新属性进行赋值
phone.place = "河北"
phone.picture = "野猪佩奇"
phone.ps = "旺财来电"
phone.call("12458392012")