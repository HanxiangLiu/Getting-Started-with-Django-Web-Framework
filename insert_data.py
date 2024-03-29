import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()

from datetime import datetime
from faker import Faker
import random

from learn.models import Course


fake = Faker('zh-cn')
name_list = ['Django 入门与实践', 'C++ 实现简易 Docker 容器', 'Flask 实现问答社区']


def create_courses():
    for name in name_list:
        course = Course(name=name, pub_date=fake.date(), stu_number=random.randint(100, 1000))
        course.save()


if __name__ == '__main__':
    create_courses()