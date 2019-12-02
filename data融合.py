import os,shutil

level="L23"
path="D:\\1\\"
path2="D:\\2\\"

result=os.listdir(path)

if not os.path.exists(path2+str(level)):
    os.mkdir(path2+str(level))

if not os.path.exists(path2+str(level)+"\\image"):
    os.mkdir(path2+str(level)+"\\image")
for file in result:
    if os.path.isdir(path+str(file)):
        print(file)
        result1 = os.listdir(path+str(file))
        result2 = os.listdir(path + str(file)+"\\image")
        for file1 in result1:
            if str(level) in file1:
                shutil.copyfile(path+str(file)+"\\"+file1,path2+str(level)+"\\"+file1)
                print(file1)
        for file2 in result2:
            if str(level) in file2:
                shutil.copyfile(path+str(file)+"\\image\\"+file2,path2+str(level)+"\\image\\"+file2)
                print(file2)