#-*coding:utf-8*-
from django.db import models
from django.conf import settings

#用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,所以修改str类的title方法就可以实现.
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

# Create your models here.
STATUS = {
        0: u'正常',
        1: u'草稿',
        2: u'删除',
}

#资讯来源
NEWS = {
        0: u'oschina',
        1: u'知乎',
        2: u'BBC',
}


class Nav(models.Model):
    name = models.CharField(max_length=40,verbose_name=u'导航条内容')
    url = models.CharField(max_length=200,blank=True,null=True,verbose_name=u'指向地址')

    status = models.IntegerField(default=0,choices=STATUS.items(),verbose_name='状态')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u"导航条"
        ordering = ['-create_time']
        app_label = string_with_title('blog',u"博客管理")

    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=60,verbose_name=u'标题')

    news_from = models.IntegerField(default=0,choices=NEWS.items(),verbose_name=u'来源')
    url = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'源地址')

    summary = models.TextField(verbose_name=u'摘要')
    
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    pub_time = models.DateTimeField(u'发布时间',default=False)

    class Meta:
        verbose_name_plural = verbose_name =u'编年史'
        ordering = ['-create_time']
        app_label = string_with_title('blog',u'博客管理')

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=40,verbose_name=u'分类名')

    parent = models.ForeignKey('self',null=True,blank=True,verbose_name=u'父级分类')

    rank = models.IntegerField(default=0,verbose_name=u'排序')
    status = models.IntegerField(default=0,choices=STATUS.items(),verbose_name=u'状态')

    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)


    class Meta:
        verbose_name_plural = verbose_name =u'分类'
        ordering = ['-create_time']
        app_label = string_with_title('blog',u'博客管理')


    def __unicode__(self):
        if self.parent:
            return '%s --> %s' %(self.parent,self.name)
        else:
            return self.name


class Article(models.Model):
    title = models.CharField(max_length=40,verbose_name=u'标题')
    en_title = models.CharField(max_length=40,verbose_name=u'英文标题')
    img = models.CharField(max_length=200,default='/static/img/article/default.png')

    category = models.ForeignKey(Category,verbose_name=u'所属分类')

    view_times = models.IntegerField(default=0,verbose_name=u'浏览次数')
    rank = models.IntegerField(default=0,verbose_name=u'排序')
    status = models.IntegerField(default=0,choices=STATUS.items(),verbose_name=u'状态')

    is_top = models.BooleanField(default=False,verbose_name=u'置顶')

    summary = models.TextField(verbose_name=u'摘要')
    content = models.TextField(verbose_name=u'正文')

    pub_time = models.DateTimeField(default=False,verbose_name=u'发布时间')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['rank','-is_top','-pub_time','-create_time']
        app_label = string_with_title('blog',u'博客管理')

    def __unicode__(self):
        return self.title


class Carousel(models.Model):
    title = models.CharField(max_length=40,verbose_name=u'标题')
    img = models.CharField(max_length=200,verbose_name=u'轮播图片',default='/static/img/carousel/default.png')

    summary = models.TextField(verbose_name=u'摘要')

    status = models.IntegerField(default=0,choices=STATUS.items(),verbose_name=u'状态')

    article =models.ForeignKey(Article,verbose_name=u'文章')

    create_time = models.DateTimeField(verbose_name=u'创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'轮播'
        ordering = ['-create_time']
        app_label = string_with_title('blog',u'博客管理')

