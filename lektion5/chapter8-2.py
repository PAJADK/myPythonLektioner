def make_album(name, title, number_of_tracks=''):
    if number_of_tracks:
        album = {'artist_name': name, 'album_titel': title, 'tracks':number_of_tracks}
    else:
        album ={'artist_name': name, 'album_titel': title}
    return  album

albums = make_album('jime', 'henrikx')
print(albums)

albums = make_album('jime', 'henrikx', number_of_tracks=6)
print(albums)


def make_album(name, title, number_of_tracks=''):
    if number_of_tracks:
        album = {'artist_name': name, 'album_titel': title, 'tracks':number_of_tracks}
    else:
        album ={'artist_name': name, 'album_titel': title}
    return  album

while True:
    print("(enter 'q' at any time to quit)")

    artist_name = input("Name: ")
    if artist_name == 'q':
        break
    album_name = input("Album name: ")
    if artist_name == 'q':
        break

albums = make_album(artist_name, album_name)
print(albums)

albums = make_album('jime', 'henrikx', number_of_tracks=6)
print(albums)