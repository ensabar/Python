#class ManagedFile:
#    def __init__(self, filename):
#        print('init')
#        self.filename = filename
#
#    def __enter__(self):
#        print('enter')
#        self.file = open(self.filename, 'w')
#        return self.file
#    
#    def __exit__(self, exc_type, exc_value, exc_traceback):
#        if self.file:
#            self.file.close()
#        if exc_type is not None:
#            print('exception has been handled')
#        #print('exc: ', exc_type, exc_value)
#        print('exit')
#        return True
#
#
#with ManagedFile('notes.txt') as file:
#    print('do some stufff...')
#    file.write('some to do...')
#    file.somemethod()

######################################################

from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('writing something to do....')