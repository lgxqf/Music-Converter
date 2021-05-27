# -*- coding: utf-8 -*-
# @Author    : Justin Ma


import os
import shutil
import sys
import ncm
import qmc


def main():
    if 1 == len(sys.argv):
        raise Exception("please input correct input dir.")

    input_dir = sys.argv[1]

    if not os.path.isabs(input_dir):
        input_dir = os.path.join(os.getcwd(), input_dir)

    print("Input dir is ", input_dir)

    if not os.path.isdir(input_dir):
        raise Exception("input support directory only.")

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
