'''
@author: Max

Script for reproducing the mandelbrot

'''

#imports
import numpy as np
import matplotlib.pyplot as plt
import time

class Mandelbrot:
	def __init__(self,xmax=1.5,xmin=-2.5,ymax=1.5j,ymin=-1.5j,step=0.01):
		#initial variables
		self.xmax = xmax
		self.xmin = xmin
		self.ymax = ymax
		self.ymin = ymin
		self.step = step

		self.maxiter = 100

		self.build_plot()

	def test_number(self,c):
		z = 0.0j

		for i in range(self.maxiter):
			z = z*z + c
			if np.sqrt((z.real*z.real)+(z.imag*z.imag)) >= 2:
				return i
		return self.maxiter

	def build_plot(self):
		start = time.time()

		nx = int((self.xmax-self.xmin)/self.step)
		ny = int(((self.ymax-self.ymin)/self.step *-1j).real)
		m = np.zeros((ny,nx,3))

		for iy in range(ny):
			y_val = self.ymax - iy*self.step*1j
			for ix in range(nx):
				x_val = self.xmin + ix*self.step

				c = x_val+y_val

				m[iy,ix,0] = c.real
				m[iy,ix,0] = c.imag
				m[iy,ix,2] = self.test_number(c)

		print(f'Elapsed time for step size = {self.step} is {time.time()-start} seconds...')

		plt.figure()
		plt.imshow(m[:,:,2],cmap='hot',extent=[self.xmin,self.xmax,(self.ymin*-1j).real,(self.ymax*-1j).real])
		plt.ylabel('Im')
		plt.xlabel('Re')
		plt.title('Mandelbrot Plot')
		plt.show()



if __name__ == '__main__':
	step = 0.005
	Mandelbrot(step=step)