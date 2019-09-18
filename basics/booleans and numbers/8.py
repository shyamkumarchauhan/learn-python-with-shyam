print("Enter the value: ");
x = input();
try:
   if "." in x :
     y = float(x)
     z = abs(y)
     if (y == z):
         print ("True");
     else:
         print ("False");
   else:
      y = int(x)
      z = abs(y)
      if (y == z):
          print ("True");
      else:
          print ("False");
except ValueError:
   print("No.. the input value is not a number. It's a string")
