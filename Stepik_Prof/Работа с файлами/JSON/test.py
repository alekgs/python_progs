import json

# lines = {
#          True: 97,
#          2: "I've been running for a reason",
#          "3": ("I", "could", "never", "retain"),
#          4: ["Sweet", "lips", "like", "pink", "lemonade"],
#          5.0: "When he's feeling generous he's gonna give me a taste",
#          "six": "10"
#         }
#
# lines_json = json.dumps(lines)
#
# lines = json.loads(lines_json)
# print(lines)
#
# weekdays = {i: day for i, day in enumerate(['Sunday', 'Monday', 'Tuesday'])}
# weekdays_json = json.dumps(weekdays, separators=('; ', '-'))
# print(weekdays_json)

# numbers = {2: 'two', 1: 'one', 4: 'four', 3: 'three'}
# numbers_json = json.dumps(numbers, sort_keys=True)
# print(numbers_json)

data = {('Timur', 'Guev'): 'BEEGEEK', ('Roman', 'Belyh'): 'IQ-option'}
data_json = json.dumps(data)
print(data_json)


