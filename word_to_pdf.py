from docx2pdf import convert

# import OS module
import os
import shutil

path = os.getcwd()
dir_list = os.listdir(path)
pdf_lst = []
condition = True

while condition:
    # Get the list of all files and directories
    for i in dir_list:
        if "docx" in i:
            convert(i, i.replace("docx", "pdf"))
            pdf_lst.append(i.replace("docx", "pdf"))
    condition = False

for i in pdf_lst[1::]:
    current = path + "/" + f"{i}"
    destination = path + "/pdf/" + f"{i}"
    shutil.move(current, destination)
 



# convert(r"Đồ án tốt nghiệp.docx", r"Đồ án tốt nghiệp.pdf")