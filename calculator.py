import re
from collections import deque


class Calculator:

    def process_add_minus(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '+':
                tmp = float(result.pop()) + float(input.popleft())
                result.append(tmp)
            elif data == '-':
                tmp = float(result.pop()) - float(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def process_times_divided(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '*':
                tmp = float(result.pop()) * float(input.popleft())
                result.append(tmp)
            elif data == '/':
                tmp = float(result.pop()) / float(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def cal(self, question):
        data = deque(re.split(r'([+]|[-]|[/]|[*])', question.replace(' ', '')))

        result = self.process_times_divided(data)
        result = self.process_add_minus(result)

        return result.pop()
