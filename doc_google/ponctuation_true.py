from google.cloud import speech_v1p1beta1
import io

def sample_recognize(local_file_path):
    client = speech_v1p1beta1.SpeechClient()
    enable_automatic_punctuation = True
    language_code = "fr-FR"
    config = {
            "enable_automatic_punctuation": enable_automatic_punctuation,
            "language_code": language_code,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))

sample_recognize('voice_test.wav')
