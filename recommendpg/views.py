import os
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from .forms import ArtistForm
from django.contrib.auth.decorators import login_required
from .recommendations import recommendations
import math
#from sklearn.ensemble import RandomForestClassifier
#import pandas as pd
#import platform

def getsphandle():
    client_credentials_manager = SpotifyClientCredentials(client_secret='',
                                                      client_id='')

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

@login_required
def home(request):
    sp = getsphandle()
    sp.trace = False

    sngs = []

    form = ArtistForm()

    if request.method == 'POST':

        form = ArtistForm(request.POST)
        if form.is_valid():
            artname = form.cleaned_data.get('artist')
            print(artname)

            results = sp.search(q=artname, limit=20)
            for t in results['tracks']['items']:
              tmp = dict()
              tmp['id'] = t['id']
              tmp['name'] = t['name']
              tmp['art'] = t['album']['images'][1]['url']
              tmp['link'] = t['external_urls']['spotify']
              tmp['album'] = t['album']
              tmp['duration'] = str(math.floor(t['duration_ms']/60000)) + " mins " + str(math.floor((t['duration_ms']/60000 - math.floor(t['duration_ms']/60000))*60)) + " secs "
              sngs.append(tmp)

        context = {
        'tracks': sngs
        }
        return render(request,'recommendpg/home.html',context)             

    else:
        form = ArtistForm()
    
    return render(request,'recommendpg/home.html',{'form': form})


@login_required
def recommend(request, tid):
    sp = getsphandle()
    context = recommendations(sp,tid)
    #features = pd.DataFrame(sp.audio_features(tid))
  
    return render(request,'recommendpg/recopage.html',context)
