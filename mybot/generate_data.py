import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, findfont, get_font
import random
import string

from typing import TypedDict, List

class BoundingBox(TypedDict):
    upper: float
    lower: float

class TextBlock(TypedDict):
    text: str
    bounding_box: BoundingBox
    fontsize: int
    width: int

class MetaBadge(TypedDict):
    label: str
    bounding_box: BoundingBox
    fontsize: int
    width: int

class SkillChip(TypedDict):
    name: str
    bounding_box: BoundingBox
    width: int
    fontsize: int
    text_width: int

class JobPane(TypedDict):
    top_badge: MetaBadge       # e.g., "Posted yesterday • Proposals: 5 to 10"
    title: TextBlock           # e.g., "Electric Engineer in New York"
    job_specs: TextBlock       # e.g., "Fixed-price: $5,000 | Intermediate | ..."
    location_req: TextBlock    # e.g., "Only freelancers located in the United States..."
    description: TextBlock     # Core job text paragraphs
    skills_list: List[SkillChip] # Tag layout chips
    footer_stats: MetaBadge    # e.g., "Actively recruiting • Payment verified..."

def estimate_text_size(text, fontsize, dpi=100):
    """
    Estimates the width and height of a string in pixels without rendering a canvas.
    """
    # 1. Grab font properties and locate the font file
    props = FontProperties(size=fontsize)
    font_path = findfont(props)
    
    # 2. Load the font using Matplotlib's internal FT2Font engine
    font = get_font(font_path)
    
    # 3. Set the font size context (Matplotlib scales points to DPI internally)
    font.set_size(fontsize, dpi)
    
    # 4. Load the text string into the engine to calculate dimensions
    # 'angle=0' means no rotation.
    font.set_text(text, 0.0)
    
    # 5. Retrieve dimensions (returns width and height in 1/64th subpixels)
    w_subpixels, h_subpixels = font.get_width_height()
    
    # 6. Convert subpixels back to standard display pixels
    width_pixels = w_subpixels / 64.0
    height_pixels = h_subpixels / 64.0
    
    return width_pixels, height_pixels

def generate_skills_list():
    skillchip_fontsize = 12
    num_skillchips = random.randint(1,5)
    skills_list = []

    for i in range(num_skillchips):
        word_size = random.randint(3,20)

        skillchip_name = generate_random_paragraphs(lines=1, width=word_size)

        skillchip_text_width = estimate_text_size(skillchip_name,
                                                  skillchip_fontsize,
                                                  20)[0] 

        skillchip_bbox = {"upper" : 4.10, "lower" : 4.50}

        skillchip_width = word_size

        skillchip = {"name" : skillchip_name,
                     "bounding_box" : skillchip_bbox,
                     "width" : skillchip_width,
                     "fontsize" : skillchip_fontsize,
                     "text_width" : skillchip_text_width}

        skills_list.append(skillchip)

    return skills_list
def generate_top_badge_text():
    mhd = random.randint(1,4)

    text_1 = ""

    text_2 = ""

    if mhd == 1:
        MHD = random.randint(1,24)

        text_1 = f"Posted {MHD} hours ago"

    elif mhd == 2:
        MHD = random.randint(1,60)

        text_1 = f"Posted {MHD} minutes ago"

    elif mhd == 3:
        text_1 = f"Posted yesterday"

    elif mhd == 4:
        MHD = random.randint(2,30)

        text_1 = f"Posted {MHD} days ago"


    prop = random.randint(1,4)

    if prop == 1:
        text_2 = f"Proposals: Fewer than 5"

    elif prop == 2:
        text_2 = f"Proposals: 5 to 10"

    elif prop == 3:
        text_2 = f"Proposals: 20 to 50"

    elif prop == 4:
        text_2 = f"Proposals: 50+"

    return text_1, text_2

def generate_job_specs_text():
    hf = random.randint(1,3)

    estimated_time = {1 : f"Est. Time: Less than 1 week",
                      2 : f"Est. Time: 3 to 6 months",
                      3 : f"Est. Time: Less than 1 month",
                      4 : f"Est. Time: More than 6 months",
                      5 : f"Est. Time: 1 to 3 months" }

    skill_level = {1 : "Entry level", 2: "Intermediate", 3 : "Expert"}

    hours_per_week = {1 : "Less than 30 hrs/week",
                      2: "30+ hrs/week"}
                  
    if hf == 1:
        SKILL_LEVEL = skill_level[random.randint(1,3)]

        ESTIMATED_TIME = estimated_time[random.randint(1,5)]

        FIXED_PRICE = random.randint(1,1000) * 5

        text_1 = f"Fixed-price: ${FIXED_PRICE}   |   {SKILL_LEVEL}   |   {ESTIMATED_TIME}" 

    if hf == 2:
        SKILL_LEVEL = skill_level[random.randint(1,3)]

        ESTIMATED_TIME = estimated_time[random.randint(1,5)]

        HOURS_PER_WEEK = hours_per_week[random.randint(1,2)]

        text_1 = f"Hourly   |   {SKILL_LEVEL}   |   {ESTIMATED_TIME}   |   {HOURS_PER_WEEK}" 
    if hf == 3:
        SKILL_LEVEL = skill_level[random.randint(1,3)]

        ESTIMATED_TIME = estimated_time[random.randint(1,5)]

        HOURS_PER_WEEK = hours_per_week[random.randint(1,2)]

        RATE_1 = random.randint(1,10) * 5

        RATE_2 = RATE_1 + random.randint(1,10) * 5

        text_1 = f'Hourly: {RATE_1}-{RATE_2}   |   {SKILL_LEVEL}   |   {ESTIMATED_TIME}   |   {HOURS_PER_WEEK}' 

    return text_1

def generate_random_paragraphs(lines=1, width=80):
    # Characters to use for the "words"
    chars = string.ascii_letters + string.digits
    output_lines = []
    
    for _ in range(lines):
        line_chars = []
        current_len = 0
        
        while current_len < width:
            # Randomly determine a realistic word length (2 to 8 characters)
            word_len = random.randint(2, 8)
            
            # Ensure we don't overshoot the maximum line width
            if current_len + word_len > width:
                word_len = width - current_len
                
            # Generate the word fragments
            line_chars.extend(random.choices(chars, k=word_len))
            current_len += word_len
            
            # Add a single trailing space if there is still room left on the line
            if current_len < width:
                line_chars.append(" ")
                current_len += 1
                
        output_lines.append("".join(line_chars))
        
    return "\n".join(output_lines)

def main():
    fig = plt.figure(figsize=(10, 4))

    axis_bkgd = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axis_title = fig.add_axes([0.1, 0.7, 0.4, 0.1])
    axis_title.patch.set_alpha(0.0)
    axis_title.axis('off')
    text_1 = generate_random_paragraphs(lines=1, width=40)
    axis_title.text(x=0, y=0, s=text_1, fontsize=18)




    axis_2 = fig.add_axes([0.1, 0.3, 0.4, 0.2])

    # 3. Make the foreground axes completely transparent so the image shows through
    axis_2.patch.set_alpha(0.0)

    # Optional: Hide the axes spines/ticks so only the text is visible over the image
    axis_2.axis('off')
    axis_bkgd.axis('off')                       # Hide the background axis frame lines

    # Populate your text
    text_2 = generate_random_paragraphs(lines=3, width=80)

    axis_2.text(x=0, y=0, s=text_2, fontsize=12)

    # Populate your background
    bkgd_img = plt.imread('job_pane_generic.png')
    axis_bkgd.imshow(bkgd_img, aspect='auto')  # aspect='auto' matches the image to your 0.8x0.8 box dimensions

    plt.show()

if __name__ == '__main__':
    main()
