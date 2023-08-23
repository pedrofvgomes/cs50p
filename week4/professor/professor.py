import random

def main():
    level = get_level()
    # generate problems
    problems = []
    while len(problems) < 10:
        problems.append(str(generate_integer(level)) + ' + ' + str(generate_integer(level)) + ' = ')
    
    # play
    score = 0
    for problem in problems:
        tries = 0
        while True:
            x = input(problem)
            if x.isnumeric():
                p = problem.split(' ')
                if int(x) == int(p[0]) + int(p[2]):
                    score += 1
                    break
                else:
                    print('EEE')
                    tries+=1
                if tries == 3:
                    print(problem + str(int(p[0]) + int(p[2])))
                    break     
    print('Score: ' + str(score))

def get_level():
    while True:
        level = input('Level: ')
        if level.isnumeric():
            if int(level) > 0:
                break
    return int(level)

def generate_integer(level):
    return random.choice(range(pow(10,level-1), pow(10,level)))

if __name__ == '__main__':
    main()