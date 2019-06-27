import pandas as pd
import numpy as np

data_file='./asset/a'
raw_data = pd.read_csv(data_file, sep=',')

labels=raw_data['Label'].values
data=np.stack((raw_data['Col1'].values,raw_data['Col2'].values), axis=-1)
# print('data.dim')
# print(data.shape)#(6000,2)
# print(labels.shape)#(6000,)
## Fixed Parameters. Please do not change values of these parameters...
weights = np.zeros(3) # We compute the weight for the intercept as well... #(3,)
# print(weights.shape)#(3,)
num_epochs = 50000
learning_rate = 50e-5


def logistic_regression(data, labels, weights, num_epochs, learning_rate):
	dim=data.shape[0]
	data=np.insert(data,0,np.ones(1),axis=True)

	for i in range(num_epochs):
		h_t = 1/(1+np.exp(-1.0*np.dot(data, weights)))

		grad=(labels-h_t)
		weights=weights+learning_rate*np.dot(grad,data)
	return weights
coefficients=logistic_regression(data, labels, weights, num_epochs, learning_rate)
print(coefficients)