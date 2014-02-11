#coding=utf-8

things = ['a', 'b', 'c', 'd']
print things[1]
things[1] = 'z'
print things[1]
print things

stuff = {'name': 'Zed', 'age': 23, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = "San Francisco"
print stuff['city']
print stuff

aa = ['name', 'age', 'height']
for i in aa:
    print stuff[i]

stuff[1] = "11111"
stuff[2] = "22222"
stuff['three'] = "3333"
print stuff[1]
print stuff[2]
print stuff

print "=" * 15

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
        
happy_bday = Song(["happy birthday song 1",
                   "happy birthday song 2"])
bulls_on_parade = Song(["bulls on parade 1",
                        "bulls on parade 2"])

happy_bday.sing_me_a_song()
print "-" * 10
bulls_on_parade.sing_me_a_song()
