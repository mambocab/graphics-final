## Features

Run with ./invaders/main.py.

This command accepts 3 command-line arguments:

- `--prod`, which enhances performance by disabling OpenGL logging,
- `--fullscreen`, which allows you to play in fullscreen mode, and
- `--mode`, which takes 1 argument, "easy" or "hard". "easy" disables firing, while "hard" makes it more frequent.

Press left and right to move the player, and up to fire the cannon. Press q to quit.

The game plays audio on a number of occasions:

- when the player fires
- when an alien fires
- when the player wins the game
- when the player loses the game
- when the player hits an alien (there are 4 different sounds that play, with different probabilities)

Each barrier can take 4 hits. Check out the different colors for each damage level!

The aliens move as far to the left and right as they can -- that is to say, if the leftmost column of aliens is all destroyed, the remaining leftmost column will move all the way to the left.

Similarly, the aliens move as far down as they can. That is to say, if you destroy the entire bottom row of aliens, you buy yourself some time.

If the aliens reach the level of any remaining barriers, the barriers disappear.

The aliens fire approximately every 2-4 seconds. The timing is determined randomly.

### Extra Credit

- Sound on events
- "Deteriorating barriers"

## Acknowledgments

All models by William Hill (wahill2).

Audio-playing code adapted from Elliot J. Reed's example code, found at:

http://www.elliotjreed.com/article.php?read=play_a_sound_wav_audio_file_in_python3
