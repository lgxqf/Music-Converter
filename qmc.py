import math
import os
import shutil
import multiprocessing
import platform


def get_decoder_name():
    decoder = "decoder-mac"
    print("Platform is : ", platform.system())

    if platform.system() == 'Windows':
        decoder = "decoder-win.exe"
    elif platform.system() == 'Linux':
        decoder = "decoder-linux"

    return decoder


class Convert(object):
    def __init__(self, input_dir=None, output=None):
        self.input = input_dir
        self.output = output if output is not None else input_dir
        self.root_path = os.path.abspath(os.path.dirname(__file__))
        self.flac_files = []
        self.mp3_files = []
        self.procs = []
        self.qm2flac_tool = os.path.join(self.root_path, "bin/" + get_decoder_name())

    def qmc_to_flac(self):
        os.chdir(self.input)
        print(self.qm2flac_tool)
        os.system(self.qm2flac_tool)
        # print("qmc_to_flac convert finish.")
        return self
