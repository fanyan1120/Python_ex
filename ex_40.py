#coding=utf-8

import mystuff

print mystuff.mystuff['apple']
mystuff.apple()
print mystuff.mystuff_var

thing = mystuff.aaa()
#thing.apple()
thing.pear()
print thing.mystuff_var

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
