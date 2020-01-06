import subprocess


def test_ffmpeg():
    subprocess.Popen(['ffmpeg', '-version'], stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    assert True

