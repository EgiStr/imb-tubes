import os
import base64


def image_to_base64(path_url):
    # get image from path base __file__
    abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), path_url))

    with open(abs_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        base64_string = "data:image/png;base64," + encoded_string
    return base64_string


def get_preview_image(image):
    # check if image is not None and image is not empty
    # convert image to base64 and return in html format
    if image is not None and image != "":
        image = image.read()
        image = base64.b64encode(image).decode("utf-8")
        return f'<img style="width:800px;" src="data:image/png;base64,{image}" class="img-fluid" alt="...">'
    else:
        return ""


def upload_image_to_folder(image):
    # check if image is not None and image is not empty
    if image is not None and image != "":
        # create folder if not exist
        if not os.path.exists("./images"):
            os.makedirs("./images")
        # save image to folder

        with open(f"./images/{image.name}", "wb") as fh:
            fh.write(image.getbuffer())
        return f"images/{image.name}"
    else:
        return ""
