from caption.core.processor import ImageProcessModel


def test_image_caption():

    model_path = "Salesforce/blip-image-captioning-base"
    model = ImageProcessModel(model_path)
    output = model.process_image("./image/EyWy2QhWgAAwXoB.jpg")
    print(output)


test_image_caption()
