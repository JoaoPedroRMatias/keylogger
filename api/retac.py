def parse_keyboard_events(file):
    text = ''
    with open(file, 'r', encoding='utf-8') as f:
        current_window = ''
        for line in f:
            line = line.strip()
            if line.startswith("[JANELA]"):
                current_window = line[len("[JANELA]"):].strip()
            else:
                events = line.split(' ')
                for event in events:
                    if event.startswith("'"):
                        text += event.strip("'")
                    elif event == "Key.space":
                        text += ' '
                    elif event == "Key.backspace":
                        text = text[:-1]
                    elif event == "['�']":
                        text += '�'
                    elif event == "Key.enter":
                        text += ''
                if current_window:
                    text += f"\n[JANELA] {current_window}\n"

    return text

file = 'keylogger.log'
formatted_text = parse_keyboard_events(file)

print(formatted_text)
