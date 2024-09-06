f = open("allstudents.txt", "r")
data = f.read()

students = data.split("\n")

names = open("7th.txt", "r")
data = names.read()

cartagged_list = data.split('\n')
counter = 0

with open("propernames.txt", "w") as file:
    for i in students:
        l = i.split('\t')
        for j in cartagged_list:
            
            m = j.split('\t')
            if l[1] == m[-1]:
                file.write('\t'.join(l[:2]) +  "\t" + ' '.join(m[:2])+ "\t" + '\t'.join(l[3:]) + "\n")
                break

        else:
            file.write(i + "\n")