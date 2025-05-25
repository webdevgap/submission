def resize_and_centercrop224(img):
        original_width, original_height = img.size
        target_width, target_height = (224, 224)

        # Calculate aspect ratios
        original_aspect = original_width / original_height
        target_aspect = target_width / target_height

        if original_aspect > target_aspect:
            # Original image is wider than target: Resize based on height
            new_height = target_height
            new_width = int(new_height * original_aspect)
        else:
            # Original image is taller than target (or same aspect): Resize based on width
            new_width = target_width
            new_height = int(new_width / original_aspect)

        # Resize the image
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Calculate coordinates for centercropping
        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        # Crop the image
        img_cropped = img_resized.crop((left, top, right, bottom))

        return img_cropped
        
def preprocess_images(input_dir, output_dir, size=224):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        img = Image.open(os.path.join(input_dir, filename)).convert("RGB")
        img = resize_and_centercrop224(img)
        img.save(os.path.join(output_dir, filename))

# Preprocess images
preprocess_images("/kaggle/input/soil-classification-part-2/soil_competition-2025/train", "train_resized")