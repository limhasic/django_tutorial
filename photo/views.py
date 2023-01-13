from django.shortcuts import render
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos':photos})

# {P} 데이터 전달 시 사용 #
# 함수 photo_list() 호출 시 photo_list.html이 불러와짐

from django.shortcuts import render, get_object_or_404
# 모델로부터 데이터를 찾아보고 없으면 404 에러를 반환하는 함수

def photo_detail(request, pk:
    photo = get_object_or_404(Photo, pk)
    return render(request, 'photo/photo_detail.html', {'photo':photo})

# 추가하고는 view에 등록