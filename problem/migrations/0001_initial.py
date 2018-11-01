# Generated by Django 2.1.1 on 2018-10-31 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headline', models.CharField(default='无题', max_length=50, verbose_name='题目标题')),
                ('Time_Limit', models.IntegerField(default=1000, verbose_name='时间限制')),
                ('Memory_Limit', models.IntegerField(default=64, verbose_name='内存限制')),
                ('Prob_Description', models.TextField(null=True, verbose_name='题目描述')),
                ('Input', models.TextField(null=True, verbose_name='输入说明')),
                ('Output', models.TextField(null=True, verbose_name='输出说明')),
                ('Eg_Input', models.TextField(null=True, verbose_name='样例输入')),
                ('Eg_Output', models.TextField(null=True, verbose_name='样例输出')),
                ('Author', models.CharField(max_length=20, null=True, verbose_name='题目作者')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('Total_submision', models.IntegerField(default=0, verbose_name='提交次数')),
                ('Total_AC', models.IntegerField(default=0, verbose_name='AC次数')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_name', models.CharField(default='基础', max_length=30, verbose_name='标签名称')),
            ],
        ),
        migrations.AddField(
            model_name='problems',
            name='Tags',
            field=models.ManyToManyField(to='problem.Tag', verbose_name='题目标签'),
        ),
    ]
