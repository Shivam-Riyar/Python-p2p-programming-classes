# PROGRAM TO FIND AREA OF TRIANGLE
h = float(input("ENTER HEIGHT OF THE TRIANGLE : "))
b = float(input("ENTER BASE OF THE TRIANGLE : "))
area = 0.5 * h * b
print("AREA OF THE TRIANGLE IS : ",area)

# OR BY USING HERON'S FORMULA
a = float(input("ENTER FIRST SIDE OF THE TRIANGLE : "))
b = float(input("ENTER SECOND SIDE OF THE TRIANGLE : "))
c = float(input("ENTER THIRD SIDE OF THE TRIANGLE : "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**0.5
print("AREA OF THE TRIANGLE IS : ",area)
