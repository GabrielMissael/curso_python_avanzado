import time

class FiboIter():

    def __init__(self, max = None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.counter < self.max:

            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                n1 = self.n2
                self.n1, self.n2 = n1, self.n1 + self.n2
                self.counter += 1
                return self.n2
        else:
            raise StopIteration

if __name__=='__main__':

    fibonacci = FiboIter(max = 10)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)