import sys
sys.path.append('./Learning')

import Learning

Learning.foo()
Learning.do_something()
a = Learning.Computer('myPC')
a.say_hello()


import Learning.Algebra as algebra
b = algebra.add(10, 5)
print(b)

import Learning.Arithmetic as arith
c = arith.calculate(5, 8)
print(c)

