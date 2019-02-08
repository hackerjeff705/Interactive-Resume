# Hello and welcome to my interactive resume.
# Please dowload the latest version of python.
# Download files in the repository.
#Github repository https://github.com/hackerjeff705/Interactive-Resume
# Place dowloads in one file and name it as interactive resume.
# Ideally, run the program on CMD as that is the only platform i have tested'
# To run program, change the directory to desired location.
# i.e. cd desktop, cd interactive resume, python resume.py.

rn = input('Recruiter Name: ')
print('Hi',rn,'thank you for your time\nWelcome to my interactive resume\n-------------------------\n' )

def prof(menu):
    intro = '-------------------------\nSelf-motivated adaptive learner who’s not afraid to get his hands and mind mucky\nwhen building ideas into reality to create a sustainable future for mankind. With\nmore than 1 year of experience in various industries food, manufacturing, biotech,\nmedical devices and research. With a strong aptitude in electronics and mechanical\nsystems, and an ever growing skill set in software.\n\nMy core competencies includes:\n'
    return intro

def edu(menu):
    B = '-------------------------\n\nBachelors of Mechanical and Medical Engineering\nGrade: 3.7 GPA with honours\nYear: 2014-2017\nLocation: Unversity of Hull, Hull, East Yorkshire, UK\n'
    return B

def cert(menu):
    cert = {
    'Coursera University of Michigan': ['Using Python to Access Web Data', 'Python Data Structures', 'Programming for Everybody (Getting Started with Python)'], 'MATLAB': ['Deep Learning Onramp Certificate'], 'Coursera University of California Irvine': ['The Arduino Platform and C Programming', 'Introduction to the Internet of Things and Embedded Systems'], 'Duke University': ['Fundamental Neuroscience for Neuroimaging'], 'John Hopkins University': ['Programming Fundamentals'], 'Premier Food Safety': ['California Food Handler Training Certificate Program']
    }
    return cert

def skill(menu):
    skill = {
    'Programming Language': ['Python', 'C Programming', 'SQL'], 'Language Tools': ['MATLAB', 'Anaconda', 'Atom', 'EEGlab', 'Octave'], 'Libraries': ['urlib', 'beutiful soup (BS4)', 'sqlite3'], 'Computer Science': ['JSON', 'XML', 'HTML', 'Deep Learning'], 'Engineering': ['Product Design', 'Project Management', 'Design Specification', 'Product Lifecycle'], 'Mathematics': ['Matrices', 'Control Theory', 'Algebra', 'Mechanics', 'Statistics', 'Calculus', 'Mechanics', 'Probability'], 'Other': ['Microsoft Office (Word, Excel, PowerPoint, Outlook, OneDrive)', 'Illustrator', 'Tagalog'], 'Manufacturing Tools': ['Thru-hole Soldering', 'Crimping', 'Mill', 'Lathe', 'MIG & TIG Welding', 'Power Tools', '3D Printing', 'Multimeter', 'Caliper', 'Drill Press', 'Router'],  'Hardware': ['Electronics', 'Bread Board', 'EEG', 'Arduino', 'Actuator', 'Motors', 'Sensors', 'Motorized Scooters', 'PCB'], 'Design': ['SolidWorks', 'AutoCAD', 'Fusion 360', 'DFM', 'GDT', 'KiCAD', 'ANSYS', 'FEA'], 'Manufacturing': ['Lean Manufacturing (JIT, Six SIGMA)', 'Work Instructions', 'Technical Files', 'BOMs'],
    }
    return skill

while True:
    print('What would you like to do:\n\nA) Profile & Competencies\nB) Education\nC) Technical Skills\nD) Work Experience\nE) Interest\nF) Exit\n')
    menu = input('Enter letter here: ')

    if menu == 'A' or menu == 'a':
        out = prof(menu)
        fo = open('competencies.txt')
        print(out)
        for line in fo:
            #print(line)
            if not line.startswith('Python') :
                continue
            else:
                line = line.split(', ')
                for item in line:
                    print('- ', item)
        print('\n-------------------------\n\n')

    elif menu == 'B' or menu == 'b':
        out = edu(menu)
        cert = cert(menu)
        print(out,'\n')
        print('Certification','\n')
        for k,v in cert.items():
            print(k,'\n',v,'\n')
        print('-------------------------\n\n')

    elif menu == 'C' or menu == 'c':
        skill = skill(menu)
        print('-------------------------\nAppicable Technical Skills\n')
        for k,v in skill.items():
            print(k,'\n',v,'\n')
        print('-------------------------\n\n')

    elif menu == 'D' or menu == 'd':
        xp = open('info.txt')
        rxp = xp.read()
        print(rxp)
        print('-------------------------\n\n')

    elif menu =='E' or menu == 'e':
        fo = open('competencies.txt')
        print('-------------------------\nInterests')
        for line in fo:
            #print(line)
            if not line.startswith('Former ') :
                continue
            else:
                line = line.split(', ')
                for item in line:
                    print('- ', item)
        print('-------------------------\n\n')

    elif menu == 'F' or menu == 'f':
        while True:
            print('Thank you for your time')
            fin = input('Would you hire this person (Yes/No): ')
            if fin == 'Yes' or fin == 'yes' or fin == 'YES':
                print('Great!\nLets go and solve the worlds problems!')
                break
            elif fin == 'No' or fin == 'no' or fin == 'NO':
                print('ERROR\nWrong input')
            else:
                print('Wrong input, please enter a letter')
        break

    else:
        print('Wrong input, please enter a letter')
