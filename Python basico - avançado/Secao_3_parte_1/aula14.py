a= 'A'
b= 'B'
c= 1.10000030300 
string = 'a={} b ={} , c={:.2f} {}'
formato = string.format(a,b,c,'1234')
print(formato)

a= 'A'
b= 'B'
c= 1.10000030300 
#podemos usar os indices
string = 'a={0} b ={1} , c={2:.2f} '
formato = string.format(a,b,c)
print(formato)

a= 'A'
b= 'B'
c= 1.10000030300 
#podemos usar os indices
string = 'a={nome1} b ={nome2} , c={nome3:.2f} ,b={nome2} '
formato = string.format(
    nome1=a,nome2=b,nome3=c)
print(formato)


