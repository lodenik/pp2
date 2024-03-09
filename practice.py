# d=[
#     {
#         "name":"Asd1",
#         "age": 18
#     },
#     {
#         "name": "Asd2",
#         "age": 18
#     },
#     {
#         "name": "Asd3",
#         "age": 20
#     },
#     {
#         "name": "Asd4",
#         "age": 19
#     }
# ]

# def avg_age(people):
#     return sum([x["age"] for x in d]) / len(d)

# print(avg_age(d))

# _______________________________________________________

from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(5)
print(current_date)
print(five_days_ago)

