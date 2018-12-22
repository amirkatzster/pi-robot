import vlc

class play:

    speed = 0.7

    def start(self, mp3_path):
        p = vlc.MediaPlayer(mp3_path)
        # talk slower
        p.set_rate(self.speed)
        p.play()
        return p

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    def stop(self, player):
        player.stop()