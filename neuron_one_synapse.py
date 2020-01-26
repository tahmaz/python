import numpy as np


# sigmoid function 0 ve 1 arasinda bir deyer alir hemishe, deriv=true tepe noqtesi 0 olan menfi ededlerdir /\
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset .T sertlerle sutunlarin yerini deyishir, burada bir setr yaradir sonra onu sutuna cevirir. Birbasha sutunda yaratmaq olar(array([[0], [0], [1], [1]]))
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice), neticesi sadece null-dur
np.random.seed(1)

# initialize weights randomly with mean 0, -1 ve 1 arasinda 3 eded 1 setrli matrix generate edir( np.random.random((3, 1))- 0-1 arasinda olan matrix) 2-ye vurub 1 cixdiqda deyer -1 ve 1 arasinda alinir
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(10000):
    # forward propagation l0 girish matrixdir, l1 cixish. l0 ve generate olunmush -1 ve 1 arasinda olan martixsi bir-birine vurur ve alinan deyerleri 0-1 arasina cevirir
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # how much did we miss? dogru cavabdan biz tesadufi aldigimiz deyerleri cixir ve bizim sehvmizini tapiriq
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1, sehvin deltasini tapiriq
    l1_delta = l1_error * nonlin(l1, True)

    # update weights, etdiyimiz sehv qeder dogruya yaxinlashiriq ve procedurur defelerle icra ederek dogruya yaxin netice almaga calishiriq
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)