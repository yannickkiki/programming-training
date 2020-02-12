class Slideshow():
    def __init__(self):
        self.slides = list()

class Slide():
    def __init__(self):
        self.photos = list()
        self.tags = list()

class Photo():
    def __init__(self, alignment, tags):
        self.alignment = alignment
        self.tags = tags


if __name__ == "__main__":
    dataset = "a_example.txt"
    with open(dataset, "r") as f:
        n_photos = int(f.readline())
        photos = list()
        for _ in range(n_photos):
            alignment, n_tags, *tags = f.readline().split()
            photos.append(Photo(alignment, tags))
