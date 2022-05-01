import os
import eyed3
import transliterate

FIND_DIRECTORY = 'test'


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            set_tags(os.path.join(root, name))


def set_tags(file):
    name = os.path.basename(file).split('.')[0]
    audio_file = eyed3.load(file)
    if not audio_file.tag:
        audio_file.initTag()
    audio_file.tag.title = transliterate.translit(name, reversed=True)
    if not audio_file.tag.album:
        audio_file.tag.album = 'Other'
    audio_file.tag.save()


if __name__ == '__main__':
    walk(FIND_DIRECTORY)
