ordbog = {'hun':'she','han':'he', 'god morgen':'good morning'}
mereInput = True

print("Skriv q, når du er færdig med ordbogen. ")
while mereInput:
    dansk = input("Indtast dansk ord: ")
    if dansk == 'q':
        mereInput = False
    elif dansk in ordbog.keys():
        print(dansk.title() + " ---> " + ordbog[dansk].title())
    else:
        print(dansk + " Findes ikke i ordbogen!")



