i = 0;

while(i <= 100):
    divisivel = 0;

    for j in range (1,i+1):
        if i % j == 0:
            divisivel +=1;
    if divisivel == 2:
        print("Numero Primo:", i);
            
    i +=1;
