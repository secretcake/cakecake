# This file contains various definitions for use in scripts

#@TODO define all characters here
define mc = Character("MC")

# @TODO image definitions here

# @TODO audio definitions here
# note: we want to use Ren'py's audio namespace for audio because it makes things readable

label start:
    # Please don't change this!
    call pre_start
    call real_start
    return
