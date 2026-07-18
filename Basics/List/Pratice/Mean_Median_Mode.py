import statistics as st
l1 = [1,5,3,4,6,7,8]
l2 = [1,5,3,4,6,7,8,9]

#Mean = 1+5+3+4+6+7+8=34/7=4.857

sum = 0
for item in l1:
    sum += item
print(f'Mean of {l1} is {sum/len(l1)}')

#Median is either the middle value (if length is odd) or average of (length//2 and length//2-1)

l1.sort()
l2.sort()
print(f'Median of {l1} is {l1[len(l1)//2]}')
print(f'Median of {l2} is {(l2[len(l2)//2] + l2[(len(l2)//2)-1])/2}')

print()
print()

print(f'Mean of {l1} is {st.mean(l1)}')
print(f'Median of {l1} is {st.median(l1)}')
print(f'Median of {l2} is {st.median(l2)}')
print(f'Mode of {l1} is {st.mode(l1)}')
print(f'Mode of {l2} is {st.mode(l2)}')