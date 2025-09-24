class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # edge case 
        if numerator == 0:
            return "0"
        
        fraction = []
        # handle negative sign
        if (numerator < 0) ^ (denominator < 0): # check for opposite signs
            fraction.append("-")
        
        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend//divisor))
        rem =  dividend % divisor 
        
        # no decimal, return 
        if rem == 0:
            return "".join(fraction)
        
        # otherwise, fractional part 
        fraction.append(".")
        store={} # detect cycles
        while rem != 0:
            if rem in store:
                # start
                fraction.insert(store[rem], "(")
                # end
                fraction.append(")")
                break
            store[rem] =  len(fraction)
            rem = rem*10
            fraction.append(str(rem // divisor))
            rem = rem % divisor
        
        return "".join(fraction) # final integer