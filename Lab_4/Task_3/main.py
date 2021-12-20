from classes import *


def main():
    t1 = Teacher("Daniil", "Dankovsky", "+380678923165")
    t2 = Teacher("Artemy", "Burakh", "+380932378217")
    c1 = CourseFactory().create_course("Java/Spring",  "Local", ['Java', 'Spring', 'JavaScript'], t1)
    c2 = CourseFactory().create_course("Full-stack Development",  "Offsite", ['Front-end', 'Back-end'], t2)
    print(c1)
    print(c2)

    """
    Adding info to database.
    """
    # try:
    #     CourseFactory.add_teacher(t1)
    #     CourseFactory.add_teacher(t2)
    #     CourseFactory.add_course(c1)
    #     CourseFactory.add_course(c2)
    # except Exception as e:
    #     print(e)

    """
    Getting information from database.
    """
    try:
        print("\tAll courses:\n", CourseFactory.get_courses())
        print("\tAll teachers:\n", CourseFactory.get_teachers())
        print("\nFind course teacher Daniil: ", CourseFactory.find_course("Daniil"))
        print("\nFind course teacher Pavel: ", CourseFactory.find_course("Pavel"))
    except Exception as e:
        print(e)


main()
