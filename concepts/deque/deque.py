from collections import deque

def main():
    deq = deque([1, 2, 3, 4])

    deq.append(5)
    print(deq)

    deq.pop()
    print(deq)

    deq.appendleft(0)
    print(deq)

    deq.popleft()
    print(deq)

    # starts searching from the 'start' index to 'stop' index
    print(deq.index(4, 3, 5))

    deq.insert(3, 6)
    print(deq)

    print(deq.count(3))

    deq.remove(6)
    print(deq)

    print(len(deq))


if __name__ == "__main__":
    main()