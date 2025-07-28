from pathlib import Path
import os

def readFandF():
  path = Path('')
  items = list(path.rglob('*'))
  for i, items in enumerate(items):
    print(f"{i+1}: {items}")


def createFile():
  try:
    readFandF()
    name = input("please enter file name:-")
    p = Path(name)
    if not p.exists() and p.is_file():
      with open(p,'w') as fs:
        data = input("please enter your data:-")
        fs.write(data)
      print("File created Successfully!")
    else:
      print("path is exist...")
  except Exception as err:
    print(f"error occur {err}")
  
def readFile():
  try:
    readFandF()
    name = input("which file do you want to read:-")
    p = Path(name)
    if p.exists() and p.is_file():
      with open(p, 'r') as fs:
        data = fs.read()
        print(f"file data: {data}")
    else:
      print("file dose not exits")
  except Exception as err:
    print(f"an error :{err}")

def updateFile():
  try:
    readFandF()
    name = input("which file do you want to update:-")
    p = Path(name)
    if p.exists() and p.is_file():
        print("1:change file name?")
        print("2:change file Data?")
        print("3:append the file data?")
        res = int(input("enter your choice:-"))

        if res == 1:
          name2 = input("enter new file name:-")
          p2 = Path(name2)
          p.rename(p2)
        elif res==2:
          with open(p,'w') as fs:
            data = input("Enter new data:-")
            fs.write(data)
        elif res==3:
          with open(p,'a') as fs:
            data = input("Enter append data:-")
            fs.write(" "+data)
  except Exception as err:
    print(f"an error:{err}")

def delation():
    try:
      readFandF()
      name = input("which file do you want to update:-")
      p = Path(name)
      if p.exists() and p.is_file():
        os.remove(p)
        print("file deleted")
      else:
        print("file is not exits")
    except Exception as err:
      print(f"an error:{err}")



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for delation a file")

check = int(input("please enter your response:-"))

if check == 1:
  createFile()
elif check == 2:
  readFile()
elif check == 3:
  updateFile()
elif check ==4:
  delation()