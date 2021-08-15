import webbrowser, os, pyautogui
from termcolor import colored

os.system('clear')

print(colored('HELLO FROM PYSITES COMMUNITY', 'red'))

language = 'en'
icon = '    <link rel="icon" href="icon">'

def set_language(language_code):
    global language
    language = language_code

def set_icon(icon_path):
    global icon
    icon = '    <link rel="icon" href="'+icon_path+'">'

html_file, css_file = open('index.html', 'a'), open('style.css', 'a')
basic_html, basic_css = '''<!---\n\n\nWritten By Using pysites Library please do not edit!--->\n<!---Contact Info--->\n<!---Mail: guvenkerem2006@gmail.com GitHub: https://github.com/kerem700916\nHAVE A NICE DAY\n\n\n--->\n\n\n<!DOCTYPE html>
<html lang="'''+language+'''">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>\n'''+icon+'''
</head>
<body>
        
</body>
</html><!---\n\n\nWritten By Using pysites Library please do not edit!--->\n<!---Contact Info--->\n<!---Mail: guvenkerem2006@gmail.com GitHub: https://github.com/kerem700916\nHAVE A NICE DAY\n\n\n\n--->''', '''* {
    margin:0;
    padding:0;
}'''
html_rules, css_rules = [], []
ruleofhtml, ruleofcss, elements, header_elements, div_elements, span_elements, footer_elements = '', '','', '', '', '', ''
paragraph_called = []
h1_called = []
h2_called = []
h3_called = []
h4_called = []
h5_called = []
h6_called = []
input_called = []
list_called = []
header_called = []
div_called = []
span_called = []
footer_called = []
paragraph_called2 = []
h1_called2 = []
h2_called2 = []
h3_called2 = []
h4_called2 = []
h5_called2 = []
h6_called2 = []
input_called2 = []
list_called2 = []
header_called2 = []
div_called2 = []
span_called2 = []
footer_called2 = []
paragraph_called3 = []
h1_called3 = []
h2_called3 = []
h3_called3 = []
h4_called3 = []
h5_called3 = []
h6_called3 = []
input_called3 = []
list_called3 = []
header_called3 = []
div_called3 = []
span_called3 = []
footer_called3 = []
paragraph_called4 = []
h1_called4 = []
h2_called4 = []
h3_called4 = []
h4_called4 = []
h5_called4 = []
h6_called4 = []
input_called4 = []
list_called4 = []
header_called4 = []
div_called4 = []
span_called4 = []
footer_called4 = []

def load_basic():
    html_file.truncate(0)
    css_file.truncate(0)
    html_file.write(basic_html)

def paragraph(text, classname):
    tag = "\n    <p class='" + classname + "'>" + text + '''</p>'''
    if "header/" in classname:
        paragraph_called.append(tag)
    if "div/" in classname:
        paragraph_called2.append(tag)
    if "span/" in classname:
        paragraph_called3.append(tag)
    if "footer/" in classname:
        paragraph_called4.append(tag)
    html_rules.append(tag)

def h1(text, classname):
    tag = "\n    <h1 class='" + classname + "'>" + text + '''</h1>'''
    if "header/" in classname:
        h1_called.append(tag)
    if "div/" in classname:
        h1_called2.append(tag)
    if "span/" in classname:
        h1_called3.append(tag)
    if "footer/" in classname:
        h1_called4.append(tag)
    html_rules.append(tag)

def h2(text, classname):
    tag = "\n    <h2 class='" + classname + "'>" + text + '''</h2>'''
    if "header/" in classname:
        h2_called.append(tag)
    if "div/" in classname:
        h2_called2.append(tag)
    if "span/" in classname:
        h2_called3.append(tag)
    if "footer/" in classname:
        h1_called4.append(tag)
    html_rules.append(tag)

def h3(text, classname):
    tag = "\n    <h3 class='" + classname + "'>" + text + '''</h3>'''
    if "header/" in classname:
        h3_called.append(tag)
    if "div/" in classname:
        h3_called2.append(tag)
    if "span/" in classname:
        h3_called3.append(tag)
    if "footer/" in classname:
        h3_called4.append(tag)
    html_rules.append(tag)

def h4(text, classname):
    tag = "\n    <h4 class='" + classname + "'>" + text + '''</h4>'''
    if "header/" in classname:
        h4_called.append(tag)
    if "div/" in classname:
        h4_called2.append(tag)
    if "span/" in classname:
        h4_called3.append(tag)
    if "footer/" in classname:
        h4_called4.append(tag)
    html_rules.append(tag)

def h5(text, classname):
    tag = "\n    <h5 class='" + classname + "'>" + text + '''</h5>'''
    if "header/" in classname:
        h5_called.append(tag)
    if "div/" in classname:
        h5_called2.append(tag)
    if "span/" in classname:
        h5_called3.append(tag)
    if "footer/" in classname:
        h5_called4.append(tag)
    html_rules.append(tag)

def h6(text, classname):
    tag = "\n    <h6 class='" + classname + "'>" + text + '''</h6>'''
    if "header/" in classname:
        h6_called.append(tag)
    if "div/" in classname:
        h6_called2.append(tag)
    if "span/" in classname:
        h6_called3.append(tag)
    if "footer/" in classname:
        h6_called4.append(tag)
    html_rules.append(tag)

def add_script(file_path):
    tag = "\n    <script src='" + file_path + "'>" + '''\n    </script>'''
    html_rules.append(tag)

def input(type, placeholder, classname):
    tag = "\n    <input type='" + type + "' placeholder='" + placeholder + "' class='" + classname + "'>"
    if "header/" in classname:
        input_called.append(classname)
    if "div/" in classname:
        input_called2.append(tag)
    if "span/" in classname:
        input_called3.append(tag)
    if "footer/" in classname:
        input_called4.append(tag)
    html_rules.append(tag)

def br():
    tag = '''\n    <br>'''
    html_rules.append(tag)

def hr():
    tag = '''\n    <hr>'''
    html_rules.append(tag)

def alert(alert):
    script = "        alert('"+alert+"');"
    tag = "\n    <script type='text/javascript'>\n"+script+"\n    </script>"
    html_rules.append(tag)

def on_scroll(rule, classname):
    rule = "            const element = document.getElementsByClassName('"+classname+"')"+';\n            element.' + rule + ';'
    script = '''        window.addEventListener('scroll', function() {\n'''+rule+'''\n        });'''
    tag = "\n    <script type='text/javascript'>\n"+script+"\n    </script>"
    html_rules.append(tag)

def list(list_elements_list, list_style, classname, list_items_classname):
    global elements
    for list_element in list_elements_list:
        list_element = "\n        <li class='"+list_items_classname+"'>"+list_element+"</li>"
        elements = elements + list_element
    tag = "\n    <ul class='"+classname+"'>"+elements+"\n    </ul>"
    if "header/" in classname:
        list_called.append(tag)
    if "div/" in classname:
        list_called2.append(tag)
    if "span/" in classname:
        list_called3.append(tag)
    html_rules.append(tag)
    rule = '\nli'"{\n    list-style: "+list_style+";\n}"
    css_rules.append(rule)

def open_in_browser():
    html_file.truncate(0)
    css_file.truncate(0)
    global ruleofhtml, ruleofcss
    if len(html_rules) == 0:
        html = '''<!---\n\n\nWritten By Using pysites Library please do not edit!--->\n<!---Contact Info--->\n<!---Mail: guvenkerem2006@gmail.com GitHub: https://github.com/kerem700916\nHAVE A NICE DAY\n\n\n\n--->\n\n\n<!DOCTYPE html>
<html lang="'''+language+'''">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>\n'''+icon+'''
</head>
<body>
        
</body>
</html>\n<!---\n\nWritten By Using pysites Library please do not edit!\nHAVE A NICE DAY\n\n\n\n--->'''
    else:
        for rule in html_rules:
            ruleofhtml = ruleofhtml + rule
        html = '''<!---\n\nWritten By Using pysites Library please do not edit!--->\n<!---Contact Info--->\n<!---Mail: guvenkerem2006@gmail.com GitHub: https://github.com/kerem700916\nHAVE A NICE DAY\n\n\n\n--->\n\n\n<!DOCTYPE html>
<html lang="'''+language+'''">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>\n'''+icon+'''
</head>
<body>''' + ruleofhtml + '''\n</body>
</html>\n\n\n<!---Written By Using pysites Library please do not edit!--->\n<!---Contact Info--->\n<!---Mail: guvenkerem2006@gmail.com GitHub: https://github.com/kerem700916\nHAVE A NICE DAY\n\n\n\n--->'''
    if len(css_rules) == 0:
        pass
    else:
        for rule in css_rules:
            ruleofcss = ruleofcss + rule
        css = '''*{
    margin:0;
    padding:0;
}''' + ruleofcss

        css_file.write(css)
    html_file.write(html)
    return webbrowser.open(os.getcwd() + '/index.html')

def color(color, classname):
    rule = '\n.'+ classname +"{\n    color: "+color+";\n}"
    css_rules.append(rule)

def background_color(color, classname):
    if classname == 'body' or classname == 'html' or classname == '*':
        rule = '\n'+ classname +"{\n    background-color:"+color+";\n}"
        css_rules.append(rule)
    else:
        rule = '\n.'+ classname +"{\n    background-color:"+color+";\n}"
        css_rules.append(rule)

def background_image(image, classname):
    if classname == 'body' or classname == 'html' or classname == '*':
        rule = '\n'+ classname +"{\n    background-image:url(' "+image+"');\n    background-repeate: no-repeat;\n    background-size: cover;\n}"
        css_rules.append(rule)
    else:
        rule = '\n.'+ classname +"{\n    background-image:url(' "+image+"');\n}"
        css_rules.append(rule)

def position(top, left, classname):
    rule = '\n.'+classname+'{\n    position: absolute;\n    transform: translate(-50%, -50%);\n    top: '+top+';\n    left: '+left+';\n}'
    css_rules.append(rule)

def font_size(font_size, classname):
    rule = '\n.'+classname+'{\n    font-size: '+font_size+';\n}'
    css_rules.append(rule)

def font_family(font_family, classname):
    rule = '\n.'+classname+'{\n    font-family: '+font_family+';\n}'
    css_rules.append(rule)

def hover(rule, classname, transition = '1'):
    hovered_rule = '   ' + rule
    rule = '\n.'+classname+':hover{\n '+hovered_rule+';\n    transition: '+transition+'s;\n}'
    css_rules.append(rule)

def cursor(cursor_type, classname):
    rule = '\n.'+classname+'{\n    cursor: '+cursor_type+';\n}'
    css_rules.append(rule)

def width(width, classname):
    width = width
    rule = '\n.'+classname+'{\n    width: '+width+';\n}'
    css_rules.append(rule)

def height(height, classname):
    height = height
    rule = '\n.'+classname+'{\n    height: '+height+';\n}'
    css_rules.append(rule)

def min_width(width, classname):
    width = width
    rule = '\n.'+classname+'{\n    min-width: '+width+';\n}'
    css_rules.append(rule)

def min_height(height, classname):
    height = height
    rule = '\n.'+classname+'{\n    min-height: '+height+';\n}'
    css_rules.append(rule)

def max_width(width, classname):
    width = width
    rule = '\n.'+classname+'{\n    max-width: '+width+';\n}'
    css_rules.append(rule)

def max_height(height, classname):
    height = height
    rule = '\n.'+classname+'{\n    max-height: '+height+';\n}'
    css_rules.append(rule)

def outline(outline, classname):
    rule = '\n.'+classname+'{\n    outline: '+outline+';\n}'
    css_rules.append(rule)

def border(border, classname):
    rule = '\n.'+classname+'{\n    border: '+border+';\n}'
    css_rules.append(rule)

def margin(margin, classname):
    rule = '\n.'+classname+'{\n    margin: '+margin+';\n}'
    css_rules.append(rule)

def padding(padding, classname):
    padding = padding
    rule = '\n.'+classname+'{\n    padding: '+padding+';\n}'
    css_rules.append(rule)

def background(background, classname):
    rule = '\n.'+classname+'{\n    background: '+background+';\n}'
    css_rules.append(rule)

def display(display, classname):
    rule = '\n.'+classname+'{\n    display: '+display+';\n}'
    css_rules.append(rule)

def add_animation(animatinon_name, transition, classname):
    rule = '\n.'+classname+'{\n    animation: '+animatinon_name+';\n    transition: '+transition+';\n}'
    css_rules.append(rule)

def keyframes(animation_name, before, middle, after):
    rule = '\n@keyframes '+animation_name+'{\n0%{\n    '+before+';\n}\n50%{\n    '+middle+';\n}\n100%{\n    '+after+';\n}\n}'
    css_rules.append(rule)

def mouse_position():
    return pyautogui.position()

def header(classname):
    global header_elements, paragraph_called, h1_called, h2_called, h3_called, h4_called, h5_called, h6_called, input_called, list_called
    for called in paragraph_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in header_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in div_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in span_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in footer_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in h1_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in h2_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in h3_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in h4_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in h5_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in h6_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in input_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        header_elements = header_elements + new_called
    for called in list_called:
        html_rules.remove(called)
        header_elements = header_elements + called
    tag = "\n    <header class='"+classname+"'>"+header_elements+"\n    </header>"
    paragraph_called = []
    h1_called = []
    h2_called = []
    h3_called = []
    h4_called = []
    h5_called = []
    h6_called = []
    input_called = []
    list_called = []
    header_elements = ''
    html_rules.append(tag)
    if "header/" in classname:
        header_called.append(tag)
    if "div/" in classname:
        header_called2.append(tag)
    if "span/" in classname:
        header_called3.append(tag)
    if "footer/" in classname:
        header_called4.append(tag)

def div(classname):
    global div_elements, paragraph_called2, h1_called2, h2_called2, h3_called2, h4_called2, h5_called2, h6_called2, input_called2, list_called2
    for called in paragraph_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in header_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in div_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in span_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in footer_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in h1_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in h2_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in h3_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in h4_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in h5_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in h6_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in input_called2:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        div_elements = div_elements + new_called
    for called in list_called2:
        html_rules.remove(called)
        div_elements = div_elements + called
    tag = "\n    <div class='"+classname+"'>"+div_elements+"\n    </div>"
    paragraph_called2 = []
    h1_called2 = []
    h2_called2 = []
    h3_called2 = []
    h4_called2 = []
    h5_called2 = []
    h6_called2 = []
    input_called2 = []
    list_called2 = []
    div_elements = ''
    html_rules.append(tag)
    if "header/" in classname:
        div_called.append(tag)
    if "div/" in classname:
        div_called2.append(tag)
    if "span/" in classname:
        div_called3.append(tag)
    if "footer/" in classname:
        div_called4.append(tag)

def span(classname):
    global span_elements, paragraph_called3, h1_called3, h2_called3, h3_called3, h4_called3, h5_called3, h6_called3, input_called3, list_called3
    for called in paragraph_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in header_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in div_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in span_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in footer_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in h1_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in h2_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in h3_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in h4_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in h5_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in h6_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in input_called3:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        span_elements = span_elements + new_called
    for called in list_called3:
        html_rules.remove(called)
        span_elements = span_elements + called
    tag = "\n    <span class='"+classname+"'>"+span_elements+"\n    </span>"
    paragraph_called3 = []
    h1_called3 = []
    h2_called3 = []
    h3_called3 = []
    h4_called3 = []
    h5_called3 = []
    h6_called3 = []
    input_called3 = []
    list_called3 = []
    span_elements = ''
    html_rules.append(tag)
    if "header/" in classname:
        span_called.append(tag)
    if "div/" in classname:
        span_called2.append(tag)
    if "span/" in classname:
        span_called3.append(tag)
    if "footer/" in classname:
        span_called4.append(tag)

def footer(classname):
    global footer_elements, paragraph_called3, h1_called3, h2_called3, h3_called3, h4_called3, h5_called3, h6_called3, input_called3, list_called3
    for called in paragraph_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in header_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in div_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in span_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in footer_called:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in h1_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in h2_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in h3_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in h4_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in h5_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in h6_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in input_called4:
        html_rules.remove(called)
        new_called = ''
        number = 0
        for string in called:
            if string == '\n':
                string = ''
            new_called = new_called + string
            number += 1
        new_called = '\n    ' + new_called
        footer_elements = footer_elements + new_called
    for called in list_called4:
        html_rules.remove(called)
        footer_elements = footer_elements + called
    tag = "\n    <footer class='"+classname+"'>"+footer_elements+"\n    </footer>"
    paragraph_called3 = []
    h1_called3 = []
    h2_called3 = []
    h3_called3 = []
    h4_called3 = []
    h5_called3 = []
    h6_called3 = []
    input_called3 = []
    list_called3 = []
    footer_elements = ''
    html_rules.append(tag)
    if "header/" in classname:
        footer_called.append(tag)
    if "div/" in classname:
        footer_called2.append(tag)
    if "span/" in classname:
        footer_called3.append(tag)
    if "footer/" in classname:
        footer_called4.append(tag)

print('NOTE: You May Need To Refresh The Page Several Times')
