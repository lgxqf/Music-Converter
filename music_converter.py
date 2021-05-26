# -*- coding: utf-8 -*-
# @Author    : Justin Ma


import argparse
import os
import shutil
import sys
import ncm
import qmc


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=os.path.abspath, help='output directory')
    # parser.add_argument('-m', '--mode', choices=('qmc2flac', 'flac2mp3', 'qmc2mp3',), default='qmc2mp3')
    # parser.add_argument('-n', '--thread-num', type=int,help='convert thread num')

    args = parser.parse_args()
    return args


def main():
    if 1 == len(sys.argv):
        raise Exception("please input correct input dir.")

    # args = read_args()
    input_dir = sys.argv[1]

    if not os.path.isabs(input_dir):
        input_dir = os.path.join(os.getcwd(), input_dir)

    print("Input dir is ", input_dir)

    if not os.path.isdir(input_dir):
        raise Exception("input support directory only.")

    # if args.output_dir is not None:
    #     output_dir = args.output_dir

    files = os.listdir(input_dir)
    converted_count = 0
    total_count = len(files)
    output_dir = os.path.join(input_dir, "mp3_file")
    print("Output dir is ", output_dir)

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.mkdir(output_dir)
    qcm_processed = False

    for file in files:
        src_path = os.path.join(input_dir, file)
        if file.endswith(".ncm"):
            ncm.dump(src_path, output_dir)
            converted_count += 1
        elif file.endswith(".qmc0") or file.endswith(".qmc3") or file.endswith(".qmcflac"):
            if not qcm_processed:
                try:
                    convert = qmc.Convert(input_dir=input_dir)
                    convert.qmc_to_flac()
                except Exception as e:
                    print(e)

            converted_count += 1
        else:
            continue

        print("No ", converted_count, " converting file ", file)

    files = os.listdir(input_dir)

    for file in files:
        if file.endswith(".mp3"):
            shutil.move(os.path.join(input_dir, file), os.path.join(output_dir, file))

    print(total_count, " files, ", converted_count, " are converted")


if __name__ == '__main__':
    main()
