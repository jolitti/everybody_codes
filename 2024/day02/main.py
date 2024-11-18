import regex as re

sample_data = [
        "THE,OWE,MES,ROD,HER",
        "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"
        ]
sample_data2 = [
        "THE,OWE,MES,ROD,HER,QAQ",
        [
            "AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE",
            "THE FLAME SHIELDED THE HEART OF THE KINGS",
            "POWE PO WER P OWE R",
            "THERE IS THE END",
            "QAQAQ"
        ]
    ]


with open("input1.txt") as file:
    data1 = file.readlines()
data1 = [s.strip() for s in data1]
data1 = [data1[0].removeprefix("WORDS:"),data1[2]]    

with open("input2.txt") as file:
    data2 = file.readlines()
data = [s.strip() for s in data2]
data2 = [data2[0].removeprefix("WORDS:"),data2[2:]]    
data2[1] = [d.strip() for d in data2[1]]

def part1(data):
    words, text = data
    words = list(words.split(","))
    tot = 0
    for word in words:
        tot += text.count(word)
    return tot

def part2(data):
    words,texts = data
    words = list(words.split(","))
    tot = 0
    for text in texts:
        match_indices = set()
        for word in words:
            pattern = word + "|" + word[::-1]
            matches = re.finditer(pattern,text,overlapped=True)
            for m in matches:
                for i in range(*m.span()):
                    match_indices.add(i)
        tot += len(match_indices)
    return tot

assert part1(sample_data)==4
print(part1(data1))

assert part2(sample_data2) == 15 + 9 + 6 + 7 + 5
print(part2(data2))
