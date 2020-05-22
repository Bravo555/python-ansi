import threading
import time
import signal
import sys
import os


def leave(signum=0, frame=0):
    sequence('?1049l')
    sys.exit(0)


def sequence(s):
    sys.stdout.write('\033[' + s)
    sys.stdout.flush()


def append(text, n, height):
    sequence('s')
    sequence('{}H'.format(n))
    if n >= height:
        sequence('S')
        sequence('A')
        sequence('L')
    print(text)
    sequence('u')


def printing_thread():
    height = os.get_terminal_size()[1]
    for i in range(1, 50):
        lock.acquire()
        append(i, i+1, height)
        lock.release()
        time.sleep(1)


signal.signal(signal.SIGINT, leave)

printing_thread = threading.Thread(target=printing_thread, daemon=True)
lock = threading.Lock()
lock.acquire()
printing_thread.start()

sequence('?1049h')
sequence('H')

print('hello there')
sequence('999B')

inp = ''
while inp != 'e':
    sys.stdout.write('> ')
    sys.stdout.flush()
    lock.release()
    inp = input()
    lock.acquire()
    print('marcel: ' + inp)

leave()
