from django.shortcuts import render

def test(request):

    views_name = 'Zhejiang Lab'
    views_list = ['abc','def','ghk']
    views_dict = {'abc':'zjlab'}
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    views_num = 88

    return render(request,
                  'test.html',
                  {
                      "views_list": views_list,
                      "views_dict":views_dict,
                      "name":views_name,
                      'hype_link':views_str,
                      'num':views_num
                   }
                  )
