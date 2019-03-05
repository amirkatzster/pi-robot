import sys
import spotipy
import spotipy.util as util
from dotenv import load_dotenv, find_dotenv
from os.path import join, dirname
import os
from spotipy.oauth2 import SpotifyClientCredentials

class spotify:


    def __init__(self):
        self.spotify = spotipy.Spotify()
	dotenv_path = '.env'
        load_dotenv(dotenv_path)
	os.environ['SPOTIPY_CLIENT_ID'] = os.getenv('SPOTIPY_CLIENT_ID')
	os.environ['SPOTIPY_CLIENT_SECRET'] = os.getenv('SPOTIPY_CLIENT_SECRET')
	os.environ['SPOTIPY_REDIRECT_URI'] = os.getenv('SPOTIPY_REDIRECT_URI')
	

    def play(self, query):
	scope = 'user-modify-playback-state user-read-playback-state'
	
	token = util.prompt_for_user_token(os.getenv('SPOTIPY_USER'), scope)
	if token:
	    sp = spotipy.Spotify(auth=token)
	    #import pdb; pdb.set_trace()
	    res = sp.search(query)
	    print(res['tracks']['items'][0]['name'])
	    sp.start_playback('robo-pi',None,[res['tracks']['items'][0]['uri']])
	    self.dance()
	else:
            print("Can't get token for me")

    def check(self):
	client_credentials_manager = SpotifyClientCredentials()
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	playlists = sp.user_playlists('spotify')
	while playlists:
	    for i, playlist in enumerate(playlists['items']):
	        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
	    if playlists['next']:
	        playlists = sp.next(playlists)
	    else:
	        playlists = None

    def dance(self):
	import arduino
	from random import randint
	from time import sleep
	ard = arduino.arduino()
	for i in range(20):
		
		ard.send(randint(1,5))
		sleep(randint(2,7))
		ard.send(randint(50,54))
		sleep(randint(4,10))

if __name__ == "__main__":
    spotify().play('Enter Sandman')
    #spotify().check()
