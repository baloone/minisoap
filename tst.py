from audioread import audio_open

with audio_open('./songs/jingles/Squares.mp3') as f:
    print(f.duration)

