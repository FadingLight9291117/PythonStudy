"统计英文文本单词个数"
def Englishwordcount(string):
    l = ''',.?;:'"!()\n'''
    for item in l:
        string = string.replace(item, "")
    b = string.split()
    print(b)
    return len(b)

    # '''数据清理'''
    # word="qwertyuiopasdfghjklzxcvbnm"
    # Word=word.upper()
    # for item in a:
    #   if item not in word and item not in Word and item !=' ' and item !='\n':
    #     print(item)
if __name__ == '__main__':
    a = '''Dear reviewers, I am a postgraduate 
        at Wuhan University of Science and Technology.
        I major in Computer Science and Technology.So, 
        as a student of CS, I have to improve my 
        programming skill to keep up the pace, or 
        I will be out of date just like computer 
        hardware. This course is an introductory 
        course in computer coding. And it’s easy 
        to understand. In addition, I think it would 
        be used in all aspects of life. The most 
        important reason is that my research direction 
        in the graduate student stage is create a program 
        by Python. I have to learn something about Python 
        and this course is a good choice. I love the course
        and it could be a wonderful experience for my 
        learning process. I am grateful to your help if 
        I get the Finance Aid. Thank you!'''
    print(Englishwordcount(a))
