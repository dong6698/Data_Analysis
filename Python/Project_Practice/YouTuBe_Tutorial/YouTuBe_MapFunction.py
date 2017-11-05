each_week_income = [10, 20, 24, 30, 50]

def double_income(week_money):
    return week_money * 2

'''
利用map方法 直接调用方法传值输出
'''
new_income = list(map(double_income, each_week_income))

print(each_week_income)
print(new_income)

'''
利用for循环 遍历list并且输出
'''
test_old = list()
for item in each_week_income:
    test_old.append(double_income(item))

print(test_old)