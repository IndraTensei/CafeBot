from config.config import *

HELP_SKIP = 'Skip the current playing song.'
HELP_SKIP_LONG = 'Skip the playing of the current song, does not work if loop one is activated. \n\nArguments: None.'
HELP_RESUME = 'Resumes the song player.'
HELP_RESUME_LONG = 'If the player if paused, return the playing. \n\nArguments: None.'
HELP_CLEAR = 'Clear the queue and songs history.'
HELP_CLEAR_LONG = 'Clear the songs queue and songs history. \n\nArguments: None.'
HELP_STOP = 'Stop the song player.'
HELP_STOP_LONG = 'Stop the song player, clear queue and history and remove Vulkan from voice channel.\n\nArguments: None.'
HELP_LOOP = 'Control the loop of songs.'
HELP_LOOP_LONG = """Control the loop of songs.\n\n Require: A song being played.\nArguments:
    One - Start looping the current song.
    All - Start looping all songs in queue.
    Off - Disable loop."""
HELP_NP = 'Show the info of the current song.'
HELP_NP_LONG = 'Show the information of the song being played.\n\nRequire: A song being played.\nArguments: None.'
HELP_QUEUE = f'Show the first {MAX_PRELOAD_SONGS} songs in queue.'
HELP_QUEUE_LONG = f'Show the first {MAX_PRELOAD_SONGS} song in the queue.\n\nArguments: None.'
HELP_PAUSE = 'Pauses the song player.'
HELP_PAUSE_LONG = 'If playing, pauses the song player.\n\nArguments: None'
HELP_PREV = 'Play the previous song.'
HELP_PREV_LONG = 'Play the previous song. If playing, the current song will return to queue.\n\nRequire: Loop to be disable.\nArguments: None.'
HELP_SHUFFLE = 'Shuffle the songs playing.'
HELP_SHUFFLE_LONG = 'Randomly shuffle the songs in the queue.\n\nArguments: None.'
HELP_PLAY = 'Plays a song.'
HELP_PLAY_LONG = 'Play a song in discord. \n\nRequire: You to be connected to a voice channel.\nArguments: Youtube or Spotify song/playlist link or the title of the song to be searched in Youtube.'
HELP_HISTORY = f'Show the history of played songs.'
HELP_HISTORY_LONG = f'Show the last {MAX_SONGS_HISTORY} played songs'
HELP_MOVE = 'Moves a song from position x to y in queue.'
HELP_MOVE_LONG = 'Moves a song from position x to position y in queue.\n\nRequire: Positions to be both valid numbers.\nArguments: 1º Number => Initial position, 2º Number => Destination position. Both numbers could be -1 to refer to the last song in queue.\nDefault: By default, if the second number is not passed, it will be 1, moving the selected song to 1º position.'
HELP_REMOVE = 'Remove a song in position x.'
HELP_REMOVE_LONG = 'Remove a song from queue in the position passed.\n\nRequire: Position to be a valid number.\nArguments: 1º Number => Position in queue of the song.'
HELP_RESET = 'Reset the Player of the server.'
HELP_RESET_LONG = 'Reset the Player of the server. Recommended if you find any type of error.\n\nArguments: None'
HELP_HELP = f'Use {BOT_PREFIX}help "command" for more info.'
HELP_HELP_LONG = f'Use {BOT_PREFIX}help command for more info about the command selected.'
HELP_INVITE = 'Send the invite URL to call Vulkan to your server.'
HELP_INVITE_LONG = 'Send an message in text channel with a URL to be used to invite Vulkan to your own server.\n\nArguments: None.'
HELP_RANDOM = 'Return a random number between 1 and x.'
HELP_RANDOM_LONG = 'Send a randomly selected number between 1 and the number you pass.\n\nRequired: Number to be a valid number.\nArguments: 1º Any number to be used as range.'
HELP_CHOOSE = 'Choose randomly one item passed.'
HELP_CHOOSE_LONG = 'Choose randomly one item passed in this command.\n\nRequire: Itens to be separated by comma.\nArguments: As much as you want.'
HELP_CARA = 'Return cara or coroa.'
HELP_CARA_LONG = 'Return cara or coroa.'