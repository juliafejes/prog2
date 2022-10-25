#!/usr/bin/env python3

from numba import njit
from person import Person
import matplotlib.pyplot as plt
from time import perf_counter as pc


def fib_py(n):
	if n<=1:
		return n
	else:
		return (fib_py(n-1)+fib_py(n-2))

@njit
def fib_numba(n):
	if n<=1:
		return n
	else:
		return (fib_numba(n-1)+fib_numba(n-2))



def main():
	t_py = []
	t_c = []
	t_n = []

	for i in range(31, 46, 2):
		t1 = pc()
		f = Person(i)
		f.fib()
		t2 = pc()
		fib_py(i)
		t3 = pc()
		fib_numba(i)
		t4 = pc()
		t_py.append(t3-t2)
		t_c.append(t2-t1)
		t_n.append(t4-t3)

	plt.figure(1)
	n = [*range(31, 46, 2)]
	fig, axis = plt.subplots()
	axis.plot(n, t_py, label='Python')
	axis.plot(n, t_c, label='C++')
	axis.plot(n, t_n, label='numba')
	axis.legend()
	axis.set(xlabel='n', ylabel='seconds (s)', title='c++ vs python (fib)')
	axis.grid()
	fig.savefig('pyCnu30-45.png')


	tjutre_py  = []
	tjutre_nu = []
	for i in range(20,31):
		t1 = pc()
		fib_py(i)
		t2 = pc()
		fib_numba(i)
		t3 = pc()
		tjutre_py.append(t2-t1)
		tjutre_nu.append(t3-t2)
	plt.figure(2)
	n = [*range(20,31)]
	fig, axis = plt.subplots()
	axis.plot(n, tjutre_py, label='python')
	axis.plot(n, tjutre_nu, label='numba')
	axis.legend()
	axis.set(xlabel='n', ylabel='s', title='numba vs pthon n=20-30')
	axis.grid()
	fig.savefig('20-30.png')


	#f = Person(47)
	#print(f'n=47 with c++: {f.fib()}, with numba: {fib_numba(47)} ')
#f.fib() (C++) with n=47: -1323752223, numba gives 2971215073
# integer overflow for C++ but not for numbah
# so it goes over




if __name__ == '__main__':
	main()
