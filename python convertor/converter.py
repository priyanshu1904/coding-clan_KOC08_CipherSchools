def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
str = str(input("ENTER A ROMAN NUMBER: "))
def romanToDecimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        # Getting value of symbol s[i]
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res
 
# Driver code
print("Integer form of Roman Numeral is"),
print(romanToDecimal(str))

#  PROGRAMME TO COVERT NUMBER TO ROMAN NUMERALS
# Function to convert integer to Roman values
def roman_numbers(num):
    if num > 3999:
        print('enter number less than 3999!')
        return
    value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol=['M','CM','D','XD','C','XD','L','XL','X','IX','V','VI','I']
    roman=''
    i=0
    while num>0:
        div = num//value[i]
        num = num%value[i]
        while div:
            roman = roman+symbol[i]
            div = div-1
        i=i+1
    return roman
num = int(input("enter an integer number:"))
print("roman numerals of",num,"is:",roman_numbers(num))