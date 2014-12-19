from threading import Thread
import pyaudio
import wave

import random
import time


class AudioFile:
    '''
    adapted to be asynchronous from
    elliotjreed.com/article.php?read=play_a_sound_wav_audio_file_in_python3
    '''
    chunk = 1024

    def __init__(self, file, wait=1):
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True
        )
        self.data = []
        d = self.wf.readframes(self.chunk)
        while d != '':
            self.data.append(d)
            d = self.wf.readframes(self.chunk)
        self.last_played = time.time()
        self.wait = wait

    def blocking_play(self):
        for d in self.data:
            self.stream.write(d)

    def play(self):
        if time.time() - self.last_played > self.wait:
            p = Thread(target=self.blocking_play)
            p.start()
            self.last_played = time.time()

    def close(self):
        self.stream.close()
        self.p.terminate()

player_fire_player = AudioFile('invaders/audio/player-fire.wav', wait=.55)
alien_fire_player = AudioFile('invaders/audio/alien-fire.wav', wait=.4)
way_to_go_player = AudioFile('invaders/audio/way-to-go.wav')
direct_hit_player = AudioFile('invaders/audio/direct-hit.wav')
nice_shot_player = AudioFile('invaders/audio/nice-shot.wav')
you_lose_player = AudioFile('invaders/audio/you-lose.wav', wait=3)
alien_hit_player = AudioFile('invaders/audio/default-alien-hit.wav', wait=.3)
congrats_player = AudioFile('invaders/audio/congratulations.wav', wait=3)


def player_fire():
    player_fire_player.play()


def alien_fire():
    alien_fire_player.play()

_alien_down_sounds = (way_to_go_player, direct_hit_player, nice_shot_player)


def alien_down():
    if random.random() < .2:
        random.choice(_alien_down_sounds).play()
    else:
        alien_hit_player.play()


def you_lose():
    you_lose_player.play()


def congratulations():
    congrats_player.play()
