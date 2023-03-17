
zeta_list = []
for i in range (len(frequencies)):
    small_list = []
    for t in range (len(list[i])):
        zet, iter, error = root_newton_raphson(list[i][t],frequencies[i],f,dfdx)
        small_list.append(zet)
    zeta_list.append(small_list)