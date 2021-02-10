# name = "JEROEN"
name = "JAN"
# name = "JAZ"

count=0
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d={}
indexes=[]
current_idx=0
n=len(name)
for i in range(len(alpha)):
    d[alpha[i]] = min(i,26-i)
    # print(d)
    # print(min(i,26-i))
#print(d)
for i in range(n):
    num=d[name[i]]
    # print(num)
    count+=num
    if num !=0 :
        indexes.append(i)
        print(indexes)

while True:
    if len(indexes)==0:
        break
    min_dist=99
    min_idx=0
    for it in indexes:
        print("it: %s" %it)
        min_dist2=min(abs(it-current_idx),n-abs(it-current_idx))
        print("min_dist2 %s" % min_dist2)
        if min_dist2 < min_dist:
            min_dist=min_dist2
            min_idx=it
    count += min_dist
    indexes.remove(min_idx)
    current_idx = min_idx

print(count)

