from celery import Celery

app = Celery('tasks', backend='db+mysql+pymysql://root:root@10.101.4.2/dev',
             broker='redis://10.101.4.2:6379/0')

# same
@app.task(cpu='4')
def sub(x, y):
    return x - y

# program cpu set 40000
@app.task(exchange='feeds', cpu='4')
def add(x, y):
    return x + y

# same
@app.task(cpu='10')
def mul(x, y):
    return x * y


if __name__ == '__main__':
    app.worker_main(argv=['-A', 'tasks', 'worker', '-l', 'INFO'])
    # res = add.delay(2, 1)
    # res.ready()
    # print(res.get())
