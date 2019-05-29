class stack():
    def __init__(self,size):
        self.size=size
        self.stack=[None]*size
        self.top=-1

    def push(self,data):
        if(self.top==len(self.stack)-1):
            print('sack overflow')
            return
        self.stack[self.top]=data

    def pop(self):
        if(self.top==-1):
            print('empty stack')
            return

