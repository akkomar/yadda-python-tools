import shutil
import os

collection_ids = ['pldml', 'cejsh', 'agro', 'baztech', 'bazhum', 'bazekon']

OUT_DIR = 'out'
if os.path.exists(OUT_DIR):
    shutil.rmtree(OUT_DIR)

os.mkdir(OUT_DIR)

for collection in collection_ids:
    COLLECTION_DIR = OUT_DIR + '/' + collection
    os.mkdir(COLLECTION_DIR)

    with open(COLLECTION_DIR + '/' + 'robots.txt', 'w') as output:
        with open('template_robots.txt', 'r') as template:
            for line in template:
                output.write(line.replace('@repo_id@', collection))

#composite
COMPOSITE_DIR = OUT_DIR + '/' + 'composite'
os.mkdir(COMPOSITE_DIR)
with open(COMPOSITE_DIR + '/' + 'robots.txt', 'w') as output:
    collection_ids.append('yadda')
    for collection in collection_ids:
        with open('template_robots.txt', 'r') as template:
            for line in template:
                output.write(line.replace('@repo_id@', collection))


