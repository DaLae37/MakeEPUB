import os

os.makedirs("Result", exist_ok = True)
filename = input("Input File Name(.txt) : ")
if filename in os.listdir("./") :
    with open(filename, "r") as file :
        with open("Result/"+filename, "w") as newfile :
            data = file.read()
            key = 0
            index = 0
            while key != -1 :
                index = key + 1
                key = data.find("\n", index)
                if key != -1 :
                    newfile.write("<p>" + data[index:key] + "</p>")
            newfile.write("<p>" + data[index:] + "</p>")
    print("Finish!")
else :
    print("Can't Find " + filename + "!")