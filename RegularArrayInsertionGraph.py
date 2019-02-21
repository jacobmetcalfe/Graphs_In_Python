from matplotlib import pyplot as py
import time as time
# simple array insertion with time
start = time.time()
array = []
for x in range(100):
    array.append(x)

end = time.time()
totaltime = end-start
print(totaltime)
py.plot(array, c='blue')
py.title("Regular Graph")
py.xlabel("Index")
py.ylabel("Value")

py.show()
