from celery import Celery

app = Celery('tasks', backend='db+mysql+pymysql://root:root@10.101.4.2/dev',
             broker='redis://10.101.4.2:6379/0',  strategy='simp_strategy')


# same
@app.task(cpu='4')
def sub(x, y, resource_required):
    """
    resource_required: 是否需要保证超算底层的资源满足task的声明需求，默认false，关闭这个要求。

    test:
    task 的 strategy不更新，不需要资源限制
    """
    return x - y


# program cpu set 40000
@app.task(exchange='feeds', cpu='10')
def add(x, y, resource_required):
    """
    resource_required: 是否需要保证超算底层的资源满足task的声明需求，默认false，关闭这个要求。

    test:
    task 的 strategy应该更新，不需要资源限制
    """
    return x + y


# same
@app.task(cpu='10')
def mul(x, y, resource_required):
    """
    resource_required: 是否需要保证超算底层的资源满足task的声明需求，默认false，关闭这个要求。

    test:
    task 的 strategy应该更新，进行资源限制
    """
    return x * y


if __name__ == '__main__':
    app.worker_main(argv=['-A', 'tasks', 'worker', '-l', 'INFO'])
    # res = add.delay(2, 1)
    # res.ready()
    # print(res.get())
