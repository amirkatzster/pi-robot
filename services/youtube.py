import pafy
import vlc


class youtube:

    def play_url(self,url):
        url = u'https://www.youtube.com/watch?v=tbKXMwunm1o'
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()