# nric = input('Enter an NRIC number: ')
# prefix = nric[0]
# if prefix in ['S', 'T', 'F', 'G', 's', 't', 'f', 'g']:

#   if nric[1:8].isdigit:

#     if len(nric) == 9:

#       if nric[8].isalpha:

#           print('NRIC format is valid.')
#       else:
#           print('NRIC format is invalid')
#     else:
#         print('NRIC format is invalid')
#   else:
#       print('NRIC format is invalid')
# else:
#     print('NRIC format is invalid')

nric = input('')
if nric[0] in ['S', 'T', 'F', 'G', 's', 't', 'f', 'g']:
  
  if nric[1:8].isdigit():
    
    if len(nric) == 9:
      
      if nric[8].isalpha():
          
          num1 = int(nric[1])*2
          num2 = int(nric[2])*7
          num3 = int(nric[3])*6
          num4 = int(nric[4])*5
          num5 = int(nric[5])*4
          num6 = int(nric[6])*3
          num7 = int(nric[7])*2
          num_1 = num1+num2+num3+num4+num5+num6+num7
          if nric[0] in ['T','t','G','g']:
               num_1 = num_1 + 4
          else:
              num_1 = num_1
          num_2 = num_1%11
          string1 = 'JZIHGFEDCBA'
          string2 = 'XWUTRQPNMLK'
          last_letter_1 = 'a'
          last_letter_2 = 'a'
          if nric[0] in ['S','s','T','t']:
              last_letter_1 = string1[num_2]
          if nric[0] in ['F','f','G','g']:
              last_letter_2 = string2[num_2]
          if nric[8]==last_letter_1:
               print('NRIC is valid.')
          elif nric[8]==last_letter_2:
              print('NRIC is valid.')
          else:
              print('NRIC is invalid.')
      else:
          print('NRIC is invalid.')
    else:
        print('NRIC is invalid.')
  else:
      print('NRIC is invalid.')
else:
    print('NRIC is invalid.')
          
  
   



  
# Type your code below
