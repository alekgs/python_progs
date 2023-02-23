# import nums_from_string
import re

s = "Extract100,100.45and10000from677878787687this2345string7885656"
# print(nums_from_string.get_nums(s))
nums = re.findall(r'\d*\.\d+|\d+', s)
nums = [float(i) for i in nums]
print(nums)
