'''x=[]
for i in range(11):
    ( x.append(i**2))
print(x)'''
                #    by list comprehton
            #   print the squares of numbers (1-10)  
# x=[i**2 for i in range(11)]
# print(x)
                # print the first letter of words which exist in a list 
# x=['mangal','raja','akash'] 
# y=[]
# for i in x:
    # y.append(i[0:3])
# print(y)
# y=[i[0] for i in x ]
# print(x)
# print(y)
                        # print the negative numbers 1-10
# x=[]
# x=[-i for i in range(11) ]
# for i in range(10):
    # x.append(-i)
# print(x)
            # print a reverse string of a list 
# l=['MAN','RAJ','NAMAK' 'MANGAL']
# l1=[i[::-1] for i in l ]
# for i in l:
    # l1.append(i[::-1])
# print(l1)     simple list methd 
                                                    # by a func
# def my_list(l):
    # l1=[]
    # return [i[::-1] for i in l] 
    # for i in l:
        # l1.append(i[::-1])
    # return l1
# x=['MAN','RAJ','NAMAK' 'MANGAL']
# print(my_list(x))
    
    


# def mylist(l):
    # return l1=[i**2 if (i%2==0) for i in l ]
    # return l2(i**3 else )
    # l2=[i**3 (else) for i in l ]
    # for i in l:
        # if i%2==0:
        #   l1.append(i**2)
        # else:
            # l2.append(i**3)
    # return l3=[l1,l2]
    # return l3
# x=[1,2,3,4,5,6,7,8,9]
# print(mylist(x))
        
# def mylist(l):
    # l1_for_str=[]
    # for i in l:
        # if 'A' in i:
            # l1_for_str.append(i)
    # return l1_for_str
# x=['MANGAL', 'AKASH','DINKAR','PREET','PUNEET','YOGANDRA']
# print(mylist(x))
            # print multi list in a list by list comp
# def my_list(l):
    # new_list=[]
    # for i in l:
        # for j in i:
        # new_list.append(i)
    # return new_list
# x=[[1,2,3],[4,5,6],[7,5,1,3]]
# # print(my_list(x))
# new_list=[i for i in range(1,4) for j in range(3)]
# print(new_list)
# for i in range(3):
    # new_list.append(i)
# print(new_list)


        
        
        
        