import songs as s
import platform

if(platform.system()=='Windows'):
    f = open('C:\\Users\\user\\Desktop\\important\\machine learning files\\csv\\music\\songDb.tsv', 'r')

else:
    f = open('/home/arnamaity/Hackathons/Music-recommendation-system/spotify-music-genre-list/songDb.tsv','r',encoding="ISO-8859-1")

y = f.read().splitlines()
count = []
for i in range(len(y)):
    if (i % 2 == 0):
        count.append(y[i].split('\t'))

d = []
e = 0
f = []
for i in range(len(count)):
    d.append(count[i][-1])

i = 1
j = i + 1

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
# LABEL ENCODING
try:
    while (i != len(d)):

        while (d[i] == d[j]):
            e += 1
            i += 1
            j += 1
        f.append(e)
        i += 1
        j += 1
        e = 0
except IndexError:
    pass
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
g = []
t = 0
for i, j in zip(f, range(len(f))):
    t = i
    while (t != 0):
        g.append(j)
        t -= 1
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------'


'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
# MODEL

p = []
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=19,max_depth=2)
X_train = [count[i][1:11] for i in range(1, len(count))][:92106]
y_train = g[:92106]
X_test = s.function()
model.fit(X_train, y_train)
#print(model.score(X_train,y_train))
p.append(model.predict(X_test))
print(p)
p[0].sort()

#print('GETTING YOUR RECOMMENDATION....')
'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
def fa(x):
    for i in range(len(g)):
        if (g[i] == x):
            return g[i]


'------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
# DICTIONARY
dictionary = dict(zip(g, d))
#print(dictionary)
#print(dictionary[fa(p[0])])

'------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
#RETRIEVING THE NAMES BASED ON GENRE AND DURATION IN MS
i=0
seu=[]
try:
    for j in f:
        if(dictionary[fa(p[0])] == count[i][-1] ):
            while(i!=j+1):
                v=float(count[i][-3])
                seu.append(v)
                i+=1
            break
        else:
            i+=j
except IndexError:
    pass


seu.sort()

try:

    for i in range(1,len(count)):
        if(str(seu[-i])==count[i][-3]):
            print(count[i][0])
except IndexError:
    pass
'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
