f1=open("aru.txt","r");
f2=open("demo.txt","w");
for i in f1:
    f2.write(i)
f1.close()
f2.close()