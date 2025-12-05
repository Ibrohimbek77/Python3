import threading

primes_found = []          # shared list
list_lock = threading.Lock()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            with list_lock:   # protect shared list
                primes_found.append(num)


def main():
    threads = []

    # Example range
    start_num = 1
    end_num = 200

    # Divide range into chunks
    step = 50
    for s in range(start_num, end_num + 1, step):
        e = min(s + step - 1, end_num)
        t = threading.Thread(target=check_range, args=(s, e))
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    print("Prime numbers found:")
    print(sorted(primes_found))


if __name__ == "__main__":
    main()





import threading
from collections import defaultdict

word_counts = defaultdict(int)
lock = threading.Lock()


def process_lines(lines):
    local_counts = defaultdict(int)

    for line in lines:
        words = line.strip().split()
        for w in words:
            w = w.lower()
            local_counts[w] += 1

    # merge local counts into global dictionary
    with lock:
        for w, c in local_counts.items():
            word_counts[w] += c


def threaded_word_count(filename, thread_count=4):
    with open(filename, "r") as f:
        lines = f.readlines()

    # split file into chunks
    chunk_size = len(lines) // thread_count
    threads = []

    for i in range(thread_count):
        start = i * chunk_size

        if i == thread_count - 1:
            end = len(lines)    # last thread gets leftovers
        else:
            end = start + chunk_size

        t = threading.Thread(target=process_lines, args=(lines[start:end],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return word_counts


def main():
    result = threaded_word_count("big_text.txt", 5)

    print("Word occurrences:")
    for word, count in list(result.items())[:20]:  # show first 20
        print(word, ":", count)


if __name__ == "__main__":
    main()
