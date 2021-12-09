import datetime
def worker():
    print('worker Initailized')
    #will work in backend
def demoninitializer():
    t = threading.Thread(target=worker)
    # We want the program to wait on this thread before shutting down.
    t.setDaemon(True)
    t.start()