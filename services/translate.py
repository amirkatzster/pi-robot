from google.cloud import translate as google_translate

class translate:

    def __init__(self):
        self.translate_client = google_translate.Client()

    def heb_to_eng(self, heb_text):
        return self.translate(heb_text,'en')

    def eng_to_heb(self, eng_text):
        return self.translate(eng_text,'he')

    def translate(self, text, target_code):
        # Translates some text into Russian
        translation = self.translate_client.translate(
            text,
            target_language=target_code)

        print(u'Text: {}'.format(text))
        print(u'Translation: {}'.format(translation['translatedText']))
        return translation['translatedText']