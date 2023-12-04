import numpy
data = numpy.array([[1, -1, 4],[2, 1, 3],[1, 3, -1]])
C = numpy.cov(data)
eps = 1e-10
x0 =numpy.matrix([[11],[45],[14]],dtype=float)
while 1:
    t = x0[0]
    x1 = C * x0
    x0 = x1 / numpy.linalg.norm(x1)
    #print(x0)
    if abs(numpy.abs(t)-numpy.abs(x0[0])) < eps :
        break
    t = x0[0]
x1 = C * x0
print("C:\n{}".format(C))
print("最大特征值:\n{}".format(x1[0]/x0[0]))

