import threading 

def print_cube(num): 
    f=open("C:\\Saket Vats\\PythonDS\\thread1.txt",'w+')
	#print("Cube: {}".format(num * num * num))
    f.write("Square: {}".format({pow(i,3) for i in range(num)}))
    f.write("Hello")
    f.close()
def print_square(num): 
	print("Square: {}".format(num * num)) 

if __name__ == "__main__": 
	# creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,))
    t1.start()
    t2.start()
    print("Done!") 
