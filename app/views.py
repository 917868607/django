from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

numbers = random.randint(1, 101)


class People(object):
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


def index(request):
    print(request)

    people = People('李四', 25, 1111)

    data = {
        'name': '张三',
        'age': 22,
        'numbers': [x for x in range(0, 30) if x % 2 == 0],
        'dictData': {'city': '郑州', 'weather': '晴天'},
        'people': people
    }
    return render(request, 'index.html', data)


def login(request):
    print(request)
    # 判断是get 请求 还是post 请求

    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        #
        #
        ID = request.POST.get('id', default='')
        pwd = request.POST.get('pwd', default='')
        if ID == '123456789' and pwd == '123456':
            return HttpResponse('登录成功')
        else:
            return render(request, 'login.html', {'error': '密码错误'})


# 定义主页的视图函数
def guess_num(request):
    result = ''
    # 判断当前请求的 是get /post
    # 设置全局变量
    global numbers
    if request.method == 'POST':
        # 从post 请求中提取传递过来的参数
        gus_num = request.POST.get('gus_num', default='0')
        if gus_num == '':
            result = '请重新输入,数字不能为空'
        else:
            if int(gus_num) < numbers:
                result = '猜小了'
            elif int(gus_num) > numbers:
                result = '猜大了'
            else:
                result = '猜对了,答案已重置,请继续'
                numbers = random.randint(0,101)
    names = ['小红', '小明', '小李', '小王', '小花']
    data = {
        'name': random.choice(names),
        'age': random.randint(18, 23),
        # 返回的是一个列表,startswith () 是以什么开头的
        'names': [name for name in names if name.startswith('小')],
        'phone': 13213,
        'result': result
    }
    # data 就是箱模板传递参数
    return render(request, 'guess_num.html', data)
