with open('question.txt', 'r', encoding = 'utf_8'
                  ) as file:
            lines = file.readlines()
            print('debug', lines)
separate = []
for line in lines:
    line = line.rstrip('\n')
    separate.append(line)

print(separate)
                                      