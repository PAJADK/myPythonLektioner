
def borrow_books(*titler):
    antal = len(titler)
    print("\nantal bøger : " + str(antal))
    for title in titler:
        print(title)


borrow_books('Idioten')
borrow_books('Kældermennesket', 'Forbrydelse og Straf')
borrow_books('Kældermennesket', 'Forbrydelse og Straf', 'Tvang')