import numpy as np
x=np.array([1.0,2.0,3.0])
y=np.array([2.0,4.1,5.9])
w,lr=0.0,0.1s
print("Step w-value Gradient")
for step in range(1,53):
    grad=2*np.mean(x*(w*x-y))
    w-=lr*grad
    if step in (1,2,3,10,50,52):
        print(step,round(w,4),round(np.mean((w*x-y)**2),4))