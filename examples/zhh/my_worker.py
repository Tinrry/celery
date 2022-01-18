from celery import Celery

app = Celery('tasks', backend='db+mysql+pymysql://root:root@10.101.4.2/dev',
             broker='redis://10.101.4.2:6379/0')


@app.task
def add(x, y):
    return x + y


# 需要在celery环境中启动这个命令
if __name__ == '__main__':
    app.worker_main(argv=['worker'])
