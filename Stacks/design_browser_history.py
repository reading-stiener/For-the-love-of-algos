class BrowserHistory:

    def __init__(self, homepage):
        self.back_stack = [homepage]
        self.forward_stack = []
        

    def visit(self, url):
        self.forward_stack = []
        self.back_stack.append(url)
        

    def back(self, steps):
        while steps > 0 and len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
            steps -= 1
        return self.back_stack[-1]


    def forward(self, steps):
        while steps > 0 and len(self.forward_stack) >= 1:
            self.back_stack.append(self.forward_stack.pop())
            steps -= 1
        return self.back_stack[-1]
