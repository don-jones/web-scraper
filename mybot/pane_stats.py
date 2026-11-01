import matplotlib.pyplot as plt
from generate_data import generate_random_paragraphs
from typing import TypedDict

class BoundingBox(TypedDict):
    upper : float
    lower : float

class PaneObject(TypedDict):
    bounding_box : BoundingBox
    fontsize : int
    lines : int
    width : int

class Pane(TypedDict):
    job_stats : PaneObject
    title : PaneObject
    rate_job_length : PaneObject
    us_only : PaneObject
    description : PaneObject
    skills : PaneObject
    client_stats : PaneObject

def normalize(x, offset_bot, offset_top):
    return x / (offset_bot - offset_top)

def pane_offsets():
    pane_objects = { "job_stats" : { "upper" : 1.34 ,
                                     "lower" : 1.5,
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 },
                    "title" :{ "upper" : 1.58 ,
                                     "lower" : 1.78,
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 },

                    "rate_job_length" : { "upper" : 1.88 ,
                                     "lower" : 2.05,
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 },

                    "us_only" : { "upper" : 2.14 ,
                                     "lower" : 2.36,
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 },

                    "description" : { "upper" : 2.5 ,
                                     "lower" : 2.85,
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 },

                    "skills" : { "upper" : 3.03 ,
                                     "lower" : 3.41,
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 },

                    "client_stats" : { "upper" : 3.52 ,
                                     "lower" : 3.7,
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 }
}

    pane_objects: Pane = {
        "job_stats" : { "bounding_box" : {"upper" : 1.34 ,
                                     "lower" : 1.5},
                                     "fontsize" : 12,
                                     "lines" : 1,
                                     "width" : 40 }
    }                
    offset_top = 0.94
    offset_bot = 3.88

    pane_objects_offset = {}

    for key, item in pane_objects.items():
        pane_objects_offset[key] = {}

        for position, value in item['bounding_box'].items():
            offset_value = offset_bot - value

            normalized_value = normalize(offset_value,
                                         offset_bot,
                                         offset_top)

            pane_objects_offset[key] 
            pane_objects_offset[key]['bounding_box'][position] = normalized_value

    return pane_objects_offset

def main():
    pane_objects = pane_offsets()

    fig = plt.figure(figsize=(9.59, 2.94))

    axes_dict = {}
    
    for key, item in pane_objects.items():
        print(key, item)
        height = item["upper"] - item["lower"]
        axes_dict[key] = fig.add_axes([0.1, item["lower"], 0.8, height])
        axes_dict[key].axis('off')

        item_text = generate_random_paragraphs(lines=item["lines"],
                                               width=item["width"])

        axes_dict[key].text(x=0, y=0, s=item_text, fontsize=item["fontsize"])

    plt.show()

if __name__ == '__main__':
    main()
