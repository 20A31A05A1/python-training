class clg:
    name="pragati"
    dep="all"
    loc="surampalem"
    roll="pgcet"
class faculty(clg):
    name="Rajesh"
    pos="hod"
    dep="cse"
    loc="surampalem"
    roll="5q1"
class studnt(clg):
    roll="20a31a05b2"
    dep="civil"
obj1=studnt()
obj2=faculty()
print(obj1.name)
print(obj2.roll)
print(obj1.dep)
print(obj2.loc)

    
