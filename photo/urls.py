from django.urls import path
from . import views
# 현재 폴더에서 views를 가져오라는 의미

urlpatterns = [
    path('', views.photo_list, name = 'photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name = 'photo_detail'),

]

# pk -> 정수형 변수가 들어감
# 기본 ID값으로 구분
#

# path = > 127.0.0.1:8000
# 현재 폴더에서 views.py를 가져오고 photo_list 함수 실행 name은 photo_list

# photo url에도 추가