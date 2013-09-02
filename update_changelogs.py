import codecs
import string
from xml.dom.minidom import parse
import os


#os.chdir('/path/to/project')

def get_version_from_pom(directory):
    pom_file = os.path.join(directory, 'pom.xml')
    dom = parse(pom_file)
    project = dom.getElementsByTagName('project')[0]
    for node in project.childNodes:
        if node.nodeType == node.ELEMENT_NODE and node.tagName == 'version':
            full_version_string = node.firstChild.nodeValue
            return string.replace(full_version_string, '-SNAPSHOT', '')

    for node in project.childNodes:
        if node.nodeType == node.ELEMENT_NODE and node.tagName == 'parent':
            for parent_node in node.childNodes:
                if parent_node.nodeType == parent_node.ELEMENT_NODE and parent_node.tagName == 'version':
                    full_version_string = parent_node.firstChild.nodeValue
                    return string.replace(full_version_string, '-SNAPSHOT', '')


def add_entry_to_changelog_in(project_dir, version):
    file_name = os.path.join(project_dir, 'changelog.txt')

    f = codecs.open(file_name, 'r', 'utf-8')
    old_changelog_content = f.read()
    f.close()

    line_to_add = '==VERSION: ' + version + '=='

    if old_changelog_content.startswith(line_to_add):
        print('Changelog seems to be up-to-date')
    else:
        f = codecs.open(file_name, 'w', 'utf-8')
        f.write(line_to_add + "\n")
        f.write(old_changelog_content)
        f.close()

for project_dir in os.listdir(os.getcwd()):
    if os.path.isdir(project_dir):
        directory_contents = os.listdir(project_dir)
        if 'pom.xml' in directory_contents and 'changelog.txt' in directory_contents:
            print()
            print('Project:', project_dir)
            project_version = get_version_from_pom(project_dir)
            add_entry_to_changelog_in(project_dir, project_version)
