import os, random, shutil

def move_file(old_path, new_path, flag):  # 前者可以是文件(文件夹)   后者为文件夹 flag 用于判断是否为文件夹
    if flag == 0:
        filelist = os.listdir(old_path)  # 列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
        for file in filelist:
            src = os.path.join(old_path, file)
            dst = os.path.join(new_path, file)
            shutil.copy(src, dst)
    elif flag == 1:  # 如果不为文件夹，直接移动文件到指定目录
        src = old_path
        dst = new_path
        shutil.copy(src, dst)


def move_all_file(old_path_all,new_path):
    old_path_every = ''  # 这是该文件夹下具体的文件（包含子文件夹）
    file_list = os.listdir(old_path_all)  # 获取文件路径
    for i in range(len(file_list)):  # 遍利每一个文件夹
        if os.path.isdir(old_path_all + "/" + file_list[i]):  # 判断下一个文件是否为文件夹
            filelist = os.listdir(old_path_all + "/" + file_list[i])  # 列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
            for file in filelist:
                if file.split(".")[1] == "jpg":
                    old_path_every = old_path_all + "/" + file_list[i]+"/" +file
                    print("jpg is in progress:",old_path_every)
                    mkdir("{}/JPEGImages".format(new_path))
                    move_file(old_path_every, "{}/JPEGImages".format(new_path), 1)
                elif file.split(".")[1] == "xml":
                    old_path_every = old_path_all + "/" + file_list[i]+"/" +file
                    print("xml is in progress:",old_path_every)
                    mkdir("{}/Annotations".format(new_path))
                    move_file(old_path_every, "{}/Annotations".format(new_path), 1)
                else:
                    pass



import os

'''这个就是一个简单的创建文件夹的函数'''


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        pass


if __name__ == '__main__':
    move_all_file("","")

