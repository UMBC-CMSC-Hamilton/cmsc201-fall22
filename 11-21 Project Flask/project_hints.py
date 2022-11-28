dir_name = '/hello'
file_name = 'hello.txt'

root_directory = {dir_name: {}, file_name: "the file contents"}

for dir_or_file in root_directory:
    print(dir_or_file)
    if dir_or_file[0] == '/':
        print('this is a directory')
    else:
        print('this is a file')
        
'/hello/first-layer/second-layer'
"""
    Scan through the directory levels using a loop of some kind
        or recursively (probably not)
    find the last directory.
"""

"cd .."


root_dir = {
    'sub-dir':
        {
            '..': None,
            'other_file': ""
        },
    'my_file.txt': ""
}

root_dir['sub-dir'][".."] = root_dir
print(root_dir)

print(root_dir)
current = root_dir['sub-dir']
print(current)
"""
    now we run a cd .. command
"""
current = current['..']
print(current)
