from celery import Celery
app = Celery('tasks', backend='redis://rd', broker='pyamqp://rq')  # 注意这行！！！！

@app.task
def add(x, y):
    return x + y
