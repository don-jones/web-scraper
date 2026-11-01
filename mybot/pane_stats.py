import matplotlib.pyplot as plt
from generate_data import generate_random_paragraphs
from typing import TypedDict

class BoundingBox(TypedDict):
    upper: float
    lower: float

class PaneObject(TypedDict):
    bounding_box: BoundingBox
    fontsize: int
    lines: int
    width: int

class Pane(TypedDict):
    job_stats: PaneObject
    title: PaneObject
    rate_job_length: PaneObject
    us_only: PaneObject
    description: PaneObject
    skills: PaneObject
    client_stats: PaneObject

def normalize(x: float, offset_bot: float, offset_top: float) -> float:
    return x / (offset_bot - offset_top)

def pane_offsets() -> Pane:
    # 1. Single source of truth explicitly matching the Pane TypedDict structure
    pane_data: Pane = {
        "job_stats":       {"bounding_box": {"upper": 1.34, "lower": 1.50}, "fontsize": 12, "lines": 1, "width": 40},
        "title":           {"bounding_box": {"upper": 1.58, "lower": 1.78}, "fontsize": 18, "lines": 1, "width": 40},
        "rate_job_length": {"bounding_box": {"upper": 1.88, "lower": 2.05}, "fontsize": 14, "lines": 1, "width": 40},
        "us_only":         {"bounding_box": {"upper": 2.14, "lower": 2.36}, "fontsize": 14, "lines": 1, "width": 40},
        "description":     {"bounding_box": {"upper": 2.50, "lower": 2.85}, "fontsize": 12, "lines": 3, "width": 80},
        "skills":          {"bounding_box": {"upper": 3.03, "lower": 3.41}, "fontsize": 16, "lines": 1, "width": 40},
        "client_stats":    {"bounding_box": {"upper": 3.52, "lower": 3.70}, "fontsize": 14, "lines": 1, "width": 40},
    }

    offset_top = 0.94
    offset_bot = 3.88

    # 2. Modern dict comprehension that safely builds the nested bounding_box copies
    return {
        key: {
            **item,  # Preserves fontsize, lines, and width seamlessly
            "bounding_box": {
                pos: normalize(offset_bot - val, offset_bot, offset_top)
                for pos, val in item["bounding_box"].items()
            }
        }
        for key, item in pane_data.items()
    }  # Type checked safely back as a complete Pane dictionary

def main():
    pane_objects = pane_offsets()

    # The figure height matches your exact normalization scale factor (3.88 - 0.94 = 2.94)
    fig = plt.figure(figsize=(9.59, 2.94))

    axes_dict = {}
    
    for key, item in pane_objects.items():
        print(key, item)
        
        # 1. Pull upper and lower values from the inner bounding_box dictionary
        bbox = item["bounding_box"]
        upper = bbox["upper"]
        lower = bbox["lower"]
        
        # 2. Calculate the bounding height for the axis bounds
        height = upper - lower
        
        # 3. Add axes using the normalized coordinates [left, bottom, width, height]
        axes_dict[key] = fig.add_axes([0.1, lower, 0.8, height])
        axes_dict[key].axis('off')

        # 4. Correctly extract lines, width, and fontsize from the outer item
        item_text = generate_random_paragraphs(
            lines=item["lines"],
            width=item["width"]
        )

        axes_dict[key].text(x=0, y=0, s=item_text, fontsize=item["fontsize"])

    plt.show()

if __name__ == '__main__':
    main()
