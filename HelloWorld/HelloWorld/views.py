from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def main(request):

    # views_name = 'Zhejiang Lab'
    # views_list = ['abc','def','ghk']
    # views_dict = {'abc':'zjlab'}
    # views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    # views_num = 88

    return render(request,
                  'main.html',
                  # {
                  #     "views_list": views_list,
                  #     "views_dict":views_dict,
                  #     "name":views_name,
                  #     'hype_link':views_str,
                  #     'num':views_num
                  #  }
                  )

def upload_file(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("no files for upload!")
        else:
            # 打开特定的文件进行二进制的写操作;
            with open("/tmp/%s" % File.name, 'wb+') as f:
              # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("upload over!")
    else:
        return render(request, 'excel_to_neo4j.html')

def excel_to_neo4j(file_name):
    df = pd.read_excel(file_name)

