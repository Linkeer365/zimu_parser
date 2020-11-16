# raw lines -> final ass
# start_timezone \t end_timezone \t text
# time format: hour-minute-second

import sys

boilerplate_path=r"D:\zimu_parser\boilerplate.ass"
raw_path=r"D:\zimu_parser\raw.txt"

final_ass_path=r"D:\zimu_parser\final.ass"


with open(boilerplate_path,"r",encoding="utf-8") as f:
    boilerplate_s=f.read()

with open(raw_path,"r",encoding="utf-8") as f:
    # no \n here
    raw_lines=[each.strip("\n") for each in f.readlines() if each!='\n']


def parse_timezone(timezone_str):
    packs=timezone_str.split("-")
    assert len(packs)<4
    print(packs)
    if len(packs)==3:
        hour,minute,second=packs
    elif len(packs)==2:
        hour='0'
        minute,second=packs
    elif len(packs)==1:
        hour='0'
        minute='0'
        second=packs[0]
    pack_s=f"{hour.zfill(1)}:{minute.zfill(2)}:{second.zfill(2)}"

    print("Timezone: ",pack_s)

    return pack_s

# parse_timezone("11-2")


def parse_line(raw_line:str):
    # print(repr(raw_line))
    time_zones,text=raw_line.rsplit("\t",maxsplit=1)
    start_timezone,end_timezone=time_zones.split("\t")
    start_s=parse_timezone(start_timezone)
    end_s=parse_timezone(end_timezone)
    dialogue_s=f"Dialogue: 0,{start_s},{end_s},Default,,0,0,0,,{text}"

    print("Text: ",text)

    # print("Dialogue: ",dialogue_s)

    return dialogue_s

def merge(dialogues):
    dialogues_s="\n".join(dialogues)
    final_s=f"{boilerplate_s}\n{dialogues_s}"
    print("final:\n",final_s)

    return final_s

# dialogues=[ "Dialogue: 0,0:00:02.00,0:00:05.00,Default,,0,0,0,,好，那我现在就开始",
#             "Dialogue: 0,0:00:05.00,0:00:07.00,Default,,0,0,0,,很多小伙伴去超星（网站）"]
#
# merge(dialogues)

def main():
    dialogues=[]
    for raw_line in raw_lines:
        dialogue=parse_line(raw_line)
        dialogues.append(dialogue)
    final_s=merge(dialogues)
    with open(final_ass_path,"a",encoding="utf-8") as f:
        f.write(final_s)

if __name__ == '__main__':
    main()




# parse_line("3,5,ccd")



