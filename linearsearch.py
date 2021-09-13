from datetime import datetime

def search(array, length, x):
    start_time = datetime.now()

    for i in range(0, length):
        if (array[i] == x):
            end_time = datetime.now()
            print("The element is found at index: ", i+1)

    end_time = datetime.now()
    print('Funciton running time: {}'.format(end_time - start_time))
    return -1


array = [1,2,3,4,5,6,7,4]
x = 4
length = len(array)

search(array, length, x)
