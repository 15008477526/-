def sum(*agrs):
    result = 0
    for i in agrs:
        result += i
    return result

result = sum(1,23,3,4)
print(result)


'''
关键字打包  [形式参数]
'''
# def show_info(name,age,**kwargs):
#     print(f'个人信息的姓名{name},年龄是{age},其他信息{kwargs}')
#
# show_info('古',23,sex='男',height=154)


'''
拆包  【实际参数】
'''


