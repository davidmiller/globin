#!/usr/bin/env python
import os
import sys
import argparse

if __name__ == '__main__':
    program = 'Globin'
    parser = argparse.ArgumentParser( prog = program )    
    parser.add_argument( 'program',
                         help = 'name of the program - also the command you will use from stdin')
    parser.add_argument( 'path',
                         help = """the path to the program you want to add to the global path""")
    args = parser.parse_args()    

    script = os.path.abspath( args.path )
    if not os.path.isfile( script ):
        print 'the path to the script you entered turns out not to be a file'
        sys.exit()
    home_bin_location = os.path.join( '/home' )
    global_link_location = os.path.join( '/usr/local/bin', args.program )
    os.symlink( script, global_link_location ) 
