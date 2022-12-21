tabby_cat = "\tI'm tabbed in. "
persian_cat = "I'm split\non a line"
backslach_cat = "I'am \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslach_cat)
print (fat_cat)


while True:
   for i in ["/","-","|","\\","|"]:
       print  ("%s\r" % i,)
