import threading
import time
value = { 'count': 0 }
stop = { 'action': 'go' }

def increment_value(value, stop):
    while True:
        value['count'] += 1
        time.sleep(1)
        if value.get('count') >= 100:
            print('set stop')
            stop['action'] = 'stop'
            print(value, stop)
            break
    return


def save_to_disk(value, stop):
    var = 0
    while True:
        var += 1
        time.sleep(15)
        with open('num.file', 'w') as numfile:
            numfile.write('{0} - {1}'.format(value, var))
        print('{0} - {1}'.format(value, var))
        if stop.get('action') == 'stop':
            print('signaled to stop')
            break
        if var >= 10:
            print('failsafe stop')
            break
    return


def main():
    p = threading.Thread(target=save_to_disk, args=(value, stop))
    w = threading.Thread(target=increment_value, args=(value, stop))
    p.start()
    w.start()
    w.join()
    p.join()
    print(value)

if __name__ == '__main__':
    main()
