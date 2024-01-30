import os

def Rename_file():
    location = "D:\Meme" #เลือกไดร์
    dir_list = os.listdir(location)
    os.chdir(location)
    i = 1

    for filename in dir_list:
        newname = "This_is_Picture"  # ชื่อที่จะนำมาใส่แทนชื่อเดิม
        name1 = "{}_{:03d}.png".format(newname, i) #{:01d}ใช้กำหนดความยาวตัวเลข
        os.rename(filename , name1)
        
        i +=1
    print(f"\n\n\nChange_Nam_Succes\n   \m/*.*\m/\n\n\n")
if __name__ == "__main__" :
     Rename_file()