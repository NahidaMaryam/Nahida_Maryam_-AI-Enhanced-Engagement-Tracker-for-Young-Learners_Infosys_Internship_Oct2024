import os
import shutil

def segregate_images_by_labels(image_dir, label_dir, matched_dir, unmatched_dir, img_ext=".jpeg", label_ext=".txt"):
    # Create directories if they don't exist
    os.makedirs(matched_dir, exist_ok=True)
    os.makedirs(unmatched_dir, exist_ok=True)

    # Get sets of file names without extensions
    image_files = {os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith(img_ext)}
    label_files = {os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith(label_ext)}

    # Find matched and unmatched images
    matched_images = image_files & label_files
    unmatched_images = image_files - label_files

    # Move matched images and labels to the matched folder
    for image_name in matched_images:
        img_path = os.path.join(image_dir, f"{image_name}{img_ext}")
        label_path = os.path.join(label_dir, f"{image_name}{label_ext}")
        
        shutil.move(img_path, os.path.join(matched_dir, f"{image_name}{img_ext}"))
        shutil.move(label_path, os.path.join(matched_dir, f"{image_name}{label_ext}"))
        print(f"Moved matched: {image_name}")

    # Move unmatched images to the unmatched folder
    for image_name in unmatched_images:
        img_path = os.path.join(image_dir, f"{image_name}{img_ext}")
        
        shutil.move(img_path, os.path.join(unmatched_dir, f"{image_name}{img_ext}"))
        print(f"Moved unmatched image: {image_name}")

# Define your directories
image_dir = 'img'
label_dir = 'lab'
matched_dir = '/home/maryam/python projects/annotations/matched'
unmatched_dir = '/home/maryam/python projects/annotations/unmatched'

segregate_images_by_labels(image_dir, label_dir, matched_dir, unmatched_dir)