from threading import Thread
import sys
def imprimirConsole(numeroThread):
    while True:
        valor = "Imprimir thread de número: " + str(numeroThread) + "\n"
        sys.stdout.write(valor)
        sys.stdout.flush()
for i in range(1,11):
    thread = Thread(target=imprimirConsole, args=(i,))
    thread.start()



