import re
from collections import deque


class Calculator:

    # def process_add(self, input):
    #     result = deque()
    #     while len(input) > 0:
    #         data = input.popleft()
    #         if data == '+':
    #             tmp = int(result.pop()) + int(input.popleft())
    #             result.append(tmp)
    #         else:
    #             result.append(data)
    #     return result

    # def process_minus(self, input):
    #     result = deque()
    #     while len(input) > 0:
    #         data = input.popleft()
    #         if data == '-':
    #             tmp = int(result.pop()) - int(input.popleft())
    #             result.append(tmp)
    #         else:
    #             result.append(data)
    #     return result

    def process_add_minus(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '+':
                tmp = int(result.pop()) + int(input.popleft())
                result.append(tmp)
            elif data == '-':
                tmp = int(result.pop()) - int(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    # def process_times(self, input):
    #     result = deque()
    #     while len(input) > 0:
    #         data = input.popleft()
    #         if data == '*':
    #             tmp = int(result.pop()) * int(input.popleft())
    #             result.append(tmp)
    #         else:
    #             result.append(data)
    #     return result

    def process_times_divided(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '*':
                tmp = int(result.pop()) * int(input.popleft())
                result.append(tmp)
            elif data == '/':
                tmp = int(result.pop()) / int(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        print result
        return result

    # def process_divided(self, input):
    #     result = deque()
    #     while len(input) > 0:
    #         data = input.popleft()
    #         if data == '/':
    #             tmp = int(result.pop()) / int(input.popleft())
    #             result.append(tmp)
    #         else:
    #             result.append(data)
    #     return result

    def cal(self, question):
        data = deque(re.split(r'(\D)', question))

        result = self.process_times_divided(data)
        result = self.process_add_minus(result)

        # result = self.process_times(data)
        # result = self.process_divided(result)
        # result = self.process_add(result)
        # result = self.process_minus(result)

        print result
        return result.pop()

# c = Calculator()
# c.cal('100/2/5*2')
# c.process_add_minus(deque([1, '+', 3]))