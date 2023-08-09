mrs = ["kuga","agito","ryuki","555","blade","hibiki","kabuto","den-o","kiba","DCD"]
mrs2 = mrs[:5]
print(len(mrs))

#(1) 10 (2) 5 (3) 4 (4)エラーになる 

a = list()
b = ["100","200","300"]
c = [i*2 for i in b]
a.append(c)
a.append(b)
for i in a:
    if i == "100":
        print("FIND",end="")

#(1) FIND (2) FINDFIND (3) 何も表示されない (4)エラーになる 

a = "She said,\"He" + 3 * "y" + "!"
b = "How are you?\" "
print (a, b)

# She said,"HeHeHe! How are you?"
# She said,"HeyHeyHey! How are you?"
# She said,"Hey!y!y! How are you?"
# She said,"Heyyy! How are you?"

Zen = 'SimpleIsBetterThanComplex'
Zen[:]
Zen[1000:]
Zen[5:1000]
#Zen[0] = 'J'
Zen[:1000] + 'J'

a = [1, 2, 3]
b = [3, 4, 5]
a.extend(b)
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[-3] = a[-3] * -1
print(sum(a))