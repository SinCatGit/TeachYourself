## django-channel tutorial

该工程依据[django-channel官方教程](https://channels.readthedocs.io/en/latest/tutorial/index.html)创建


### 运行

1. redis作为backend

```bash
docker run -p 6379:6379 --name mychannel_redis redis

```

2. 运行该工程

```bash
pipenv install # 安装依赖
python manage.py runserver # 运行工程
```

3. 访问测试

打开 http://127.0.0.1:8000/chat/hobby/ 进行测试