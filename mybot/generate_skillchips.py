from generate_data import generate_random_paragraphs
from generate_data import SkillChip
import random

def generate_skills_list():
    num_skillchips = random.randint(1,10)

    skills_list = []

    for i in range(num_skillchips):
        word_size = random.randint(3,10)

        skillchip_name = generate_random_paragraphs(lines=1, width=word_size)

        skillchip_bbox = {"upper" : 4.10, "lower" : 4.50}

        skillchip_width = word_size

        skillchip = {"name" : skillchip_name,
                     "bounding_box" : skillchip_bbox,
                     "width" : skillchip_width }

        skills_list.append(skillchip)

    return skills_list

def main():
    skills_list = generate_skills_list()

    print(skills_list)

if __name__ == '__main__':
    main()
