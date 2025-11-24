print("Aayushi Tanwar","25BCE11275")
print("select operation: \n1.Add \n2.Subtract \n3.Mutiply \n4.Divide  \n5.Square root \n6.power \n7.Sin value \n8.Cos value \n9.Tan value \n10.End ")

while True:
  ch=input("Choose operation (1/2/3/4/5/6/7/8/9/10)")
  if ch=='10':
    print("END")
    break
  if ch in ['1','2','3','4','5','6','7','8','9']:
      a=int(input("Enter first number"))
      b=int(input("Enter second number"))
      if ch=='1':
       sum=a+b
       print("Sum of a and b=",sum)
      elif ch=='2':
       diff=a-b
       print("Difference of a and b=",diff)
      elif ch=='3':
       pro=a*b
       print("productof a and b=",pro)
      elif ch=='4':
       quot=a/b
       rem=a%b
       print("quotient of a and b=",quot)
       print("remainder of a and b=",rem)
      elif ch=='5':
        sq_rt=a**(0.5)
        print("Square root of a=", sq_rt)

      elif ch=='6':
        powr=a**b
        print("a to the power b=", powr)
      elif ch=='7':
        sin_val=math.sin(a)
        print("Sin value of a=",sin_val)
      elif ch=='8':
        cos_val=math.cos(a)
        print("Cos value of a=",cos_val)
      elif ch=='9':
        tan_val=math.tan(a)
        print("Tan value of b=",tan_val)
