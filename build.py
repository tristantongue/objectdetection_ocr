import glob
import os
import shutil
from jinja2 import Template
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import face_recognition

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
#print(pages)

def main():
    for page in pages:
        template_html = open("templates/base.html").read()
        template = Template(template_html)  
        page_output = page["output"]
        tess_image = Image.open(page["image_path"])
        detected_text = pytesseract.image_to_string(tess_image, lang="eng")
        face_image = face_recognition.load_image_file(page["image_path"])
        face_locations = face_recognition.face_locations(face_image)
        image_height = tess_image.height
        image_width = tess_image.width
        print(image_height)
        print(image_width)
        print(face_locations)
        print(detected_text)
        open(page_output, "w+").write(template.render(
            pages = pages,
            title = page["title"],
            image_source = page["image_path"],
            detected_text = detected_text,
            face_locations = face_locations,
            image_height = image_height,
            image_width = image_width,
            ))

main()


#    file_path = "images/first.jpg"
#    file_name = os.path.basename(file_path)
#    print(file_name)
#    name_only, extension = os.path.splitext(file_name)
#    print(name_only)

