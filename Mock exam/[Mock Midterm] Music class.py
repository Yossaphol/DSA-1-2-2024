class Song:
    def __init__(self, name, genre, durations) :
        self.name = name
        self.genre = genre
        self.durations = durations
    def show_info(self):
        m = self.durations // 60
        s = self.durations % 60
        return f"{self.name} <|> {self.genre} <|> {m}.{s:>02}"

Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())