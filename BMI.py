weight = input('請輸入體重（kg）')
height = input('請輸入身高（m）')
BMI = int(weight)/float(height)/float(height)
if BMI < 18.5:
	print('你的BMI為', BMI, '體重過輕喔')
elif BMI >= 18.5 and BMI < 24:
	print('你的BMI為', BMI, '你的體重標準')
elif BMI >= 24 and BMI < 27:
	print('你的BMI為', BMI, '超重一點點')
elif BMI >= 27 and BMI < 30:
	print('你的BMI為', BMI, '輕度肥胖子')
elif BMI >=30 and BMI < 35:
	print('你的BMI為', BMI, '中度肥子')
else:
	print('你的BMI為', BMI, '你是超級大肥子')