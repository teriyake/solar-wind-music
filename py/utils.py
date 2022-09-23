import re

dataPath = "C:/Users/butte/pd/data/";
dirtyData = "sw090522.json";
# reSearch = r'^(\]\,)$';
output = "sw090522.csv";

fileOut = open(dataPath + output, 'w');
with open(dataPath + dirtyData, 'r') as f:
    content = f.readlines();
    for line in content:
        lineNew = line.replace('],', '\n').replace('[', '').replace(']', '').replace('"', '');
        fileOut.write(lineNew);
       # lineNew = re.sub('\]\,', '\n', content, flags=re.M);

# for line in content:
 #    print(line);
