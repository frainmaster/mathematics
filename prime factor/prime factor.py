num = 1
while(num != 0):
    print("put a positive integer to break it down to its prime factors")
    num = input()
    if str(num).isdigit() and str(num)[0] != "-":
        num = int(num)
        i = 2
        fact = []
        while (i<=num):
            if(num%i==0):
                num /= i
                fact.append(i)
            else:
                i += 1
        print(str(fact)[1:len(str(fact))-1] + '\n')
    else:
        print('number is not a positive integer' + '\n')
