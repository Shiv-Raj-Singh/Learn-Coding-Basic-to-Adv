# from functools import wraps
# def decorator_function(any_funcgtion ):
#     @wraps(any_funcgtion)
#     def function1(*args, **kwargs):
#         return "mangal is not a don while he s a good person"
#         any_funcgtion(*args, **kwargs)
    # return function1
# functi=fecorator_function
# print(fecorator_function(a))
# print(functi())

# @fecorator_function

# def func(a,b):
    # return a+b
        # print('maangal is don' )
# print(func(3,4))       
# func=fecorator_function(func)
# func()

# # def decorater(a_func):
#     def function():
#         print("its a function whuch is modified by decoter function")
#         a_func
#     return function
# # @decorater
# def func():
#     return "its a simple function"
# # func()
# print(func())
# func=decorater(func)

#                                find the power of any numbers
# def to_power(x):
#     def number(n):
#         return n**x
#     return number
# num =to_power(2)
# print(num(5))

# from functools import wraps
# def decorater_function(any_function):
#     @wraps(any_function)
#     def function1(*args, **kwargs):
#         print("it's a decorater function")
#         """its a simple decorater function"""
#         return any_function(*args, **kwargs)
#     return function1


# @decorater_function
# def func(a,b):
#     print(f'its a function with arguments{a},{b}')
#     return a+b
    
# # print(func(9,4))
# # # print(add.__doc__)
# # print(func.__doc__)
# # from time import time

# # import time
# # t1=time.time()
# # def func():
# #     ''' its a simple function '''
# #     print("its a func ")
# # func()
# # print(func.__doc__)
# # t2=time.time()
# # total = t2-t1
# # print(total)

# # CALCULATE TIME OF A DECORATO FUNCTI

# from functools import wraps
# import time
# def calculate_time(function):
#     @wraps(function)
#     def function_1(*args, **kwargs):
#         print(f"exicuting func ----{function.__name__}")
#         t1=time.time()
#         return_value=function(*args, **kwargs)
#         t2=time.time()
#         total =t2-t1
#         print(f"the function took {total} seconds ")
#     return function_1
# @calculate_time
# def func(n):
#     x= [a**2 for a in range(1, n+1)]
#     print(x)
# func(100)
    
from re import X


def decorator_func(any_function):
    def function1(*args, **kwargs):
        return " mangal is don "
    
        return any_function(*args, **kwargs)
    return function1


@decorator_func
def func():
    print('hello')
x=func(3,4)
decorator_func=func()

print(func(x))