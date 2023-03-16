from itertools import permutations

def calc(_nums: list) -> bool:

    _opers = ['+', '-', '*', '/']

    for nums in permutations(_nums):
        for bracket_number in range(1, 5):  # bracket number (1, 2, 3, 4)
            for bracket_pos in range(0, 4 - bracket_number + 1):  # (0, 1, 2, 3)
                for oper1 in _opers:
                    for oper2 in _opers:
                        for oper3 in _opers:
                            statement = ''
                            oper = [oper1, oper2, oper3]
                            for i, n in enumerate(nums):
                                if i == bracket_pos:
                                    statement += '('
                                statement += str(n)
                                if i == bracket_pos + bracket_number - 1:
                                    statement += ')'
                                if i < len(oper):
                                    statement += oper[i]
                            try:
                                if eval(statement) == 10:
                                    print(f'Found answer: {statement}')
                                    return True
                            except ZeroDivisionError:
                                continue

    return False

def main():
    while True:
        try: 
          if not calc(list(map(int, input('Please enter the numbers: ').strip().split()))):
            print('Answer not found')
        except EOFError: return


if __name__ == '__main__':
    main()
