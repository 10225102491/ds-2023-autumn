import  numpy
A = numpy.array([[2,1],[4,5]])
print('矩阵：\n{}'.format(A))
a, b = numpy.linalg.eig(A)
print('特征值：\n{}'.format(a))
print('特征向量：\n{}'.format(b))