def distribute_electrons(electrons):
    shells = []
    n = 1  # Номер на текущата обвивка

    while electrons > 0:
        # Формулата 2n^2
        max_capacity = 2 * (n ** 2)

        if electrons >= max_capacity:  # 64  8
            # Запълваме обвивката максимално
            shells.append(max_capacity)  # 8
            electrons -= max_capacity    # 64-8
        else:
            # Слагаме остатъка и приключваме
            shells.append(electrons)
            electrons = 0

        n += 1  # Преминаваме към следващата обвивка

    return shells
electrons_input = int(input())
print(distribute_electrons(electrons_input))