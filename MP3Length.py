# python standard library
import glob
# python external library
from mutagen.mp3 import MP3


class MP3Length:

    @staticmethod
    def get_length():
        mp3_dir = './mp3/'

        # ファイル一覧
        files = glob.glob(mp3_dir + '*.mp3')

        if len(files) == 0:
            print('./mp3配下にMP3ファイルがありません。')
            exit()

        for file in files:
            mp3 = MP3(file)
            # ファイル名を切り出す
            file_name = file[len(mp3_dir):]
            # 標準出力(小数点は四捨五入される)
            print('{} >> {:.5f}'.format(file_name, mp3.info.length))


if __name__ == '__main__':
    MP3Length.get_length()