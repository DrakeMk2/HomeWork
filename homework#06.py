my_dict={'Sasha':1985,'Masha':1992,'Pasha':1980,'Dasha':2001}
print('Dict:',my_dict)
print('Existing value:',my_dict['Masha'])
print('Not existing value:',my_dict.get('Ivan'))
my_dict.update({'Ivan':1984,
                'Anna':1988})
a=my_dict.pop('Dasha')
print('Deleted value:',a)
print('Modified dictionary:',my_dict)

print(' ')

my_set={1,2,3,4,5,3,4,5,'A','v','a','n','g','a','r','d'}
print('Set:',my_set)
my_set.add('Forest')
my_set.add((42,17,78))
my_set.remove(5)
print('Modified set:',my_set)