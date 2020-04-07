from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import sys
import stt as st

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------'
print('ARE YOU THE ADMIN ?')
d=input('response')
if(d=='yes'):
    v=int(input(' enter secret key'))
    if(v==53415):
        st.reveal_info()
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------'
def function():
    client_credentials_manager = SpotifyClientCredentials(client_secret='0d2e381e77fa48c9b0504b4559eb1613',client_id='60512ae1d0614bea93fab9ba5f58e73a')

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    sp.trace = False

    if len(sys.argv) > 1:

        artist_name = ' '.join(sys.argv[1:])

    else:

        artist_name = input('artist  ')
    results = sp.search(q=artist_name, limit=50)

    tids = []

    for i, t in enumerate(results['tracks']['items']):

        print(' ', i, t['name'])

        tids.append(t['uri'])
    print('Enter the index corresponding to the song you want to hear..')
    x=int(input('index '))

    q=[]
    print('GETTING YOUR RECOMMENDATIONS....')

    features = pd.DataFrame(sp.audio_features(tids[x]))
    return (features.iloc[:,1:11])

#print(function())




