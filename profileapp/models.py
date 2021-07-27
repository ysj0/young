from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # on_delete 옵션은 Django에서 모델을 구현할 때 데이터베이스 상에서 참조무결성을 유지하여
    # ForeignKeyField가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법을 지정해 준다.
    # CASCADE : ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제한다.

    # profile 객체와 연결되어있는 user 객체를 거꾸로 불러올때, 이름으로 부르기 위해 related_name 설정

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)