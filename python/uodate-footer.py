##################################################################################
# Program: update-footer.py
# Author: Antonius Torode
# Created: 3/11/2019 then modified 1/9/2021
# Purpose: To update the footer in multiple html documents based on a template.
##################################################################################

# These are the files that the footer will be added to. They must all be html files.
filenames = ['index',
             'articles/introduction'
             'articles/helloWorld',
             'articles/localGitSetup',
             'articles/construction',
             'articles/createFromTemplate']

# This is the template file containing the footer html.
templateFileName = 'footer.html'

# Print the template file being used.
print('...')
print('...Template File as {0}'.format(templateFileName))
print('...')

# Store the text from the template file.
with open('{0}'.format(templateFileName), 'r') as templateFile:
    templateText = templateFile.read()

# Print the text from the template file.
print('...')
print('...Printing Template Text.')
print('...')
print(templateText)
print('...')

# Update the footer in the html files.
for filename in filenames:
    # Prints the current html file being processed.
    # Then opens it, gathers the lines from it, closes it, and opens it for writing.
    print('...')
    print('...Processing file: {0}.html'.format(filename))
    print('...')
    file = open('../{0}.html'.format(filename), 'r')
    fileLines = file.readlines()
    file.close()
    file = open('../{0}.html'.format(filename), 'w')

    p1 = True
    p2 = p3 = p4 = False

    # This will go through each line of the file.
    # p1 represents the section before the start footer marker.
    # p2 represents the section where the footer template is placed.
    # p3 represents the text after the footer until the end footer marker.
    # p4 represents the rest of the file.
    # CAUTION: The order of these if statements is important!
    for fileline in fileLines:
        if p1:
            file.write(fileline)
        if p3:
            if '<!-- ============== END FOOTER - PYTHON ENCODED =============== -->' in fileline:
                p3 = False
                p4 = True
        if p2:
            file.write(templateText)
            p2 = False
            p3 = True
        if p4:
            file.write(fileline)
        if '<!-- ============== BEGIN FOOTER - PYTHON ENCODED =============== -->' in fileline:
            p1 = False
            p2 = True

print('...')
print('...Program Finished.')
