# part 1
person={
    'name':'Ali',
    'age':'20',
    'hobbies':['horse riding','painting','swimming']
}
print(person['name'])
print(person['age'])

#part 2
person['age']=21
person['country']='Kuwait'
print(person)
print(len(person))

#part 3
person['hobbies'].append('reading')

def check_hobby(person):
    if len(person['hobbies']) >= 3:
        print('WOW you are amazing!')

check_hobby(person)