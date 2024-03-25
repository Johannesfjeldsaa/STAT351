
filepath = "C:\\Users\\fjejo\\OneDrive\\Skrivebord\\sykkeloverhaling.txt"
with open(filepath) as f:
    new_file = ''
    for line in f:
        if line[0] == '[':
            line = '- ' + line
        else:
            if line.strip() != "":
                line = '**' + line
        new_file = new_file + line

    print(new_file)