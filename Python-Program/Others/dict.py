# define a fun of cubes print the dict of cubes that numbers 

'''def cubes_finder(n):
    cube={}
    for i in range(1,n+1):
        cube[i]=i**3
    return cube

    
print(cubes_finder(10))'''
# print(f"{key}={value}")

# count the number of letter in a word 



def letter_count(s):
    count={}
    for i in s:
        count[i]=s.count(i)
    return count
print(letter_count("mangal don"))

# takes data from user print a dict 

# dic={}
# nam=input("enter a name :")
# age=input("enter your age :")
# fav_movies=input("enter your fav movies").split(",")
# fav_songs=input("enter your fav songs:").split(",")

# dic["name"]=nam
# dic['age']=age
# dic['fav_movies']=fav_movies
# dic['fav_songs']=fav_songs
# print(dic)
# for key, value in dic.items():
    # print(f"{key} : {value}")
    
    # set ......
# s2={1,2,2,3,3,4,5}
# s1={1,5,6,7,8,9,2,3}
# s=s1&s2 for interaction 
# s=s1|s2 joint both sets 
# print(s)

# def dic(d):
#     d1={}
#     for i in range(1,d+1):
#         d1[i]=i**2
#     return d1
# print(dic(10))for key , value in d1.items():
# print(f'{key} :{value}')

x=[1,1,2,3,4,4,4,5,6,7,7,7,9]
def count_num_in_list(l1):
    count={}
    for i in l1:
        # count[i]=l1.count(i)
        count[i]=l1.count(i)
    print(count)
count_num_in_list(x)