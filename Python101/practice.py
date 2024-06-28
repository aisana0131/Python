all = {'instructors': ['Ahmad', 'Abdul', 'Kris', 'Gulnaz', 'Esen'], 'members': ["Abdulhamid Abdullajonov", "Ahmadyar", "Aiya", "Esenbek", "Gulnaz", "Kris", "Marlen", "Meerim", "Mohammad", "Salmon", "Simon"]}

both = []


for person in range(len(all['instructors'])):
    inst = all['instructors'][person]
    if inst != all['members']:
        both.append(inst)


print(both)