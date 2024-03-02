n =int(input("enter a number:  "))
inverse =0
while n!= 0:
    inverse = ( inverse * 10 ) + ( n % 10 )
    n = n // 10
print("oposite a number est ;",inverse)
 
