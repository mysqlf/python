from django.db import models
class Article(model.Model):
    STATUS_CHOICES=(
        ('d','Draft'),
        ('p','Published'),
    )
    title=models.CharField('标题',max_length=70)
    body=models.TextField('正文')
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time=models.DateTimeField('修改时间',auto_now=True)
    status=models.CharField('文章状态',max_length=1,choices=STATUS_CHOICES)
    abstract=models.CharField('摘要',max_length=54,blank=True,help_text='')
    view=models.PositiveIntegerField('浏览量',dedault=0)
    like=models.PositiveIntegerField('点赞数',dedault=0)
    topped=models.BooleanField('置顶',dedault=False)
    category=models.ForeignKey('Category',verbose_name='分类',null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-last_modified_time']
class Category(models.Model):
    name=models.CharField('类名',max_length=20)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time=models.DateTimeField('修改时间',auto_now=True)
    def __str__(self):
        return self.name







































