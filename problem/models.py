from django.db import models

# Create your models here.

class Tag(models.Model):
    Tag_name=models.CharField("标签名称",primary_key=True,max_length=30)
    Prob_num=models.IntegerField("标签对应题目数量",default=0)
    def __str__(self):
        return self.Tag_name


class Problems(models.Model):
    Pid=models.AutoField("题目编号",primary_key=True)                          #题目编号
    Headline=models.CharField("题目标题",max_length=50,null=False)             #题目标题，限制字符50
    Time_Limit=models.CharField("时间限制",max_length=30,null=False)           #时间限制，限制字符30
    Memory_Limit=models.CharField("内存限制",max_length=30,null=False)         #内存限制，限制字符30
    Prob_Description=models.TextField("题目描述",null=False)                   #问题描述
    Input=models.TextField("输入说明", null=True)                              #输入
    Output=models.TextField("输出说明", null=True)                             #输出
    Eg_Input=models.TextField("样例输入",null=True)                            #样例输入，可为空
    Eg_Output=models.TextField("样例输出",null=True)                           #样例输出，可为空
    Author=models.CharField("题目作者",max_length=20,null=True)                #题目作者，所有用户名限制字符为20，可为空
    Up_time=models.DateField("上传时间")                                       #题目上传时间
    Total_submision = models.IntegerField("提交次数",default=0)                #本题总提交次数，根据states表
    Total_AC = models.IntegerField("AC次数",default=0)                         #本题总AC次数,根据states表
    Tags=models.ManyToManyField(Tag,verbose_name="题目标签")                   #题目标签（分类），多对多关系，自动生成对应表




