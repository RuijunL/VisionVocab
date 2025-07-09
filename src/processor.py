from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


class ImageProcessModel:

    def __init__(self, path: str):

        try:
            self.processor = BlipProcessor.from_pretrained(path)
            self.model = BlipForConditionalGeneration.from_pretrained(path, use_safetensors= True)
        except:
            raise ValueError("Invalid model path")

    def process_image(self, image_path):

        try:
            raw_image = Image.open(image_path).convert("RGB")
        except:
            raise ValueError("The image can't be converted to RGB format")
        
        inputs = self.processor(raw_image, return_tensors="pt")
        output = self.model.generate(**inputs)
        caption = self.processor.decode(output[0], skip_special_tokens = True)
        
        return caption


        

