import vlc

class play:

    def start(self, mp3_path):
        p = vlc.MediaPlayer(mp3_path)
        # talk slower
        p.set_rate(0.7)
        p.play()
        return p

    def stop(self, player):
        player.stop()