import matplotlib.pyplot as plt
from generate_data import BoundingBox, TextBlock, MetaBadge, SkillChip, JobPane 
from generate_data import generate_random_paragraphs, generate_top_badge_text, generate_job_specs_text
import textwrap
import random

from typing import TypedDict, List

def normalize_y(y: float, offset_bot: float, offset_top: float) -> float:
    """Scales visual element coordinates cleanly within the viewport."""
    return (offset_bot - y) / (offset_bot - offset_top)

def generate_upwork_pane_offsets() -> JobPane:
    # Baseline layout parameters from the canvas frame
    offset_top = 0.5
    offset_bot = 5.5

    top_badge_text_1, top_badge_text_2 = generate_top_badge_text()
    ar_flag = False

    raw_data: JobPane = {
        "top_badge": {
            "label": f"{top_badge_text_1} • {top_badge_text_2}",
            "bounding_box": {"upper": 0.72, "lower": 0.95},
            "fontsize": 10,
            "width": 35,
            "actively_recruiting": ar_flag
        },
        "title": {
            "text": generate_random_paragraphs(lines=1, width=random.randint(20,50)),
            "bounding_box": {"upper": 1.15, "lower": 1.45},
            "fontsize": 18,
            "width": 50
        },
        "job_specs": {
            "text": generate_job_specs_text(), 
            "bounding_box": {"upper": 1.65, "lower": 1.90},
            "fontsize": 12,
            "width": 75
        },
        "location_req": {
            "text": "Only freelancers located in the United States may apply.",
            "bounding_box": {"upper": 2.10, "lower": 2.35},
            "fontsize": 12,
            "width": 75
        },
        "description": {
            "text": "Seeking an electric engineer to support a project in New York State. "
                    "The role involves reviewing electrical systems, identifying issues, "
                    "and recommending solutions. You will collaborate with project teams "
                    "to ensure designs meet requirements and help maintain project timelines.",
            "bounding_box": {"upper": 2.65, "lower": 3.75},
            "fontsize": 12,
            "width": 95
        },
        "skills_list": [
            {"name": "Electrical Engineering", "bounding_box": {"upper": 4.10, "lower": 4.50}, "width": 18},
            {"name": "CAD", "bounding_box": {"upper": 4.10, "lower": 4.50}, "width": 6},
            {"name": "Mechanical Engineering", "bounding_box": {"upper": 4.10, "lower": 4.50}, "width": 19},
            {"name": "Civil Engineering", "bounding_box": {"upper": 4.10, "lower": 4.50}, "width": 15}
        ],
        "footer_stats": {
            "label": "Actively recruiting   •   Payment verified   •   4.7   •   United States",
            "bounding_box": {"upper": 4.90, "lower": 5.20},
            "fontsize": 11,
            "width": 80
        }
    }

    # Normalize single structures and array chips programmatically
    normalized_pane: JobPane = {}
    for key, item in raw_data.items():
        if isinstance(item, list):
            normalized_pane[key] = [
                {
                    **chip,
                    "bounding_box": {
                        pos: normalize_y(val, offset_bot, offset_top)
                        for pos, val in chip["bounding_box"].items()
                    }
                } for chip in item
            ]
        else:
            normalized_pane[key] = {
                **item,
                "bounding_box": {
                    pos: normalize_y(val, offset_bot, offset_top)
                    for pos, val in item["bounding_box"].items()
                }
            }

    return normalized_pane

import matplotlib.pyplot as plt
import textwrap

# Ensure the previous definitions (TypedDicts and generate_upwork_pane_offsets) are imported/available

def draw_job_card():
    pane_data = generate_upwork_pane_offsets()
    
    # Target dimension scale matching an aspect ratio close to the input image card
    fig, ax = plt.subplots(figsize=(11.0, 4.0))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1) # Normalized height viewport
    ax.axis('off')
    
    # Configure overall design card borders
    bbox_props = dict(boxstyle="round,pad=0.6", fc="white", ec="#e4e4e7", lw=1.5)
    ax.text(0, 0, "", bbox=bbox_props, transform=ax.transAxes)

    # 1. Top Status Badge
    top = pane_data["top_badge"]
    ax.text(
        x=2, y=top["bounding_box"]["lower"], s=top["label"], 
        fontsize=top["fontsize"], color="#2563eb", weight="semibold",
        bbox=dict(boxstyle="round,pad=0.3", fc="#eff6ff", ec="none")
    )
    
    # 2. Main Job Title Title
    title = pane_data["title"]
    ax.text(
        x=2, y=title["bounding_box"]["lower"], s=title["text"], 
        fontsize=title["fontsize"], color="#0f172a", weight="bold",
        wrap=True
    )
    
    # 3. Contextual Job Specifications
    specs = pane_data["job_specs"]
    ax.text(
        x=2, y=specs["bounding_box"]["lower"], s=specs["text"], 
        fontsize=specs["fontsize"], color="#475569"
    )
    
    # 4. Mandatory Geo Location Constraint
    loc = pane_data["location_req"]
    ax.text(
        x=2, y=loc["bounding_box"]["lower"], s=f"📍 {loc['text']}", 
        fontsize=loc["fontsize"], color="#475569", weight="medium"
    )
    
    # 5. Multiline Core Paragraph Description Block
    desc = pane_data["description"]
    wrapped_lines = textwrap.wrap(desc["text"], width=int(desc["width"]))
    wrapped_text = "\n".join(wrapped_lines)
    
    ax.text(
        x=2, y=desc["bounding_box"]["lower"], s=wrapped_text, 
        fontsize=desc["fontsize"], color="#334155", linespacing=1.4,
        va="bottom"
    )
    
    # 6. Categorical Horizontal Skill Chips
    current_x = 2
    for chip in pane_data["skills_list"]:
        y_pos = chip["bounding_box"]["lower"]
        
        # Draw background patch label container
        ax.text(
            x=current_x, y=y_pos, s=chip["name"], 
            fontsize=10, color="#1e293b", weight="bold",
            bbox=dict(boxstyle="round,pad=0.8", fc="#f1f5f9", ec="none")
        )
        # Advance layout pointer contextually via targeted width
        current_x += chip["width"] + 1.5
        
    # 7. Verification Footer Row Data
    footer = pane_data["footer_stats"]
    ax.text(
        x=2, y=footer["bounding_box"]["lower"], s=footer["label"], 
        fontsize=footer["fontsize"], color="#64748b", weight="medium"
    )

    bkgd_img = plt.imread('job_pane_generic.png')
    ax.imshow(bkgd_img, extent=[0, 100, 0, 1], aspect='auto', zorder=-10)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    for i in range(3):
        draw_job_card()
