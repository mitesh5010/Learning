# print('mitesh prajapati')

# a = 'mitesh'
# print(a[::-1])

# print(input("age"))

# if 10>5:
#   print("sdjfb")
# a = int(input('age'))
# if a>50:
#   print(f'old{a}')
# elif a<18:
#   print('child')
# else :
#   print('sdnfk')

# a = range(1,21,1)
# for i in a:
#   print(i)

# for i in range(21):
#   print(i)

# a = "Mitesh"
# for i in range(len(a)):
#   print(a[i])

# a= "ndjf"
# for i in a:
#   print(i)

# for i in range(20):
#   if i==10:
#     continue
#   else:
#     print(i)

# even= 0
# odd=0
# for i in range(10):
#   print(i)
#   if i%2==0:
#     even+=1
#   else:
#     odd+=1

# print(f"count {even},{odd}")

# a=5
# while a<10:
#   print(a)
#   a+=1


# s = "mitesh"
# a =''
# for i in range(len(s)-1, -1,-1):
#   print(i)
#   a = a+s[i]
#   print(a)
# print(a)


# help(dict)

# a = [1,1,1,1,2,2,2,3,3,4,4,4,4,5,5,5,6]
# d = {}
# for i in a:
#   if i in d.keys():
#     d[i] +=1
#   else: 
#     d[i] =1
# print(d)

# d1 = { 10: 100}
# d2 = {20:200}

# for i in d2:
#   if i in d1.keys():
#     d1[i] += d2[i]
#   else:
#     d1[i] = d2[i]

# print(d1, d2)


# r = open('super.txt', 'a')
# r.write('just doing practice')
# r.close()

# class

# class Factory:
#   def __init__(self, meterial, pockets):
#     print(self)
#     self.meterial = meterial
#     self.p = pockets
#     print("initilaized")
#   def show(self):
#     print(f"{self.p}")
  
# reebok = Factory("cutton",5)
# nike = Factory("k",4)

# nike.show()


# inheritnace
# class Factory:  #super class/ parent class
#   a = "attribute in factory"
#   def hello(self):
#     print("method in factory")
  

# class FactoryAnand(Factory): #sub calss/ child class
#   pass

# obj = FactoryAnand()

# obj.hello()

# dender method
# class Animal:
#   def __init__(self, name):
#     self.name = name

#   def __str__(self):  #use as print 
#     return f"how are you {self.name}"
  
# obj =Animal("lion")
# print(obj)

