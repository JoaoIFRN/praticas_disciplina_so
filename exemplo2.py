from threading import Thread
import sys

class ProcessadorImpressao(Thread):
    def __init__(self,numeroThread):
        Thread.__init__(self)
        self.numero = numeroThread

    def run(self):
        while True:
            sys.stdout.write(str(self.numero))
            sys.stdout.flush()

for i in range(1,11):
    thread = ProcessadorImpressao(i)
    thread.start()
