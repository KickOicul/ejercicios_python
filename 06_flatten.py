def flatten(lists):
  flatt = []
  for i in lists:
    if isinstance(i, list):
      flatt.extend(flatten(i))
    else:
      flatt.append(i)
  return flatt


print(flatten(['perro', 'gato', ['perico', 'caballo', ['burro']]]))