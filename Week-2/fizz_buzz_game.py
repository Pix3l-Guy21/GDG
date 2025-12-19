#Question #7: FizzBuzz

n = int(input("Enter a number n: "))

def play_game(num):
    answer = []
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(i)
    return answer
print(play_game(n))