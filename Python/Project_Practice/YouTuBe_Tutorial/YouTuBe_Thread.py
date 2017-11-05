import threading

class sendMessage(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = sendMessage(name = 'send message')
y = sendMessage(name = 'receive message')

x.start()
y.start()
y.join()

