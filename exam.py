print('enter number')
N= int(input())   # recieve an integer input
print("enter 'abab' or 'abba' etc equal to {}".format(N))
S=input()                           # recieve a string
counter1=0                             
counter2=0
i=0
j=0
k=0
l=0

list1=list(S)                         # convert string to list for easy changes and sorting 
#we will use two different lists and sort them
#then change them different ways the one with min counter is answer  

list1.sort()
list2=list(S)
list2.sort()


for i in range(0,N-1):
    for j in range(0,N-i-1):
         if list1[j]!=list1[j+1]:
             counter1=counter1+1;
             list1[j+1]=list1[j];
             
         else:
             pass
for k in range(0,N-1):
    for l in range(0,N-k-1):
         if list2[l]!=list2[l+1]:
             counter2=counter2+1;
             list2[l]=list2[l+1];
             
         else:
             pass

if counter1<counter2:
    print(counter1);
else:
    print(counter2)
