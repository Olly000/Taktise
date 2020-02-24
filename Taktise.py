#!/usr/bin/env Python3

import os
import errno
from pydub import AudioSegment


class Taktise:
    def __init__(self):
        self.target = input("which folder to be converted?: ")
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

    def file_convert(self, file):
        file_container = AudioSegment.from_file(f"{self.path}/{file}")
        file_container = file_container.set_frame_rate(48000).set_channels(1)
        if file.endswith("mp3"):
            file = file.split('.')[0] + ".wav"
        file_container.export(out_f=f"{self.out_path}/{file}", format="wav")

    def loop_files(self):
        for file in self.file_list:
            if file.endswith(".wav") or file.endswith(".mp3"):
                self.file_convert(file)
        print("Conversion Completed")


if __name__ == '__main__':
    test = Taktise()
    test.loop_files()