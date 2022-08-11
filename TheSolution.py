def main2(letter):
    a='qwertyuiopasdfghjklzxcvbnm1234567890'
    arr=[]
    for i in a:
        arr.append(i)
    arr1=[]
    for i in letter:
        arr1.append(i)
    for i in arr1:
        for j in arr:
            if j==i:
                arr.remove(j)
    print(arr)
main2('qwer1234')
