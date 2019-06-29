from django.shortcuts import get_object_or_404, render
from .models import Major
# Create your views here.

# 학과 전체 보여주는 페이지
def main(request):
    majors = Major.objects.all()

    return render(request, 'main.html', {'majors': majors})