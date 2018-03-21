import threading
import time

def myFunc():
	print('Hello World!')
	
t = Threding.thread(target = myFunc)
t.start()
