import math
p1,m1 = input("Insert longitude,latitude of 1st point:").split(",")
p2,m2 = input("Insert longitude,latitude of 2nd point:").split(",")
p1 = math.radians(float(p1))
m1 = math.radians(float(m1))
p2 = math.radians(float(p2))
m2 = math.radians(float(m2))

dp = p2-p1
dm = m2-m1

alpha = math.sin((dp/2)**2)+math.cos(p1)*math.cos(p2)*math.sin((dm/2)**2)

R = 6372.8
c = 2*math.asin(math.sqrt(alpha))
dist = R*c

print("Distance in Km:",dist)
