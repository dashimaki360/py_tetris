# python tetris

class Mino():
    def __init__(self):
        self.list = [[0,0,1,0],
                     [0,0,1,0],
                     [0,0,1,0],
                     [0,0,1,0]]

    def rot(self):
        temp = [dot for dot in self.list]

class Blocks():
    def __init__(self):
        self.list = [[1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,1,1,1,1,1,1,1,1,1]]
        self.str = "init"
    def updateStr(self):
        self.str = ""
        for line in self.list:
            for dot in line:
                if dot == 0:
                    self.str += " "
                elif dot == 1:
                    self.str += "@"
                elif dot == 2:
                    self.str += "#"
                else:
                    print("ERROR")
            self.str += "\n"

class Window():
    def __init__(self):
        pass

    def show(self, Blocks):
        print(Blocks.str)

    def clear(self):
        pass

class Input():
    def __init__(self):
        pass

class Core():
    def __init__(self):
        pass

if __name__ == "__main__":
    win = Window()
    block = Blocks()
    block.updateStr()
    win.show(block)
