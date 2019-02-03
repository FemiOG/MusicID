import os
import shortuuid
import pandas as pd

'''
Run this in bash before running this file ---> find . -name '.DS_Store' -type f -delete -print 
You can run only once so back up the songs folder incase of a rewrite

'''

# def artist_initials(artist):
#     first_letters = [ i[0].upper() for i in artist.split() ]
#     output = "".join(first_letters[:2])
#     return output

def rename_songs(source):
    genres = []
    dirs = []
    meta = []

    for _, dir, _ in os.walk(source):
        dirs.append(dir)

    genres = dirs[0]

    for genre in genres:
        for artist in os.listdir(source + '/' + genre):
            for artist_song in os.listdir(source + '/' + genre + '/' + artist):
                filename = source + '/' + genre + '/' + artist + '/'
                id = shortuuid.uuid()

                # Rename songs to a uuid
                os.rename(filename + artist_song, filename + id + '.mp3')
                meta.append([id, artist_song, artist, genre])

    meta = pd.DataFrame(data=meta, columns=['id', 'artist_song', 'artist', 'genre'])
    return meta 


def main():
    source_train = '/Users/femi/Desktop/ML Mentorship Project/project/data/songs/train'
    source_test = '/Users/femi/Desktop/ML Mentorship Project/project/data/songs/test'

    train = rename_songs(source_train)
    train.to_csv('train.csv')

    test = rename_songs(source_test)
    test.to_csv('test.csv') 



if __name__ == '__main__':
    main()


