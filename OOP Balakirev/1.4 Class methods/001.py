class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')


media1, media2 = MediaPlayer(), MediaPlayer()
media1.open('file media1')
media2.open('file media2')
media1.play()
media2.play()
