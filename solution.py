s = open("24.txt").readline().strip() #original file: 10 milllion symbols in a row: "ABCDEFGH"
m = 0
k = []
p = []
s = s.replace("E", "A")
for i in s.split("A"):
    if i:
        k.append(len(i)) #appending length of consonants between vowels
    else:
        p.append(k) #lists are divided according to the principle: a new list if there are several vowels in a row in the original file
        k = []
app = []
p = sorted(p, key = len, reverse = True)
for i in p:
    for j in range(len(i)-1):
        for k in range(j+1, len(i)):
            if sum(i[j:k+1]) == ((i[j] + i[k])/2*len(i[j:k+1])):
                app.append([sum(i[j-1:k+2]) + len(i[j-1:k+2])-1, i[j:k+1], i])
print(max(app))
