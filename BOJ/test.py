
def first_person(n):
    answer = []

    for i in range(n):
        if (i + 1) % 5 == 1:
            answer.append(1)
        elif (i + 1) % 5 == 2:
            answer.append(2)
        elif (i + 1) % 5 == 3:
            answer.append(3)

        elif (i + 1) % 5 == 4:
            answer.append(4)
        elif (i + 1) % 5 == 0:
            answer.append(5)

    return answer

def second_person(n):
    answers = [2 for _ in range(10000)]
    for i in range(1,10000,8):
        answers[i]=1

    for i in range(3,10000,8):
        answers[i]=3

    for i in range(5,10000,8):
        answers[i]=4

    for i in range(7,10000,8):
        answers[i]=5

    return answers[:n]

def third_person(n):
    answers = [0 for _ in range(10000)]

    for i in range(0,10000,10):
        answers[i] = 3
        answers[i+1] =3

    for i in range(2,10000,10):
        answers[i] =1
        answers[i+1]=1

    for i in range(4,10000,10):
        answers[i]=2
        answers[i+1]=2

    for i in range(6,10000,10):
        answers[i]=4
        answers[i+1]=4

    for i in range(8,10000,10):
        answers[i]=5
        answers[i+1]=5


    return answers[:n]





def solution(answers):
    answer = []
    n = len(answers)
    first_answer = first_person(n)
    second_answer = second_person(n)
    third_answer = third_person(n)

    count_1 = 0
    count_2 = 0
    count_3 = 0

    for val,ans in zip(first_answer,answers):
        if val==ans:
            count_1+=1

    for val,ans in zip(second_answer,answers):
        if val==ans:
            count_2+=1

    for val,ans in zip(third_answer,answers):
        if val==ans:
            count_3+=1


    answer_temp = [count_1,count_2,count_3]

    for person, score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(person+1)

    return answer
