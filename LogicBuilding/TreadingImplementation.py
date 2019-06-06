# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 

def print_cube(num): 
	""" 
	function to print cube of given num 
	"""
    f=open('cube.txt','w+')
    for i in range(10):
        f.write(i)
	#f.write("Cube: {}\n".format({pow(i,3) for i in range(num)}))
	
    f.close()
    print("Cube Completed")


if __name__ == "__main__": 
	# creating thread
    num=1000
    t1 = threading.Thread(target=print_cube, args=(num,)) 
	#t2 = threading.Thread(target=print_pow5, args=(num,)) 
	# starting thread 1
    t1.start() 
	# starting thread 2 
	#t2.start() 
	# wait until thread 1 is completely executed
    t1.join()
	# wait until thread 2 is completely executed 
	#t2.join()

	# both threads completely executed
    print("Done!") 
