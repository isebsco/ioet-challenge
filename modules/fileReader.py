def readtxt(file):
    '''
    This method will open a txt file, it must received a string as the name of
    the file without the extension.
  
    '''
    lines = open(f'files/{file}.txt', 'r').read().splitlines()
    return lines
    
