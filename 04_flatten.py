def flatten (list1):
  list2=list1[0:1]
  for i in range (len(list1)):
    if list1[i] not in list2:
      list2.append(list1[i])
  return list2  


print(flatten(["perro","gato","gato","gato","perico","perro"]))
