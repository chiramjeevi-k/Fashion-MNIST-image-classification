
from pathlib import Path
from PIL import Image
from tensorflow.keras.datasets import fashion_mnist

class_names = [
    "T-shirt_top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle_boot"
]

(_, _), (test_images, test_labels) = fashion_mnist.load_data()

output_dir = Path("test_images/more_samples")
output_dir.mkdir(parents=True, exist_ok=True)

saved = 0

for class_id, class_name in enumerate(class_names):
    indices = [
        i for i, label in enumerate(test_labels)
        if label == class_id
    ][:3]

    for number, index in enumerate(indices, start=1):
        image = Image.fromarray(test_images[index])
        image.save(output_dir / f"{class_name}_{number}.png")
        saved += 1

print(f"Saved {saved} images to {output_dir.resolve()}")
