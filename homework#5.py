immutable_var=42,42.0,'Лето =))',True
print(immutable_var)
# immutable_var[1]=77
# TypeError: 'tuple' object does not support item assignment. Значения элементов кортежа неизменяемые, в этом суть отличия данного модуля от списка.
mutable_list=[42,42.0,'Лето =))',True]
print(mutable_list)
mutable_list[0]='Q'
mutable_list[1]=42
mutable_list[2]='Весна'
mutable_list[3]=77
print(mutable_list)