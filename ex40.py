class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    def deleteeverything(self):
        self.lyrics = " "
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family","With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
sanbonsakura = Song(["大胆不敵に ハイカラ革命 磊々落々 反戦国家","日の丸印の 二輪車転がし 悪霊退散 ICBM 環状線を 走り抜けて 東奔西走 なんのその"])
sanbonsakura.sing_me_a_song()
lyrics = ["少年少女 戦国無双 浮世の 随(まにま)に", "千本桜 夜ニ紛レ 君ノ声モ 届カナイヨ"]
sanbonsakura2 = Song(lyrics)
sanbonsakura2.sing_me_a_song()
sanbonsakura2.deleteeverything()
sanbonsakura2.sing_me_a_song()
#i searched  
