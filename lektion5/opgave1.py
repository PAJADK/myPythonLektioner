def make_shirts(shirts_size, shirts_text, shirts_color=''):
    if shirts_color:
        print("Shirts size is: " + shirts_size + " color is " + shirts_color + " mesagge text is: " + shirts_text)
    else:
        print("Shirts size is: " +shirts_size + " mesagge text is: " + shirts_text)

make_shirts('M', 'jubiiii')
make_shirts('M', 'jubiiii', 'black')


def describe_city(city, country='Danmark'):
    print("\n" + city + ' is in ' + country)
describe_city('københavn')
