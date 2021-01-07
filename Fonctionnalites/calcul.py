from Fonctionnalites.speak import speak


def calculate(question):
    try:
        if "x" in question:
            question = question.replace("x", "*")
        num = ""
        for i in range(len(question)):
            if (question[i].isdigit()) or ("*" == question[i]) or ("/" == question[i]) or ("-" == question[i]) or ("+" == question[i]):
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
