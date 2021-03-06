'''This module is the start-up script used to launch *GridCompute*.
 
It first ensures that there is only one instance running, then creates the interface and initializes all parameters required to run the program. To finish, it runs the main loop associated to interface.'''

# Copyright 2014 Boris Dayma
# 
# This file is part of GridCompute.
# 
# GridCompute is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# 
# GridCompute is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GridCompute.  If not, see <http://www.gnu.org/licenses/>.
#
# For any question, please contact Boris Dayma at boris.dayma@gmail.com


import multiprocessing
import g_config as config
import g_interface as interface
import g_server_management as server_management
import threading
import os
import psutil
import datetime

def start(gui, current_pid):
    '''Start the program.

    Ensures there is only one instance, initialize all server related parameters and populate interface.
    
    Args:
        gui (GUI): GUI instance handling program interface.
        current_pid (int): pid of main thread.'''

    ensure_single_instance(current_pid, gui.event_queue)
    server = server_management.Server(gui.event_queue, gui.dedicated_process)
    gui.link_server(server)
    gui.event_queue.put({'type':'populate'})  # populate GUI when all actions are processed

def ensure_single_instance(current_pid, event_queue):
    '''Ensure that only one instance of the program is running.
    
    Check current pid against a configuration file that will contain pid of other running instance if any.
    
    Args:
        current_pid (int): pid of current process.
        event_queue (Queue): queue of events to process by gui.'''

    if config.pid_file.is_file():
        with config.pid_file.open() as f:
            try:  # will work if content of file is an int
                previous_pid = int(f.read().strip())
            except:
                event_queue.put({'type':'log_file_only', 'message':'PID could not be read from pid file {}'.format(config.pid_file)})
                previous_pid = -1
            if psutil.pid_exists(previous_pid):
                event_queue.put({'type':'critical', 'message':'Program already running'})
                raise SystemExit('Program already running')

    # write current pid in file
    with config.pid_file.open(mode='w') as f:
        f.write(str(current_pid))

if __name__ == "__main__":

    multiprocessing.freeze_support()  # allow freeze of program

    interface.init_log()   # Initialize logging in file
    gui = interface.GUI()  # Create gui with init screen
    threading.Thread(target=start, daemon=True, args=(gui, os.getpid())).start()
    gui.root.mainloop()    # Capture events


