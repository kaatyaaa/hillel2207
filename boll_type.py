comparison_result: bool = 3 != 5
print(comparison_result)

comparison_result: bool = 5 == 5
print(comparison_result)

comparison_result: bool = 5 <= 5
print(comparison_result)

comparison_result: bool = 5 >= 5
print(comparison_result)

method = True or False
print(f"{method=}")

method_2 = True and True
print(f"{method_2=}")

method_3 = True or True or False            #true true false = true
print(f"{method_3=}")

logical_negation = not False
print(logical_negation)

logical_negation = not not not False
print(logical_negation)

a = None
b = 7
print(a != b)

c = 10 - 1
d = ""
print(c != d)