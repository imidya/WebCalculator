import re
from collections import deque


class Calculator:

    def process_add(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '+':
                tmp = int(result.pop()) + int(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def process_minus(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '-':
                tmp = int(result.pop()) - int(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def process_times(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '*':
                tmp = int(result.pop()) * int(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def process_divided(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '/':
                tmp = int(result.pop()) / int(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def cal(self, question):
        data = deque(re.split(r'(\D)', question))

        result = self.process_times(data)
        result = self.process_divided(result)
        result = self.process_add(result)
        result = self.process_minus(result)

        return result.pop()
