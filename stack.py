#栈定义
class stack():
    def __init__(self,size):
        self.stack=[]
        self.size=size
        self.top=-1
    def push(self,content):
        if self.top==self.size:
            print 'stack is full'
        else:
            self.top+=1
            self.stack.append(content)
    def isfull(self):
        if self.top==self.size:
            return True
        else:
            return False
            
    def isempty(self):
        if self.top==-1:
            return True
        else:
            return False