import threading

def test():
	for i in range(10):
		print(i)

thread = threading.Thread(target = test)
thread.start()

print("HELLO")