def addBinary(self, a: str, b: str) -> str:
    #Step 1: To solve this problem, we first convert each string a and b to decimals
    #Step 2: We add the decimals
    #Step 3: Then convert to binary to get the equivalent
    
    #Using int(n,2): Pass the number, and then specify the base for operation
    converted_a =  int(a,2)
    converted_b = int(b,2)
    #Add the converted values (which are decimals)
    sum_of_binaries = converted_a + converted_b
    
    #Convert back to decimals and handle the case for "0b"
    return bin(sum_of_binaries).replace("0b","")