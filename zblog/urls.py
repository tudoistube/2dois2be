"""zmysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

'''
    (?P<pk>\d+) 이 정규표현식은 장고가 pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻입니다. 
    \d은 문자를 제외한 숫자 0부터 9 중, 한 가지 숫자만 올 수 있다는 것을 말합니다. 
    +는 하나 또는 그 이상의 숫자가 올 수 있습니다.. 
    따라서 http://127.0.0.1:8000/post/라고 하면 post/ 다음에 숫자가 없으므로 해당 사항이 아니지만, 
    http://127.0.0.1:8000/post/1234567890/는 완벽하게 매칭됩니다.
'''
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/1/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]