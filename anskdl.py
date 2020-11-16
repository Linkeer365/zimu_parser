# article -> raw lines
# [tic:11-12] ... [tic:13-12]

import os
import re

article_path=r"D:\zimu_parser\article.txt"
raw_path=r"D:\zimu_parser\raw.txt"

with open(article_path,"r",encoding="utf-8") as f:
    article_s=f.read()



def parse_time(s):
    time_patt="\[tic:(.*?)\]"
    finds=re.findall(time_patt,s)

    print("times: ",finds)
    return finds

def parse_dialogue(s):

    dialogue_patt="\](.*?)\[tic:"
    finds=re.findall(dialogue_patt,s,re.S)

    print("dialogues: ",finds)

    return finds

def merge(times,dialogues):
    raw_lines=[]
    start_idx=0
    while start_idx<=len(times)-2:
        start_time=times[start_idx]
        end_time=times[start_idx+1]
        dialogue=dialogues[start_idx].replace('\n','')
        raw_line=f"{start_time}\t{end_time}\t{dialogue}"

        print("raw line: ",raw_line)

        raw_lines.append(raw_line)

        start_idx+=1

    return raw_lines

def main():
    times=parse_time(article_s)
    dialogues=parse_dialogue(article_s)
    raw_lines=merge(times,dialogues)
    raw_lines_s="\n".join(raw_lines)
    with open(raw_path,"w",encoding="utf-8") as f:
        f.write(raw_lines_s)

    print("done.")

if __name__ == '__main__':
    main()


