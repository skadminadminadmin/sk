from django.db import models

# Create your models here.


class User(models.Model):
    '''
    员工表
    '''
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    def __str__(self):
        return self.name
class Clazz(models.Model):
    '''
    班级表
    '''
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
class Student(models.Model):
    '''
    学生表
    '''
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    #关联字段
    clazz = models.ForeignKey(to='Clazz')

    def __str__(self):
        return self.name
class Quentionnaire(models.Model):
    '''
    问卷表
    '''
    title = models.CharField(max_length=32)

    # 关联字段
    clazz = models.ForeignKey(to='Clazz')
    creator = models.ForeignKey(to='User')

    def __str__(self):
        return self.title

class Question(models.Model):
    '''
    问题表
    '''
    name = models.CharField(max_length=32)

    type = (
        (1,'打分'),
        (2,'单选'),
        (3,'评价')
    )

    question_type = models.IntegerField(choices=type)

    #关联关系
    questionnaire = models.ForeignKey(to='Quentionnaire')

    def __str__(self):
        return self.name

class Option(models.Model):
    '''
    单选题的选项
    '''

    name = models.CharField(verbose_name='选项名称',max_length=32)
    score = models.IntegerField(verbose_name='选项打分')
    question = models.ForeignKey(to='Question')

    def __str__(self):
        return self.name

class Answer(models.Model):
    '''
    回答表
    '''

    content = models.CharField(max_length=255,null=True,blank=True)
    value = models.IntegerField(null=True,blank=True)

    #关联关系
    student = models.ForeignKey(to='Student')
    question = models.ForeignKey(to='Question')
    option = models.ForeignKey(to='Option',null=True)

