# def fib(n):
#     sequence=[]
#     a,b=0,1
#     while a<n:
#         sequence.append(a)
#         a,b=b,a+b
#     return sequence
# res=fib(10)
# print(f"The sequence is :{res}")

import re
# text="My roll number is 42 and 45"
# match=re.search(r"\d+",text)
# print("Match number is ",match.group())

# text="please visit to our website https://www.mahesh.patil"
# pattern=re.search(r"https?://[^\s]+",text)
# if pattern:
#     print("Extracted website name is ",pattern.group())

x=[12,2,3,4,5,6]
y=[14,3,4,"Mahesh"]
x.extend(y)
# print(x)
x.extend("Mahesh")
# print(x)
# print(x.insert(0,45))
# print(x)
# print(x.pop(1))



# s={1,2,3,4,5}
# print(type(s))
# s.add(10)
# s.add(14,15,17,87)
# print(s)
# s.update(45)
# s.update(range(12))
# print(s)
# print(1 in s)
# print(5 not in s)
# print(s[2])\
# print(s[1:4])



# word=input("Enter the word : ")
# vowels={'a',"e","i","o","u"}
# res=set(word)
# final=res.intersection(word)
# print(f"The number of vowels present in {word} are {final}")



student = {
    "name": "John",
    "age": 25,
    "courses": ["Math", "CS"]
}
# print(student.keys())
# for key in student:
#     print(f"keys are :{key}")
# for k in student.keys():
#     print(f"keys :{k}")

# for k,v in student.items():
#     print(f"  {k} : {v}")


# word=input("Enter the word : ")
# d={}
# for i in word:
#     d[i]=d.get(i,0)+1
# print(d)

# s={i: i for i in range((15))}
# print(s)



# def is_even(n):
#     if n%2==0:
#         print("Even number")
#     else:
#         print("Odd")
# print(is_even(12))