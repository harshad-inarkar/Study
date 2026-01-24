import threading

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.current = 1
        #self.lock = threading.Lock()
        self.cv = threading.Condition()

    def fizz(self, printFizz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printFizz()
                self.current += 1
                self.cv.notify_all()

    def buzz(self, printBuzz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printBuzz()
                self.current += 1
                self.cv.notify_all()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 15 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printFizzBuzz()
                self.current += 1
                self.cv.notify_all()

    def number(self, printNumber):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printNumber(self.current)
                self.current += 1
                self.cv.notify_all()

# Test code
import io
import sys

def run_fizzbuzz(n):
    output = []
    def printFizz():
        output.append("fizz")
    def printBuzz():
        output.append("buzz")
    def printFizzBuzz():
        output.append("fizzbuzz")
    def printNumber(x):
        output.append(str(x))

    fb = FizzBuzz(n)
    threads = [
        threading.Thread(target=fb.fizz, args=(printFizz,)),
        threading.Thread(target=fb.buzz, args=(printBuzz,)),
        threading.Thread(target=fb.fizzbuzz, args=(printFizzBuzz,)),
        threading.Thread(target=fb.number, args=(printNumber,))
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return output

def test_fizzbuzz():
    assert run_fizzbuzz(15) == [
        '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz',
        '11', 'fizz', '13', '14', 'fizzbuzz'
    ]
    assert run_fizzbuzz(5) == ['1', '2', 'fizz', '4', 'buzz']
    assert run_fizzbuzz(1) == ['1']
    assert run_fizzbuzz(0) == []
    print("All tests passed.")

if __name__ == "__main__":
    test_fizzbuzz()

