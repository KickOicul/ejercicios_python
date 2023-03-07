def repeated(list1):
  list2 = list1[0:1]
  list3 = list1[0:1]
  list4 = list3[0:1]

  for i in range(len(list1)):
    if list1[i] not in list2:
      list2.append(list1[i])
    else:
      list3.append(list1[i])

  for i in range(len(list3)):
    if list3[i] not in list4:
      list4.append(list3[i])
  repeat = len(list4)
  return repeat


print(repeated(["perro", "gato", "perico", "gato", "gato", "perro"]))