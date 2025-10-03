import re

# Instructions:
# Using Python, execute this script in your game folder under your project, or where-ever you keep your story scripts.
# This will only process one script at a time.  Change the script path to target the script you want to process.  
# Change the output path to be the name of the script you want the results to be dumped out to. 
# This script will *NOT* edit the original script, only create a new one with the updates.  
# After reviewing the output, you can make a backup copy of your script, delete it, then rename the output file to match the original to implement it in.



SCRIPT_PATH = "script.rpy"
OUTPUT_PATH = "script_with_ids.rpy"

label_re = re.compile(r'^\s*label\s+(\w+)\s*:')
say_line_re = re.compile(
    r'^\s*(?P<speaker>"[^"]*"|[a-zA-Z_]\w*)'         
    r'(?:\s+\w+)*'                                   
    r'\s+(?P<quote>["\'])(?P<dialogue>.+?)(?P=quote)'
    r'\s*(?!id\s)'                                   
)

def sanitize_speaker(raw):
    raw = raw.strip()
    if raw.startswith('"'):
        return "Narrator"
    return raw

def process_script():
    with open(SCRIPT_PATH, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()     

    current_label = None
    speaker_counts = {}
    new_lines = []

    for line in lines:
        label_match = label_re.match(line)
        if label_match:
            current_label = label_match.group(1)
            speaker_counts = {}
            print(f"[DEBUG] New label detected: {current_label}")
            new_lines.append(line)
            continue

        print(f"[DEBUG] Line: {line.strip()} -> Label: {current_label}")

        say_match = say_line_re.match(line)
        if say_match:
            speaker_raw = say_match.group("speaker")
            speaker = sanitize_speaker(speaker_raw)
            label_for_id = current_label or "global"

            speaker_counts[speaker] = speaker_counts.get(speaker, 0) + 1
            count = speaker_counts[speaker]
            tlid = f'{label_for_id}_{speaker}_{count:04d}'
            new_line = line.rstrip() + f' id {tlid}\n'
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print("Done.")

if __name__ == "__main__":
    process_script()
