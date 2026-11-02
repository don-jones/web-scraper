from generate_data import generate_random_paragraphs, estimate_text_size
from generate_data import SkillChip, generate_skills_list
import random


def main():
    skills_list = generate_skills_list()

    for x in skills_list:
        print(x['name'], x['text_width'])

if __name__ == '__main__':
    main()
