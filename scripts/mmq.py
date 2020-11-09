import matplotlib.pyplot as plt
import numpy as np

def gauss_jordan(array):
	x = np.zeros(2)
	
	for i in range(2):
		for j in range(2):
			if i != j:
			    ratio = array[j][i]/array[i][i]

			    for k in range(3):
			    	array[j][k] -= ratio*array[i][k]
				
	for i in range(2):
		x[i] = array[i][2]/array[i][i]
				
	return x

def mmq(xarray, yarray, n_var):
	#matriz das variáveis
	mc = np.array([[0,0,0],[0,0,0]])
	for i in range(2):
		for j in range(3):
			buff = xarray	
			if j == 2:
				mc[i][j] = np.sum(yarray*np.power(buff, i))
			else:
				mc[i][j] = np.sum(np.power(buff, i+j))
	
	h = gauss_jordan(mc)
	x = np.linspace(-1,1, 100)
	y = h[0] + h[1]*x
	
	fig = plt.figure()
	plt.ylabel('Metros Vendidos(x1000m²)')
	plt.xlabel(n_var)
	plt.title("Y = %.3f + %.3fX" %(h[0],h[1]))
	plt.plot(x,y, 'g')
	plt.savefig(n_var + '.png')
