import glob
import os
import shutil

all_jpg_files = glob.glob("images/*.jpg")
print(all_jpg_files)


pages = []

for image in all_jpg_files:
    file_path = image
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    shutil.copy(image, "docs/%s" % image)
    pages.append(
        {
            "image_path": image,
            "image_path_docs": "docs/%s" % image,
            "title": "%s image" % name_only,
            "output": "docs/%s.html" % name_only,
            "output_filename": "%s.html" %name_only,
        }
    )


def build_template(title):
    template = open('templates/base.html').read()
    ready_template = template.replace('{{title}}', title)
    return ready_template

print(pages)





#    file_path = "images/first.jpg"
#    file_name = os.path.basename(file_path)
#    print(file_name)
#    name_only, extension = os.path.splitext(file_name)
#    print(name_only)

