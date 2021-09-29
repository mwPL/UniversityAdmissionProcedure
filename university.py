depts = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
applicants = []
file = open('/Users/mw/Downloads/applicant_list_7.txt', 'r')
for line in file:
    applicants.append(line.split())
for i in applicants:
    i[2] = float(i[2])
    i[3] = float(i[3])
    i[4] = float(i[4])
    i[5] = float(i[5])
    i[6] = float(i[6])
    i.append((float(i[4])+float(i[2]))/2)  # Physics [10]
    i.append((float(i[4])+float(i[5]))/2)  # Engineering [11]
    i.append((float(i[3])+float(i[2]))/2)  # Biotech [12]
    i.append(float(0.0)) # Max field [13]
applicants.sort(key=lambda a: (-(a[10]), a[6], a[0], a[1]))


def org(dept):
    if dept == 'Biotech':
        for i in applicants:
            i[13] = max(i[12], i[6])
    elif dept == 'Chemistry':
        for i in applicants:
            i[13] = max(i[3], i[6])
    elif dept == 'Engineering':
        for i in applicants:
            i[13] = max(i[11], i[6])
    elif dept == 'Mathematics':
        for i in applicants:
            i[13] = max(i[4], i[6])
    else:
        for i in applicants:
            i[13] = max(i[10], i[6])

'''
org('Biotech')
applicants.sort(key=lambda a: (-a[13], a[7], a[0], a[1]))

for x in applicants:
    print(x)
'''
# org('Physics')
# applicants.sort(key=lambda a: (-a[13], a[7], a[0], a[1]))
# for x in applicants:
#      print(x)
# exit()

limit = int(input())

for priority in range(7, 10):
    toremove = []
    org('Physics')
    applicants.sort(key=lambda a: (-a[13], a[7], a[0], a[1]))
    for i in applicants:
        if i[priority] == 'Physics' and len(depts['Physics']) < limit:
            depts['Physics'].append(i)
            toremove.append(i)
    for i in toremove:
        # print(f'***Removed {i}')
        applicants.remove(i)

    org('Chemistry')
    applicants.sort(key=lambda a: (-(a[13]), a[priority], a[0], a[1]))
    toremove = []
    for i in applicants:
        if i[priority] == 'Chemistry' and len(depts['Chemistry']) < limit:
            depts['Chemistry'].append(i)
            toremove.append(i)
    for i in toremove:
        # print(f'***Removed {i}')
        applicants.remove(i)

    org('Biotech')
    applicants.sort(key=lambda a: (-(a[13]), a[priority], a[0], a[1]))
    toremove = []
    for i in applicants:
        if i[priority] == 'Biotech' and len(depts['Biotech']) < limit:
            depts['Biotech'].append(i)
            toremove.append(i)
    for i in toremove:
        # print(f'***Removed {i}')
        applicants.remove(i)

    org('Mathematics')
    applicants.sort(key=lambda a: (-(a[13]), a[priority], a[0], a[1]))
    toremove = []
    for i in applicants:
        if i[priority] == 'Mathematics' and len(depts['Mathematics']) < limit:
            depts['Mathematics'].append(i)
            toremove.append(i)
    for i in toremove:
        # print(f'***Removed {i}')
        applicants.remove(i)

    org('Engineering')
    applicants.sort(key=lambda a: (-(a[13]), a[priority], a[0], a[1]))
    toremove = []
    for i in applicants:
        if i[priority] == 'Engineering' and len(depts['Engineering']) < limit:
            depts['Engineering'].append(i)
            toremove.append(i)
    for i in toremove:
        # print(f'***Removed {i}')
        applicants.remove(i)

for k, v in depts.items():
    v.sort(key=lambda a: (-float(a[13]), a[0], a[1]))

for k, v in depts.items():
    file = open(k.lower()+".txt", "w")
    for i in v:
        file.write(f'{i[0]} {i[1]} {float(i[13])}\n')
    file.close()
