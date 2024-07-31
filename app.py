
import os
from flask import Flask

fibapp = Flask(__name__)
fibapp.config.from_object(os.environ['APP_CONFIG'])

print('DEBUG:', fibapp.config['DEBUG'])
print('TESTING:', fibapp.config['TESTING'])


@fibapp.route('/') 
def index():
    return "Hello World!"


@fibapp.route('/fib/<int:x>')
def fib(x):
    return str(calcfib(x))
def calcfib(n):
    if n == 0:
        return 0
    b, a = 0, 1             # b, a initialized as F(0), F(1)
    for i in range(1,n) :
        b, a = a, a+b       # b, a always store F(i-1), F(i) 
    return a

if __name__ == '__main__':
    fibapp.run()