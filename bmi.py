#輸入身高
height = input('請輸入身高（公分）：')
height = float(float(height)/100)

#輸入體重
weight = input('請輸入體重（公斤）：')
weight = float(weight)

#計算BMI
bmi = float(weight/(height*height))

#if 正常 elif 過輕 過重 輕度肥胖　中度肥胖 else 重度肥胖
if 18.5 <= bmi < 24:
    print('正常，BMI為：', bmi)
elif bmi < 18.5:
    print('過輕，BMI為：', bmi)
elif 24 <= bmi < 27:
    print('過重，BMI為：', bmi)
elif 27 <= bmi < 30:
    print('輕度肥胖，BMI為：', bmi)
elif 30 <= bmi < 35:
    print('中度肥胖，BMI為：', bmi)
else :
    print('重度肥胖，BMI為：', bmi)