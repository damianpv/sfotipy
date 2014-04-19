from celery import task
import time

@task
def demorada():
    time.sleep(5)
    print 'acabe'