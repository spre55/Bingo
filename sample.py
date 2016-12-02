# coding: utf-8

i=0
random_key=random.randint(0,75-i)


random_list=[x for x in range(1,76)]
print(random_list[random_key])
random_list.pop(random_key)

i+=1

random_key=random.randint(1,75-i)
print(random_list[random_key])
random_list.pop(random_key)

print(random_list)
