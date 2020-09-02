# def print_msg(msg):
# # This is the outer enclosing function
#
#     def printer():
# # This is the nested function
#         nonlocal
#         msg=msg*2
#         print(msg)
#
#     printer()
#
# # We execute the function
# # Output: Hello
# print_msg("Hello")
a = 100
def outer_function():
    a = 5
    def inner_function():
        a = 20
        def inner_inner():
            nonlocal a
            print("Inner inner function: ",a)

        inner_inner()
    inner_function()
    print("Outer function: ",a)

outer_function()