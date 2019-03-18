def desplay_message():
    print("What you are learning about in this chapter? ")
desplay_message()


def favorite_books(book_name):
    print("One of my favorite books is: " + book_name.title())
favorite_books('Python crash course')


def make_shirts(size, shirts_text, shirts_color=''):
    if shirts_color:
        print("Shirts size is: " + size + " color is " + shirts_color + " mesagge text is: " + shirts_text)
    else:
        print("Shirts size is: " +size + " mesagge text is: " + shirts_text)

make_shirts('M', 'jubiiii')
make_shirts('M', 'jubiiii', 'black')


def make_shirt(shirt_text,Tsize ='L'):
    print("Shirts size is: " +Tsize + " mesagge text is: " + shirt_text)
make_shirt(shirt_text='jubiiii' )


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

def describe_city(city, country='Danmark'):
    print("\n" + city + ' is in ' + country)
describe_city(city='københavn')
