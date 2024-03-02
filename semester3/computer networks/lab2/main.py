import socket
import struct
import threading
import random
matrix = []
threads =[]
client_count = 0


random.seed()
start=1; stop=2**17-1
my_num= random.randint(start,stop)
print('Server number: ',my_num)

mylock = threading.Lock()
e = threading.Event()
e.clear()


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def worker(client):
    try:
        # Receive the length of the array (n)
        int_size = struct.calcsize('I')
        n_bytes = client.recv(int_size)

        n = struct.unpack('!I', n_bytes)[0]

        if n == 0:
            print("Received empty array. Closing connection.")
            return

        # Receive the array of floats
        data = client.recv(int_size * n)

        floats = struct.unpack('!{}I'.format(n), data)

        # Sort the array
        sorted_data = merge_sort(floats)

        # Send the sorted array back to the client
        sorted_data_packed = struct.pack('!{}I'.format(len(sorted_data)), *sorted_data)
        client.send(sorted_data_packed)

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client.close()


def resetSrv():
    global mylock, client_guessed, winner_thread, my_num, threads, e, client_count
    while True:
        e.wait()
        for t in threads:
            t.join()
        print("all threads are finished now")
        e.clear()
        mylock.acquire()
        threads = []
        client_count = 0
        my_num = random.randint(start, stop)
        print('Server number: ', my_num)
        mylock.release()

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('0.0.0.0', 1234))
        server.listen(1024)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    t = threading.Thread(target=resetSrv, daemon=True)
    t.start()
    while True:
        client_socket, addr = server.accept()
        t = threading.Thread(target=worker, args=(client_socket,))
        threads.append(t)
        client_count += 1
        t.start()