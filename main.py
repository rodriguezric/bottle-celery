import bottle
import celery

from celery.result import AsyncResult

app = celery.Celery('main', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

@app.task
def add(x, y):
    return sum(map(int, (x, y)))

@bottle.route('/')
def home():
    return 'test'

@bottle.route('/add/<x>/<y>/')
def add_route(x, y):
    res = add.delay(x, y)

    return {
        'task_id': res.id
    }

@bottle.route('/task_result/<task_id>/')
def task_result_route(task_id):
    res = AsyncResult(task_id)

    return {
        'task_id': task_id,
        'status': res.status,
        'result': res.result,
    }

if __name__ == '__main__':
    bottle.run()
