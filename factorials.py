"""
 A small practice a i made for a task  , 
 the program works under the definition of 'n! = n * ( n - 1)!'
 returning the result of a given number

  FOR EXAMPLE : 5! = 5 * 4 * 3 * 2 * 1 
"""

def factorial(n):
    # recursivity
    result = 1
    for element in range (1,n+1):
        result = result * element
        print(result)
        #the print statement exist here only for debug purposes
    return result

def run():
    given_number=int(input("Enter the number to calculate its factorial: "))
    calculator=factorial(given_number)
    print(calculator)

if __name__=="__main__":
    run()

