i = int(input("masukan nilai: ")) #pengambilan variabel input dengan type:integer
while i <= 10:
  i += 1
  if i == 5:
    continue #skip function
  print(i,' x ',i ,' = ',i*i) 