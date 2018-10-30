def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num

print(bubble_sort([111,22,3333,4,5]))