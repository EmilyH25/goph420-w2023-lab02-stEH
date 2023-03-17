
wave_list = []
for i in range (len(frequencies)):
    small_list = []
    for t in range (len(vel_list[i])):
        wave = (vel_list[i][t])/frequencies[i]
        small_list.append(wave)
    wave_list.append(small_list)