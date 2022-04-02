def Rosenbrock(x_1, x_2):
    f = 100*(x_2 - (x_1)**2)**2 + (1 - x_1)**2
    return f

f_list = []
f_0 = Rosenbrock(-1.2, 0)
f_list.append(f_0)
f_1 = Rosenbrock(0.7319, 0.5176)
f_list.append(f_1)
f_2 = Rosenbrock(-0.00995, -0.57775)
f_list.append(f_2)
f_r = Rosenbrock(1.922, -0.0602)
f_ce = Rosenbrock(-0.00995, -0.57775)
f_list.sort()
results = " f1 = {},\n f2 = {},\n f3 = {},\n fr = {}, \n fce = {}"
print(results.format(f_list[0], f_list[1], f_list[2], f_r, f_ce))
