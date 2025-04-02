

thisdict= {

   "rajeev": 100,
   "nikhat": 95,
   "saniya": 98
}

name= input("Enter the students name: ")

if name in thisdict:
    print(f'{name}s marks', thisdict[name])
else:
    print('Student not found')