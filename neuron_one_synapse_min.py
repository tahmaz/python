from numpy import exp, array, random, dot
X = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
y = array([[0,1,1,0]]).T
random.seed(1)
syn0 = 2*random.random((3,1)) - 1
print(syn0)
for iteration in range(10000):
    l1 = 1/(1+exp(-(dot(X,syn0))))
    syn0 += dot(X.T, (y - l1) * l1 * (1 - l1))
print(syn0)

print(1 / (1 + exp(-(dot(array([1, 0, 0]), syn0)))))