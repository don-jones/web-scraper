from generate_data import generate_random_paragraphs, estimate_text_size
from generate_data import SkillChip
import random

def generate_skills_list():
    skillchip_fontsize = 12
    num_skillchips = random.randint(1,10)

    skills_list = []

    for i in range(num_skillchips):
        word_size = random.randint(3,20)

        skillchip_name = generate_random_paragraphs(lines=1, width=word_size)

        skillchip_text_width = estimate_text_size(skillchip_name,
                                                  skillchip_fontsize,
                                                  100)[0] 

        skillchip_bbox = {"upper" : 4.10, "lower" : 4.50}

        skillchip_width = word_size

        skillchip = {"name" : skillchip_name,
                     "bounding_box" : skillchip_bbox,
                     "width" : skillchip_width,
                     "fontsize" : skillchip_fontsize,
                     "text_width" : skillchip_text_width}

        skills_list.append(skillchip)

    return skills_list

def main():
    skills_list = generate_skills_list()

    for x in skills_list:
        print(x['name'], x['text_width'])

if __name__ == '__main__':
    main()
