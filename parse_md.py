
import markdown
import subprocess

# Variables 

input_file_location="Trail2.pdf"  # Write the file Name you want to Convert
output_file_location=""     # In the Output Folder 


def Convert():
    subprocess.run(["marker_single", input_file_location,output_file_location],shell=True)

def parse_markdown():
    with open(input_file_location.split(".")[0]+"/"+input_file_location.split(".")[0]+".md", 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Parse the Markdown content
    html_content = markdown.markdown(markdown_content)

    # Initialize data structures
    units = []
    lessons = []
    activities = []
    lesson_contents = []

    # Iterate through the Markdown content and extract the structure
    current_unit = None
    current_lesson = None
    current_lesson_content = []
    in_activity = False
    current_activity_name = None
    current_activity_content = []

    for line in markdown_content.split('\n'):
        #print(line)
        if line.startswith('# '):
            # Unit
            if current_lesson:
                # Store the previous lesson's content
                lesson_contents.append({'lesson': current_lesson, 'content': '\n'.join(current_lesson_content), 'activity': current_activity_name, 'activity_content': '\n'.join(current_activity_content)})
                current_lesson_content = []
                current_activity_name = None
                current_activity_content = []
            current_unit = line[2:].strip()
            units.append(current_unit)
            current_lesson = None
        
        elif line.startswith('## ') or line.startswith("### "):
            # Lesson
            if current_lesson:
                # Store the previous lesson's content
                lesson_contents.append({'lesson': current_lesson, 'content': '\n'.join(current_lesson_content), 'activity': current_activity_name, 'activity_content': '\n'.join(current_activity_content)})
                current_lesson_content = []
                current_activity_name = None
                current_activity_content = []
            current_lesson = line[3:].strip()
            lessons.append(current_lesson)
            in_activity=False
            if current_unit:
                # Link the lesson to the current unit
                lesson_index = len(lessons) - 1
                unit_index = units.index(current_unit)
                lessons[lesson_index] = {'title': current_lesson, 'unit': unit_index}
        
        # Differentialting between activity and lesson, logic is wrong here. 
        elif line.startswith('#### '):
            # Activity
            current_activity_name = line.strip()
            in_activity = True

        elif in_activity:
            # Activity content
            current_activity_content.append(line)
        

        else:
            # Lesson content
            if current_lesson:
                current_lesson_content.append(line)

    # Store the last lesson's content
    if current_lesson:
        lesson_contents.append({'lesson': current_lesson, 'content': '\n'.join(current_lesson_content), 'activity': current_activity_name, 'activity_content': '\n'.join(current_activity_content)})

    #for eachActivity in activities:
    #    print("Activity: ",eachActivity['content'])

    for  eachU in units:
        print("Unit",eachU)
    for eachL in lessons:
        print("Lesson",eachL)
    for eachLc in lesson_contents:
        print("Content",eachLc)


Convert()
parse_markdown()