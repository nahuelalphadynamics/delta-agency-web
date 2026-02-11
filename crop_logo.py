from PIL import Image, ImageOps
import numpy as np

def crop_and_remove_black_bg(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        newData = []
        # Threshold for BLACK background removal (keep white/bright pixels)
        threshold = 50 
        
        for item in datas:
            # If pixel is dark (black background), make it transparent
            if item[0] < threshold and item[1] < threshold and item[2] < threshold:
                newData.append((0, 0, 0, 0)) # Make Transparent
            else:
                newData.append(item) # Keep original pixel (likely white)

        img.putdata(newData)
        
        # Now crop based on alpha channel (content is the white triangle)
        bbox = img.getbbox()
        
        if bbox:
            cropped_img = img.crop(bbox)
            cropped_img.save(output_path)
            print(f"Successfully removed black bg and cropped to {bbox}")
        else:
            print("Failed to find content (all black?).")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    crop_and_remove_black_bg("public/isologo_delta.jpg", "public/isologo_delta_cropped.png")
