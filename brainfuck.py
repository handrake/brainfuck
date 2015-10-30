import sys
from getch import getch

commands = '><+-.,[]'

class BrainfuckInterpreter:
    def __init__(self):
        self.i = 0
        self.p = 0
        self.cells = [0]

    @staticmethod
    def find_matching_paren(source, c):
        paren = 0
        d = {'[':']', ']':'['}
        for k in range(len(source)):
            if source[k]==c:
                paren += 1
            elif source[k]==d[c]:
                if paren == 0:
                    return k
                paren -= 1
        return -1

    def eval(self, source):
        s = ''
        while self.i != len(source):
            c = source[self.i]
            if c == '>':
                if self.p == len(self.cells)-1:
                    self.cells.append(0)
                self.p += 1
            elif c == '<':
                if self.p != 0:
                    self.p -= 1
            elif c == '+':
                self.cells[self.p] += 1
            elif c == '-':
                self.cells[self.p] -= 1
            elif c == '.':
                sys.stdout.write(chr(self.cells[self.p]))
                sys.stdout.flush()
                s += chr(self.cells[self.p])
            elif c == ',':
                self.cells[self.p] = ord(getch())
            elif c == '[' and self.cells[self.p] == 0:
                self.i += self.find_matching_paren(source[self.i+1:], c)
            elif c == ']' and self.cells[self.p] != 0:
                self.i -= self.find_matching_paren(source[self.i-1::-1], c) + 1
            self.i += 1
        return s

def main():
    source = ''
    while 1:
        line = input("brainfuck>> ")
        if line == '':break
        source += line
    source = ''.join([c for c in source if c in commands])
    interpreter = BrainfuckInterpreter()
    interpreter.eval(source)

if __name__ == "__main__":
    main()
