import pickle

f = open("./python_basic/test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

with open("./python_basic/test.txt",'rb') as f:
    data = pickle.load(f)
    print(data)