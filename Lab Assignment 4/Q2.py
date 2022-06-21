n=int(input('Enter a Year:'))

if n%4==0:
    
    if n%100==0 and n%400!=0 :
        print('It is not a Leap Year')
    
    else:
        print('It is a Leap Year')

else:
    print('It is not a Leap Year')
