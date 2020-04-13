#from __future__ import print_function    # (at top of module)
#from spotipy.oauth2 import SpotifyClientCredentials
#import spotipy
#import pandas as pd
#import sys
#
import os
from django.shortcuts import render
from django.views import generic
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from .forms import ArtistForm
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse
#import music_recommendation

# Create your views here.

#class Track:
#    def initialize(self,res):
#        self.art = res['album']['images'][2]['url']
#        self.name = res['name']
#        self.link = res['external_urls']['spotify']
#
#    def to_dic(self):
#        x = dict()
#        x['name'] = self.name
#        x['art'] = self.art
#        x['link'] = self.link
#        return x
#
#    def __str__(self):
#        return ("art link: " + self.art + " name: " + self.name + " ext. link: " + self.link + "\n")
#
#
#def function(artname):
#    client_credentials_manager = SpotifyClientCredentials(client_secret='0d2e381e77fa48c9b0504b4559eb1613',client_id='60512ae1d0614bea93fab9ba5f58e73a')
#
#    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
#    sp.trace = False
#
#    if len(sys.argv) > 1:
#
#        artist_name = ' '.join(sys.argv[1:])
#
#    else:
#        artist_name = artname
#
#    results = sp.search(q=artist_name, limit=50)
#
#    tids = []
#    sngs = []
#
#    for i, t in enumerate(results['tracks']['items']):
#        tmp = Track()
#        tmp.initialize(t)
#        sngs.append(tmp.to_dic())
#        #print(' ', i, t['name'])
#        tids.append(t['uri'])
#
#    return sngs
#
#tracks = function('justin bieber')
#print(tracks)
#
##tracks = [{'name': 'Intentions', 'art': 'https://i.scdn.co/image/ab67616d0000b27308e30ab6a058429303d75876', 'link': 'https://open.spotify.com/track/364dI1bYnvamSnBJ8JcNzN'}, {'name': '10,000 Hours (with Justin Bieber)', 'art': 'https://i.scdn.co/image/ab67616d0000b27386953b1cbaa29e477db0b479', 'link': 'https://open.spotify.com/track/2wrJq5XKLnmhRXHIAf9xBa'}, {'name': 'Forever (feat. Post Malone & Clever)', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/2ZlCGeK30BLRNSPC832pNZ'}, {'name': 'Intentions (feat. Quavo)', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/4umIPjkehX1r7uhmGvXiSV'}, {'name': 'Yummy', 'art': 'https://i.scdn.co/image/ab67616d0000b27360eec5a0953d4a33d77ed71d', 'link': 'https://open.spotify.com/track/41L3O37CECZt3N7ziG2z7l'}, {'name': "I Don't Care (with Justin Bieber)", 'art': 'https://i.scdn.co/image/ab67616d0000b27357cc434093fd4b6af7500fd8', 'link': 'https://open.spotify.com/track/3HVWdVOQ0ZA45FuZGSfvns'}, {'name': 'Come Around Me', 'art': 'https://i.scdn.co/image/ab67616d0000b273b33d394952d326221494a887', 'link': 'https://open.spotify.com/track/1Y8g8zMEK5lwGIXGg1DOZc'}, {'name': "That's What Love Is", 'art': 'https://i.scdn.co/image/ab67616d0000b273b33d394952d326221494a887', 'link': 'https://open.spotify.com/track/4KqV5XrQ3bTqPtZrH38kQy'}, {'name': 'Confirmation', 'art': 'https://i.scdn.co/image/ab67616d0000b273b33d394952d326221494a887', 'link': 'https://open.spotify.com/track/1wFRIylMFDLvENzNNg4B1O'}, {'name': 'All Around Me', 'art': 'https://i.scdn.co/image/ab67616d0000b273b33d394952d326221494a887', 'link': 'https://open.spotify.com/track/45ON4eYvgOZlyOt4cYKjmI'}, {'name': 'Changes', 'art': 'https://i.scdn.co/image/ab67616d0000b273b33d394952d326221494a887', 'link': 'https://open.spotify.com/track/5Ghv5BHrZHKOUkjinFlSd4'}, {'name': 'Confirmation', 'art': 'https://i.scdn.co/image/ab67616d0000b273f1a5e16a4deda66f64b35390', 'link': 'https://open.spotify.com/track/5uNjKMXxJkRfXp1jCO3DD5'}, {'name': 'Come Around Me', 'art': 'https://i.scdn.co/image/ab67616d0000b273b8ea1707293c2e067fd51a0a', 'link': 'https://open.spotify.com/track/3e2VVyqCmnTXl0bBfgQgBJ'}, {'name': 'All Around Me', 'art': 'https://i.scdn.co/image/ab67616d0000b273f1a5e16a4deda66f64b35390', 'link': 'https://open.spotify.com/track/3kYJNRjyoiPPoxsAbvXfZx'}, {'name': 'E.T.A.', 'art': 'https://i.scdn.co/image/ab67616d0000b273f1a5e16a4deda66f64b35390', 'link': 'https://open.spotify.com/track/7Mo2grPV40f3uGHLvcOI5o'}, {'name': 'Second Emotion', 'art': 'https://i.scdn.co/image/ab67616d0000b273b8ea1707293c2e067fd51a0a', 'link': 'https://open.spotify.com/track/6cMGECjzH3m1QjfCmFqQM6'}, {'name': 'Changes', 'art': 'https://i.scdn.co/image/ab67616d0000b273f1a5e16a4deda66f64b35390', 'link': 'https://open.spotify.com/track/7h32HFeMu1PAjg9miUta6c'}, {'name': 'Running Over', 'art': 'https://i.scdn.co/image/ab67616d0000b273b8ea1707293c2e067fd51a0a', 'link': 'https://open.spotify.com/track/66sFU2r6DPVMLdh73CSnbK'}, {'name': 'Intentions', 'art': 'https://i.scdn.co/image/ab67616d0000b273b8ea1707293c2e067fd51a0a', 'link': 'https://open.spotify.com/track/6FOOTEAugyi3q8HXjK17t7'}, {'name': 'Habitual', 'art': 'https://i.scdn.co/image/ab67616d0000b273f1a5e16a4deda66f64b35390', 'link': 'https://open.spotify.com/track/3JeTe0VAQfCPwERsR1Xj51'}, {'name': 'Sorry', 'art': 'https://i.scdn.co/image/ab67616d0000b273a360cb00705e7da78bf73c40', 'link': 'https://open.spotify.com/track/0JKxxBowPpQr4fSMIbUwos'}, {'name': 'Love Yourself', 'art': 'https://i.scdn.co/image/ab67616d0000b2736b32e7b45203c040a17ba691', 'link': 'https://open.spotify.com/track/1vyQSn9D3el41r5bUE2P8O'}, {'name': 'Intentions - Acoustic', 'art': 'https://i.scdn.co/image/ab67616d0000b273ae47a88843b756c5220bafdc', 'link': 'https://open.spotify.com/track/5M9ybwBW7sY9SoUKd79Fw4'}, {'name': 'Sorry', 'art': 'https://i.scdn.co/image/ab67616d0000b2736b32e7b45203c040a17ba691', 'link': 'https://open.spotify.com/track/0BoXEVCv7jjg5qtWD4JC2f'}, {'name': 'What Do You Mean?', 'art': 'https://i.scdn.co/image/ab67616d0000b2736b32e7b45203c040a17ba691', 'link': 'https://open.spotify.com/track/0Edh3PLM7EfNKDdPP7cbSF'}, {'name': 'What Do You Mean? - Acoustic', 'art': 'https://i.scdn.co/image/ab67616d0000b27354ed502c1c61d709f1da093c', 'link': 'https://open.spotify.com/track/2Uj8C7SWCQWIHyArv52SvG'}, {'name': 'U Smile - Acoustic Version', 'art': 'https://i.scdn.co/image/ab67616d0000b273c903227b23100f7e719e9f78', 'link': 'https://open.spotify.com/track/1WtNmAeXOZMQi97n240Jwv'}, {'name': 'Somebody To Love', 'art': 'https://i.scdn.co/image/ab67616d0000b273167546f19598d02dd07eb7e1', 'link': 'https://open.spotify.com/track/6LNFL10ILwrOFTAZcpDuU8'}, {'name': 'Baby', 'art': 'https://i.scdn.co/image/ab67616d0000b2736b32e7b45203c040a17ba691', 'link': 'https://open.spotify.com/track/24Zm8apdKjmSOeNKOs7InM'}, {'name': 'What Do You Mean?', 'art': 'https://i.scdn.co/image/ab67616d0000b273a360cb00705e7da78bf73c40', 'link': 'https://open.spotify.com/track/1gULrY3VYzlhSpcW0vHd0m'}, {'name': 'Sorry', 'art': 'https://i.scdn.co/image/ab67616d0000b273032b72c6f7bceda0aab445bb', 'link': 'https://open.spotify.com/track/5f5exAQAIs8WDu2wPYuGBK'}, {'name': 'Somebody To Love', 'art': 'https://i.scdn.co/image/ab67616d0000b2732ea85ae020075730070891b1', 'link': 'https://open.spotify.com/track/1Ri4W9PaRo2xIh6rSgFldG'}, {'name': "I Don't Care (with Justin Bieber)", 'art': 'https://i.scdn.co/image/ab67616d0000b273a53a148d92ce7afa20229e49', 'link': 'https://open.spotify.com/track/0hVXuCcriWRGvwMV1r5Yn9'}, {'name': 'bad guy (with Justin Bieber)', 'art': 'https://i.scdn.co/image/ab67616d0000b273a69b8b111a5fb8cb1c97e8eb', 'link': 'https://open.spotify.com/track/3yNZ5r3LKfdmjoS3gkhUCT'}, {'name': 'Intentions', 'art': 'https://i.scdn.co/image/ab67616d0000b2731b26ee37fa47546cf27ce0fb', 'link': 'https://open.spotify.com/track/4jWenpU6ebQFosqmJ5VVfS'}, {'name': "That's What Love Is", 'art': 'https://i.scdn.co/image/ab67616d0000b2731b26ee37fa47546cf27ce0fb', 'link': 'https://open.spotify.com/track/6wgJ237qTsXmdVpkVCCYxH'}, {'name': 'Changes', 'art': 'https://i.scdn.co/image/ab67616d0000b2731b26ee37fa47546cf27ce0fb', 'link': 'https://open.spotify.com/track/5yPwlEcCmLQBzpJA95fmOe'}, {'name': 'Yummy', 'art': 'https://i.scdn.co/image/ab67616d0000b273b8ea1707293c2e067fd51a0a', 'link': 'https://open.spotify.com/track/6OvQOYBHVsJrg8y6UCe99g'}, {'name': 'E.T.A.', 'art': 'https://i.scdn.co/image/ab67616d0000b2731b26ee37fa47546cf27ce0fb', 'link': 'https://open.spotify.com/track/0C1xSrOo29uKo51JnvVXx8'}, {'name': 'Available', 'art': 'https://i.scdn.co/image/ab67616d0000b2731b26ee37fa47546cf27ce0fb', 'link': 'https://open.spotify.com/track/4F4KxTLw2SpLyJQbeX2kG7'}, {'name': 'Come Around Me', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/2o9LAypwGH4ctV0i9boo6d'}, {'name': 'Yummy', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/16wAOAZ2OkqoIDN7TpChjR'}, {'name': 'Juke Jam (feat. Justin Bieber & Towkio)', 'art': 'https://i.scdn.co/image/ab67616d0000b273e71dd15fc5bdefd5bff70452', 'link': 'https://open.spotify.com/track/3eze1OsZ1rqeXkKStNfTmi'}, {'name': "I'm the One (feat. Justin Bieber, Quavo, Chance the Rapper & Lil Wayne)", 'art': 'https://i.scdn.co/image/ab67616d0000b2737b219c19829e83a86cc9786c', 'link': 'https://open.spotify.com/track/1jYiIOC5d6soxkJP81fxq2'}, {'name': 'Love Yourself', 'art': 'https://i.scdn.co/image/ab67616d0000b273f46b9d202509a8f7384b90de', 'link': 'https://open.spotify.com/track/50kpGaPAhYJ3sGmk6vplg0'}, {'name': 'Habitual', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/40qyPyljksBEqlNw5sW37T'}, {'name': 'Where Are Ü Now (with Justin Bieber)', 'art': 'https://i.scdn.co/image/ab67616d0000b27357fc4730e06c9ab20c1e073b', 'link': 'https://open.spotify.com/track/66hayvUbTotekKU3H4ta1f'}, {'name': 'All Around Me', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/5Py8zRKGkZvgHniVVtvNCN'}, {'name': 'Available', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/1b6tPXXCV2fSNtR3SKWUQA'}, {'name': 'Running Over (feat. Lil Dicky)', 'art': 'https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6', 'link': 'https://open.spotify.com/track/75nKBP8jQu681pTNCtrEnn'}]

@login_required
def home(request):
    client_credentials_manager = SpotifyClientCredentials(client_secret='0d2e381e77fa48c9b0504b4559eb1613',client_id='60512ae1d0614bea93fab9ba5f58e73a')

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    sp.trace = False

    sngs = []

    form = ArtistForm()

    if request.method == 'POST':

        form = ArtistForm(request.POST)
        if form.is_valid():
            artname = form.cleaned_data.get('artist')
            print(artname)

            results = sp.search(q=artname, limit=50)

            for i, t in enumerate(results['tracks']['items']):
              tmp = dict()
              tmp['name'] = t['name']
              tmp['art'] = t['album']['images'][1]['url']
              tmp['link'] = t['external_urls']['spotify']
              sngs.append(tmp) 

        context = {
        'tracks': sngs
        }
        return render(request,'recommendpg/home.html',context)             

    else:
        form = ArtistForm()
    
    return render(request,'recommendpg/home.html',{'form': form})

#    results = sp.search(q='justin bieber', limit=50)
#
#    for i, t in enumerate(results['tracks']['items']):
#        tmp = dict()
#        tmp['name'] = t['name']
#        tmp['art'] = t['album']['images'][1]['url']
#        tmp['link'] = t['external_urls']['spotify']
#        sngs.append(tmp)
#
#    context = {
#        'tracks': sngs
#    }
#    return render(request,'recommendpg/home.html', context)
