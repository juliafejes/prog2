#!/usr/bin/env python3

from person import Person
import matplotlib.pyplot as plt
from time import perf_counter as pc


def fib_py(n):
	if n<=1:
		return n
	else:
		return (fib_py(n-1)+fib_py(n-2))



def main():
	t_py = []
	t_c = []
	for i in range(2, 10):
		t1 = pc()
		f = Person(i)
		f.fib()
		t2 = pc()
		fib_py(i)
		t3 = pc()
		t_py.append(t3-t2)
		t_c.append(t2-t1)
	n = [*range(2, 10)]
	fig, axis = plt.subplots()
	axis.plot(n, t_py, label='Python')
	axis.plot(n, c_py, label='C++')
	axis.legend()
	axis.set(xlabel='n', ylabel='seconds (s)', title='c++ vs python (fib)')
	axis.grid()
	fig.savefig('test.png')
	plt.show()
	f = Person(11)
	print(f'f.fib() with n=47: {f.fib()}')


if __name__ == '__main__':
	main()
