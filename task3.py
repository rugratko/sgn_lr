mas = ['alabama', 'alaska', 'texas', 'california', 'nevada', 'michigan']
txt = open('words.txt', 'w')

for i in mas:
    txt.write(i + '\n')
    
txt.close()

txt = open('words.txt', 'r')
mass = []
text = txt.readlines()
text = [line.rstrip() for line in text]
for i in text:
    print(id, end = ' ')
