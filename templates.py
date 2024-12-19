import os

def create_init(path):
    dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path,dir))]
    for dir in dirs:
        if ".git" == dir:
            pass
        else:
            init_file = os.path.join(path, dir, '__init__.py')
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    f.write('')
            create_init(os.path.join(path,dir))

create_init(os.getcwd())