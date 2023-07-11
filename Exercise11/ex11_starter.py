#!/usr/bin/python
# string named Belgium
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# print hyphens length of string
print('-' * len(Belgium))
# printed colons instead of commas
print(Belgium.replace(',', ':'))
# i extracted 10445853 converted to int, (8 to 15th)
# x = int(Belgium[8:16])
# i split Belgium into separate fields between commas
fields = Belgium.split(',')
# made second field an int
second_field = int(fields[1])
# made fourth field an int
fourth_field = int(fields[3])
# added ints lines 13 and 15 together
result = second_field + fourth_field
# printed
print(result)