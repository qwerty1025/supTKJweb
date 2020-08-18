from django.db import models
from django.contrib.auth.models import User as auth_user
# Create your models here.

# python manage.py makemigrations  ## 作用在於 更新的內容。 step< 1 >
# python manage.py migrate         ## 作用在於 更新的內容。 step< 2 >

## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --
class User(models.Model):
    firstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length=50)
    #acc_name = models.CharField(max_length = 50)
    #acc_no   = models.IntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Articles(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False, null=False)
    content = models.CharField(max_length=500, blank=False, null=False)
    last_update = models.DateField(auto_now=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='articles_related_tags'
    )

class sel02_shun(models.Model):
    # user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    play_acc_no = models.IntegerField()
    play_acc_name = models.CharField(max_length=500, blank=False, null=False)
    pre_people = models.IntegerField()


## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --

# def booking(request):
#     sel02_shun.objects.creat(play_acc_no="0923222888",play_acc_name="SHUN_test001",pre_people="2")

def create_user():
    User.objects.create(firstName="Helii", LastName="choa")                            ## 創造
    # User.objects.filter(firstName="EEE",LastName="0922288555").update(firstName="Eva")
    ## 尋找後做一些修改
   # User.object.filter(acc_name="Snoopy", acc_no="0922288555").update(acc_name="EEE")

def cc():
    # User.objects.create(firstName="Heliigggg", LastName="gu")
    sel02_shun.objects.create(play_acc_no="0923222888", play_acc_name="SHUN_test001", pre_people="2")

def booking(request):
    # User.objects.create(firstName="Mike", LastName="Wu")
    User.objects.create(firstName="jan", LastName="Lee")
    # sel02_shun.objects.creat(play_acc_no="0923222888",play_acc_name="SHUN_test001",pre_people="2")
    return


## - -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - -- -- - -- - --  -- - -- - --

def create_articles(request):
    user = auth_user.objects.get(username=request.user)
    Articles.objects.create(user=user, content=request.POST['content'])
    return

def _create_articles(request):
    a = Articles.objects.create(user = request.user, title = request.POST['title'], content = request.POST['content'])
    query = dict(request.POST)
    for i in query['tags']:
        a.tags.add(Tag.objects.get(id=i))
    return

def _edit_articles_by_id(request,id):
    Articles.objects.filter(id=id).update(title = request.POST['title'], content = request.POST['content']) # No need to update user
    a = Articles.objects.filter(id=id).get()
    a.tags.remove() # Remove all of the previous tags
    query = dict(request.POST)
    for i in query['tags']:
        a.tags.add(Tag.objects.get(id=i)) # Update the new tags
    return

def _get_articles():
    #
    # Get all of the articles
    #
    #
    return Articles.objects.all().order_by('-last_update')





def _get_articles_by_id(id):
    return Articles.objects.filter(id=id).first() # Uses "first()" because Django objects return objects by default

def _del_articles_by_id(id):
    Articles.objects.filter(id=id).delete()
    return
#
#
# def create_articles(content):
#     user =  auth_user.objects.get(username="root")
#     # User.objects.create(user=user,content=content)  # 在 view 設定好 content 的欄位。
#     Articles.objects.create(user=user,content=content)
#     return
#
# def get_article_owner():
#     article = Articles.object.get(id=2).select_related('user');


