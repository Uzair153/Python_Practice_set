content=True
i=1
with open('39_log.txt') as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"yes python is present in line {i}")
        i += 1
