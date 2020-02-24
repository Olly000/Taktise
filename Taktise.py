#!/usr/bin/env Python3

import os
import errno
from pydub import AudioSegment
from pydub.playback import play


class Taktise:
    def __init__(self):
        self.target = input("which subfolder of current directory to be converted?: ")
        self.path = os.getcwd() + "/" + self.target
        self.out_path = self.create_dir()
        self.file_list = os.listdir(self.path)

    def create_dir(self):
        destination = self.path + '48'
        try:
            os.makedirs(destination)
        except OSError as exception:
            if exception.errno == errno.EEXIST:
                print(f"{self.path}48 already exists. Conversion aborted")
                exit(0)
        return destination

    def file_convert_wav(self, file):
        file_container = AudioSegment.from_wav(f"{self.path}/{file}")
        file_container = file_container.set_frame_rate(48000).set_channels(1)
        file_container.export(out_f=f"{self.out_path}/{file}", format="wav")

    def file_convert_mp3(self, file):
        file_container = AudioSegment.from_mp3(file)
        file_container.export()

    def loop_files(self):
        for file in self.file_list:
            if file.endswith(".wav"):
                self.file_convert_wav(file)
            elif file.endswith(".mp3"):
                self.file_convert_mp3(file)


if __name__ == '__main__':
    test = Taktise()
    test.loop_files()