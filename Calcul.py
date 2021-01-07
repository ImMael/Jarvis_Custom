from Fonctionnalites.speak import speak


def Calculate(question):
    try:
        if "x" in question:
            question = question.replace("x", "*")
        num = ""
        for i in range(len(question)):
            if ('A' <= question[i] <= 'Z') or ('a' <= question[i] <= 'z'):
                pass
            elif question[i].isdigit():
                num = num + question[i]
            elif '0' >= question[i] <= '9':
                num = num + question[i]
            else:
                pass
            print(num)
        result = eval(num)
        speak(f'Le résultat est : {str(result)}')
        print(f'question : {question}')
        print(f'num : {num}')
        print(f'Le résultat est : {result}')
    except TypeError:
        pass
