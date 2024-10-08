# -*- coding: utf-8 -*-
# @Author    : Justin Ma


import os
import shutil
import ncm
import qmc
from pydub import AudioSegment


# from pydub.exceptions import CouldNotDecodeError

def convert_flac_to_mp3(flac_file_path, mp3_file_path):
    try:
        # 加载FLAC文件
        audio = AudioSegment.from_file(flac_file_path, format="flac")
        # 导出为MP3格式
        audio.export(mp3_file_path, format="mp3")

    # except CouldNotDecodeError:
    #     print("文件解码失败，请确保ffmpeg已安装且FLAC文件有效")
    except Exception as e:
        print(f"转换过程中发生错误：{e}")


def main():
    # if 1 == len(sys.argv):
    #     raise Exception("please input correct input dir.")

    # input_dir = sys.argv[1]
    input_dir = r"D:\Music\New-Music"

    if not os.path.isabs(input_dir):
        input_dir = os.path.join(os.getcwd(), input_dir)

    print("Input dir is ", input_dir)

    if not os.path.isdir(input_dir):
        raise Exception("input support directory only.")

    files = os.listdir(input_dir)
    converted_count = 0
    total_count = 0
    output_dir = os.path.join(input_dir, "mp3_file")
    print("Output dir is ", output_dir)

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.mkdir(output_dir)
    qcm_processed = False

    for file in files:
        src_path = os.path.join(input_dir, file)

        if os.path.isdir(src_path):
            continue

        total_count += 1

        if file.endswith(".ncm"):
            file_name = ncm.dump(src_path, output_dir)
            print(file_name)

            if file_name.endswith(".flac"):
                convert_flac_to_mp3(file_name, file_name.replace(".flac", ".mp3"))
                os.remove(file_name)

            converted_count += 1

        elif file.endswith(".flac"):
            convert_flac_to_mp3(src_path, src_path.replace(".flac", ".mp3"))
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
