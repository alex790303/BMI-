# BMI計算機
h = input('請問你的身高(cm)')
h = int(h)
h = h / 100
w = input('請問你的體重(kg)')
w = int(w)
bmi = w / h / h
print(bmi)
if bmi < 18.5:
	print('你的bmi值', bmi, ',體重過輕')
elif bmi >= 18.5 and bmi <= 24:
	print('你的bmi值', bmi, ',體重正常')
elif bmi > 24 and bmi <= 27:
	print('你的bmi值', bmi, ',輕度肥胖')
elif bmi > 27 and bmi < 30:
	print('你的bmi值', bmi, ',中度肥胖')
else:
	print('你的bmi值', bmi, ',超肥')