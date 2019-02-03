from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def extract_artist_top_songs(artist):
    '''
    Function to extract top 50 songs of an artist from top50songs.org

    artist -- name of artist

    '''
    song_list = []
    # specify the url
    quote_page = 'http://www.top50songs.org/artist.php?artist='+str(artist)

    # query the website and return the html to the variable ‘page’
    page = urlopen(quote_page)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    songs = soup.find_all('li')
    for song in songs:
        song_list.append(song.text)

    return song_list

def main():
    artists = pd.read_csv('artists.csv')
    artist_song = pd.DataFrame(columns=['Song','Artist','Genre'])
    for artist in artists:
        songs = extract_artist_top_songs(artist[0])
        artist_song['Songs'] = songs
        artist_song['Artist'] = artist[0]
        artist_song['Genre'] = artist[1]
    # with open('artists.csv') as csv_file:
    #     reader = csv.reader(csv_file, delimiter=',')
    #     artists = reader
    #     for artist in artists:
    #         songs = extract_artist_top_songs(artist[0])
    #         with open('artist_song.csv', 'w') as csv_file:
    #             writer = csv.writer(csv_file, delimiter=',')
    #             writer.writerows(songs,artist)

if __name__ == '__main__':
    main()
