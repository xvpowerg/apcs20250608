import a.b.A
from a.c import A
import a.c.B as B
print(a.b.A.name)
print(A.name)
print(B.name)
a.b.A.show()
A.show()
B.show()
