def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(7, 5)
print_params(6, c = 567)
print_params(c='flag', b=789, a=0)

values_list = ['summer', 3, False]
values_dict = {'a': 2024, 'b': True, 'c': 'winter'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['autumn', True]
print_params(*values_list_2, 42)
print_params(42, *values_list_2)
