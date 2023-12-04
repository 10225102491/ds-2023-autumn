import numpy
A = numpy.matrix([[2,1],[4,5]],dtype=float)
eps = 1e-10
x0 =numpy.matrix([[114],[514]],dtype=float)
while 1:
    t = x0[0]
    x1 = A * x0
    x0 = x1 / numpy.linalg.norm(x1)
    print(x0)
    if abs(numpy.abs(t)-numpy.abs(x0[0])) < eps :
        break
    t = x0[0]
x1 = A * x0
print("A:\n{}".format(A))
print("最大特征值:\n{}".format(x1[0]/x0[0]))

