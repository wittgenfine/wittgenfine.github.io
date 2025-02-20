#!/usr/bin/env python3
import os

first_part = '''
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Blog</title>
  <link rel="stylesheet" href="../../style.css">
</head>

<body>
  <!-- Navigation Bar -->

  <ol id="myNavList">
    <li><a class="arrow" href="../../index.html"><i class="fas fa-arrow-alt-right"></i>HOME</a></li>
    <li><a class="arrow" href="../blog.html"><i class="fas fa-arrow-alt-right"></i>WRITINGS</a></li>
    <li><a class="arrow" href="../library.html"><i class="fas fa-arrow-alt-right"></i>LIBRARY OF BABEL</a></li>
    <li><a class="arrow" href="../about.html"><i class="fas fa-arrow-alt-right"></i>ABOUT</a></li>
    <li><a class="arrow" href="../gf.html"><i class="fas fa-arrow-alt-right"></i>GF APPLICATION</a></li>
  </ol>

  
  <!-- Blog Post Section -->
  <section id="blog" class="blog-posts">
    <!-- Blog Post 1 -->
    <div class="post">
      <h2 class="post-title">About a girl</h2>
       <h2 class="sub-title">Object Petite a (Yes I realize it's misspelled)</h2>
      <p class="post-author"><strong>Wittgenfine</strong></p>
      <p class="post-date">Mar 16 2022</p>
      <img src="../../graph-of-desire.jpg" alt="Graph of desire">
      <div class="post-content">

'''

last_part = '''
 </div>
    </div>

  </section>

  <footer>
    <h2>Thank you for reading. Follow me on twitter: <a href="https://x.com/wittgenfine">wittgenfine</a></h2>
  </footer>
</body>

</html>
'''


def get_file_name():
    file_path = input("Enter file name/path: ")
    while not os.path.exists(file_path):
        print("ERROR THAT PATH DOES NOT EXIST")
        file_path = input("Please Enter a valid file name/path: ")
    return file_path;

def parse_file(file_name=None):
    text = "<p>&emsp; "
    if file_name == None:
        file_name = get_file_name()
    with open(file_name, 'r') as file:
        for i in file:
            i = i[:-1]
            text+=i
            text+= '</p>\n'
            text+= "<p>&emsp; "
        text += '</p>'
    return text

def make_html(text, ask_for_filename=True, file_path=""):
    if ask_for_filename == True:
        file_path = input("Enter file name/path (include .html): ")
    answer = 'n'
    while (answer == 'n' and os.path.exists(file_path) or file_path[len(file_path)-4:] != 'html'):
        print("WARNING!!: That file already or you did not end it with HTML")
        answer = input("Overwite/Proceed (y/n)")
        if answer == 'n':
            file_path = input("Enter file name/path (include .html): ")
        else:
            break


    with open(file_path, 'w') as file:
        file.write(first_part)
        file.write(text)
        file.write(last_part)

def batch_make():
    directory = "Text"
    extension = ".txt"  # Change to your desired extension
    files = [directory + "/" + f for f in os.listdir(directory) if f.endswith(extension)]
    for file in files:
        html_name = file[:-3] + "html"
        text = parse_file(file)
        make_html(text, False, html_name)

def main():
    answer = input("Press 1 for batch upload (all txt files in Text folder) or 2 for individual file: ")
    while (answer != '1' and answer != '2'):
        print("ERROR! INVALID SELECTION PLEASE TRY AGAIN")
        answer = input("Press 1 for batch upload (all txt files in Text folder) or 2 for individual file: ")

    if answer == 1:
        text = parse_file()
        make_html(text)
    else:
        batch_make()
            




if __name__ == '__main__':
    main()
