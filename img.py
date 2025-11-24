import os
from PIL import Image

def resize_images(input_folder, output_folder, size, output_format="JPEG"):
    """
    Resize and convert images in batch.
     input_folder: Folder containing original images
     output_folder: Folder where resized images will be saved
     size: New size (width, height) entered by user
     output_format: Format to save images (JPEG, PNG, WEBP)
    """

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    supported_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_extensions):

            try:
                image_path = os.path.join(input_folder, filename)
                img = Image.open(image_path)

                
                img_resized = img.resize(size)

                base_name = os.path.splitext(filename)[0]
                new_filename = f"{base_name}_resized.{output_format.lower()}"
                output_path = os.path.join(output_folder, new_filename)

                img_resized.save(output_path, output_format)

                print(f"✔ Saved: {output_path}")

            except Exception as e:
                print(f"❌ Error processing {filename}: {str(e)}")


if __name__ == "__main__":
    input_folder = "inp_img"
    output_folder = "op_img"

    # User enters width and height
    print("Enter new size for images:")
    width = int(input("Width: "))
    height = int(input("Height: "))

    # User chooses format
    print("\nChoose output format: JPEG / PNG / WEBP")
    format_to_convert = input("Format: ").upper()
    new_size = (width, height)

    resize_images(input_folder, output_folder, new_size, format_to_convert)
