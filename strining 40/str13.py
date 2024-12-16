#13-masala
s1=input("String kiriting: ")
belgi=input("Belgini kiriting: ")
count=0
for i in range(len(s1)):
    if s1[i]==belgi:
        count+=1
    print(count)
