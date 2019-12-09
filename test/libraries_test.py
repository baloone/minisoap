from audioread import audio_open


def test_ffmpeg():
    with audio_open('./songs/jingles/Squares.mp3') as f:
        assert (f.duration==28.2)

