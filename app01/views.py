from django.shortcuts import render,redirect,HttpResponse

def test(request):
    '''测试，文件的提交和contentType参数的使用规则，注意看post的源码，知道contentType的默认参数'''
    if request.is_ajax():
        # 注意如果为json只能从body中取值，注意只有contentType:application/json时才能使用body,否则报错
        import json
        print('--->',request.POST)
        print('--->',request.FILES)
        file = request.FILES.get('file')#此时的file是个文件对象！！！彻底理解清楚了吧，宋康你个人才
        print(file.name)
        # print(body,'body----->')
        # print(body.decode('utf-8'),type(json.loads(body.decode('utf-8'))))
        return HttpResponse('ok')
    elif request.method == 'GET':
        # get请求所有数据都在get中，因此无需使用body,file等
        data = request.GET
        print(data)
        return render(request,'test.html')
    else:
        file = request.FILES
        with open(file.get('file').name,'wb') as f:
            for i in file.get('file'):
                f.write(i)
        print(request.POST)
        return HttpResponse('ok')
def git(request):

    return render(request,'git.html')

def index(request):



    return render(request,'index.html')

