from django.db import models

# Create your models here.
class Category(models.Model):
    """
    分类
    """

    name = models.CharField('名称', max_length=16)


class Tag(models.Model):
    """
    标签
    """

    name = models.CharField('名称', max_length=16)


class Blog(models.Model):
    """
    博客
    """

    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签')

class Book(models.Model):
    """
    书
    """

    title = models.CharField('标题', max_length=32)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签')

class Blog_Comment(models.Model):
    """
    博客评论
    """

    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
    created = models.DateTimeField('发布时间', auto_now_add=True)

class Book_Comment(models.Model):
    """
    图书评论
    """

    book = models.ForeignKey(Book, verbose_name='图书')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
    created = models.DateTimeField('发布时间', auto_now_add=True)
