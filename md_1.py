# def func(s):
#     for sq in set(s):
#
#         count = 0
#         for sub in s:
#             if sq == sub:
#                 count += 1
#         print(f'{sq} - {count}')
#
#
# func('qdw2d222')
# def strcounter(s):
#     sym_dict = {}
#     for sym in s:
#         sym_dict[sym] = 1 + sym_dict.get(sym, 0)
#
#     for sym, count, in sym_dict.items():
#         print(f'{sym} - {count}')
#
#
# strcounter('qdw2d222')


# def strcounter(s):
#     for sym in set(s):
#         print(f'{sym} - {s.count(sym)}')

# strcounter('qdw2d222')


s = input()
h = len(s) // 2
print(s[:h] == s[:len(s)-h-1:-1])

# Проверяем, равна ли первая строка половине второй, записанной в обратном порядке.
# При условии, что в строке нечётное количество символов, тогда средний символ не участвует в проверке, поскольку не влияет на результат.
