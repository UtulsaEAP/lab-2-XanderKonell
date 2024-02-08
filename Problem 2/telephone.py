def telephone():

    ''' Type your code here. '''
    phone_number = int((input()))

    area_code = phone_number // 10000000
    
    prefix = (phone_number % 10000000) // 10000
    
    line_number = phone_number % 10000

    output = f"({area_code}) {prefix:3}-{line_number:4}"

    print(output)
    
if __name__ == "__main__":
    telephone()