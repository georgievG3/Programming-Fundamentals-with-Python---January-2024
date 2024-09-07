# def valid_ticket(token):
#     if len(token) == 20:
#         return True
#     return False
#
#
# def first_half_match(token):
#     middle_of_token = len(token) / 2
#     symbol_count = 0
#
#     for index in range(int(middle_of_token)):
#         if token[index] in special_symbols:
#             symbol_count += 1
#             if symbol_count >= 6:
#                 return True
#         else:
#             symbol_count = 0
#     return False
#
#
# def second_half_match(token):
#     middle_of_token = len(token) / 2
#     symbol_count = 0
#
#     for index in range(len(token) - 1, int(middle_of_token) - 1, -1):
#         if token[index] in special_symbols:
#             symbol_count += 1
#             if symbol_count >= 6:
#                 return True
#         else:
#             symbol_count = 0
#     return False
#
#
# def first_half_jackpot_match(token):
#     middle_of_token = len(token) / 2
#     symbol_count = 0
#
#     for index in range(int(middle_of_token)):
#         if token[index] in special_symbols:
#             symbol_count += 1
#             if symbol_count == 10:
#                 return True
#         else:
#             symbol_count = 0
#     return False
#
#
# def second_half_jackpot_match(token):
#     middle_of_token = len(token) / 2
#     symbol_count = 0
#
#     for index in range(len(token) - 1, int(middle_of_token) - 1, -1):
#         if token[index] in special_symbols:
#             symbol_count += 1
#             if symbol_count == 10:
#                 return True
#         else:
#             symbol_count = 0
#     return False
#
#
# def winning_ticket(token):
#     if valid_ticket(token) and first_half_match(token) and second_half_match(token):
#         return True
#     return False
#
#
# def jackpot_ticket(token):
#     if valid_ticket(token) and first_half_jackpot_match(token) and second_half_jackpot_match(token):
#         return True
#     return False
#
#
# special_symbols = '@', '#', '$', '^'
# tickets = input().split(", ")
# for ticket in tickets:
#     if jackpot_ticket(ticket):
#         print(ticket)
#     elif winning_ticket(ticket):
#         print(f'ticket "{ticket}" - {}{match_symbol}')
#     elif not valid_ticket(ticket):
#         print("invalid ticket")
#     else:
#         print(f'ticket "{ticket}" - no match"')
