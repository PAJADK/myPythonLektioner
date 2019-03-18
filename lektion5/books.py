def borrow_books(*titler):
    antal = len(titler)
    print("\nantal bøger : " + str(antal))
    for title in titler:
        print(title)