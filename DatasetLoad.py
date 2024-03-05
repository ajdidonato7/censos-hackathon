# Download the dataset
import os
from pathlib import Path
from datasets import load_dataset
dataset = load_dataset("Abhijit85/InsuranceClaimImages")


folder = 'insurance_claim_images'
path = Path(folder)
if not path.exists():
    os.mkdir(folder)

# Writes dataset to file
for i in range(len(dataset['01-minor']["image"])):
    image = dataset['01-minor']["image"][i]
    image_name = str('car_damage/')+str('01-minor')+str(i)+str('.jpg')
    # Check if file exists
    file = Path(image_name)
    if not file.exists():

        # File does not exist, write image
        image.save(image_name)

    else:

        # File already exists, skip writing
        print(f'{image_name} already exists, skipping...')