# while True:
#     try:
#         x = int(input('Please enter a number: '))
#         print(5 / x)
#         break

#     except ValueError:
#         print('Ooops! Try again..')

#     except ZeroDivisionError:
#         print('Can not divide with 0. Try different number')

#     except (ValueError, ZeroDivisionError):
#         print('Invalid number')


text = input()

try:
    number = int(input())
    print(text * number)
except ValueError:
    print('Variable times must be an integer')

finally:
    print('No matter what just print it')