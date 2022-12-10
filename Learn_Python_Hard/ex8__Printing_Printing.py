 
from __future__ import print_function, unicode_literals

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))

print (formatter % ("one", "two", " tree", "four"))

print (formatter % (True,False,True,False))

print ((formatter,formatter,formatter,formatter))
print (formatter % (" This is a paragah first line",
"This is a paragah second line",
"This is a paragah third line",
"This is a paragah fourth line"
))