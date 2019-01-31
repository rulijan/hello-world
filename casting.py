number_1 = input('enter 1-st number: ')
number_2 = input('enter 2-nd number: ')
if number_1.isdigit():
   if number_2.isdigit():
       sum = int(number_2) + int(number_1)
       print(number_1,"+",number_2,"=",sum)
   else:
       print(number_2," is'nt a digit")
else:
     print(number_1," is'nt a digit")
print("Good")



