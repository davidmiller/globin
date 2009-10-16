#!/usr/bin/env python
"""57 command line utility for adding scripts to local & global $PATH"""
import os
import sys
import argparse

# Error classes to hanle possible overwriting conflicts
class Error( Exception ):
    """ Base class for exceptions """
    pass


class ExistsInPathError( Error ):
    """ Don't go creating the created now"""
    def __init__( self, value ):
        self.value = value
    def __str__( self ):
        return repr( self.value )


def link_if_empty( target, destination ):
    if not os.path.isfile( destination ):
        os.symlink( script, global_link_location )
    else:
        raise ExistsInPathError( global_link_location )

if __name__ == '__main__':
    # Argument parsing stuff
    program = 'globin'
    parser = argparse.ArgumentParser( prog = program )    
    parser.add_argument( 'program',
                         help = 'name of the program - also the command you will use from stdin')
    parser.add_argument( 'path',
                         help = "the path to the program you want to add to the global path" )
    args = parser.parse_args()    

    # Get the script location
    script = os.path.abspath( args.path )
    if not os.path.isfile( script ):
        print 'the path to the script you entered turns out not to be a file'
        sys.exit()
    
    # Link location definitions
    global_link_location = os.path.join( '/usr/local/bin', args.program )
    home_link_loc = os.path.join( home_bin_path, program )

    # Put the script into the global path
    if os.access( '/usr/local/bin', os.W_OK ):
        link_if_empty( script, global_link_location )
    else:
        print """ No write access to global path - file only added locally"""         

    # Put the script into the local path
    home_bin_path = os.path.join(  os.environ['HOME'], 'bin' )    
    if os.path.isdir( home_bin_path ):
        link_if_empty( script, home_link_loc )
    
    print "%s added to $PATH" % program
