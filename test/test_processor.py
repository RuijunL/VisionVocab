from src.processor import ImageProcessModel

def image_test():

    model_path = "Salesforce/blip-image-captioning-base"
    model = ImageProcessModel(model_path)
    output = model.process_image("test/image/EyWy2QhWgAAwXoB.jpg")
    print(output)

image_test()