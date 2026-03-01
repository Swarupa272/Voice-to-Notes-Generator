from pydub import AudioSegment

def convert_to_wav_16k(src_path, out_path):
    audio = AudioSegment.from_file(src_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(out_path, format="wav")