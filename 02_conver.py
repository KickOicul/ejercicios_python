def conver (mxn):
  dol=0.055
  eur=0.052
  conv_dol=mxn*dol
  conv_eur=mxn*eur
  return conv_dol, conv_eur

print(conver(40))
print(conver(1))
print(conver(100))
print(conver(3))