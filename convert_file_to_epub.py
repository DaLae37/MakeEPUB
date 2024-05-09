import os
import shutil

os.makedirs("Result", exist_ok = True)
print("Convert to .EPUB files")
for file in os.listdir("./") :
    if file == "Result" :
        continue
    else :
        if os.path.isdir(file) :
            title = ""
            try :
                meta_dir = file + "/OEBPS/content.opf"
                with open(meta_dir, "r") as meta_file :
                    data = meta_file.read()
                    start = data.find("<dc:title>")
                    end = data.find("</dc:title>")
                    title = data[start + len("<dc:title>"):end]
            except :
                continue
            else :
                shutil.make_archive(title, "zip", file)
                shutil.move(title+".zip", "Result/"+title+".epub")
        else :
            title = file.split(".")[0]
            print(title)
print("Finish!")