# Python Program - To know student passed or failed
print("Enter name of student: ");
name = input();
print("Enter marks scored: ");
mark = input();
r = range (0,100)
if (int(mark) in r ):
    if(int(mark) >= 35):
      print(name , "has passed the exam.");
      print ("Congratulations !!");
    else:
        print(name, "has failed the exam.");
        print ("Better Luck Next Time !!");
else:
     print ("Enter a valid number: ");
   