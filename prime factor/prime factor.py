num = 1
while(num != 0):
    print("put a number to break it down to its prime factors")
    num = int(input())
    i = 2
    fact = []
    while (i<=num):
        if(num%i==0):
            num /= i
            fact.append(i)
        else:
            i += 1
    
    print(str(fact)[1:len(str(fact))-1])
