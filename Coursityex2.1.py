import math

[a,b,g] = input("Παρακαλώ εισάγετε τιμές α,β,γ (χωρισμένες με κόμμα):").split(',')
a = int(a)
b = int(b)
g = int(g)

delta = b*b-4*a*g

if delta > 0:
    delta = math.sqrt(delta)
    x1 = (-b+delta)/(2*a)
    x2 = (-b-delta)/(2*a)
    print("Οι 2 πραγματικές ρίζες είναι:",x1,x2)
elif delta == 0:
    delta = math.sqrt(delta)
    x1 = (-b)/(2*a)
    print("Η μια πραγματική και διπλή ριζα είναι:",x1)
else:
    print("Δεν υπάρχουν πραγματικές ρίζες")
