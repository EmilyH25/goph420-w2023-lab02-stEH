

vel_list = []
for i in range (len(frequencies)):
    small_list = []
    for t in range (len(zeta_list[i])):
        cl = (1/((1/1900)**2-((zeta_list[i][t])/4000)**2))**(0.5)
        small_list.append(cl)
    vel_list.append(small_list)
