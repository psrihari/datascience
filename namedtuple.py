from collections import namedtuple

# declarin named tuple
nt=namedtuple('Stu',['name','age','DOB'])

# Adding values
s=nt('Murugan','19','2541997')

print(s[0])