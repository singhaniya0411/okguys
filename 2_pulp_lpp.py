!pip install sympy
import pulp
import matplotlib.pyplot as plt
lpp=pulp.LpProblem("lp",pulp.LpMinimize)
x=pulp.LpVariable("x",lowBound=0)
y=pulp.LpVariable("y",lowBound=0)
lpp+=200*x+500*y
lpp+=x+2*y>=10
lpp+=3*x+4*y<=24
lpp.solve()
plt.plot(x.varValue,y.varValue,"ro",label="OPTIMAL SOLUTION")
p1=[0,5]
p2=[10,0]
xx=[p1[0],p2[0]]
yy=[p1[1],p2[1]]
plt.plot(xx,yy,"ro",linestyle="--")
p3=[0,6]
p4=[8,0]
x=[p3[0],p4[0]]
y=[p3[1],p4[1]]
plt.plot(x,y,"ro",linestyle="--")
plt.fill([0,0,4],[6,5,3],"b")
plt.grid(True)
plt.show()

