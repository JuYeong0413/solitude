from django.db.models import *
from django.contrib.auth.models import User
from classes.models import *

# Create your models here.
class TimeStampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    classname = ForeignKey(Class, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    category = CharField(max_length=200)
    title = CharField(max_length=200)
    content = TextField()
    view_count = models.IntegerField(default=0) # 조회수
    likes = ManyToManyField(User, related_name="liked_users")
    is_top = BooleanField(default=False)

    def comments(self):
        return Comment.objects.filter(post=self)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    post = ForeignKey(Post, on_delete=CASCADE)
    message = TextField()

    def __str__(self):
        return self.message