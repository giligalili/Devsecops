def person_desc(name, phone, city, street,*, h, age):
    print(name)
    print(phone)
    print(city)
    print(street)
    print(h)
    print(age)

def check_like(**arg):
    if arg == 'yes': 
    print(person_desc(name) 'is a nice person')
    else:
    print(person_desc(name) 'is a bad person')


person_desc('tod','9999999','lod', 'hatzbar', h=180, age=80)

check_like(yes)


