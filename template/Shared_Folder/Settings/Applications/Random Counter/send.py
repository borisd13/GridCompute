'''This script is executed when submitting cases to server. It takes as input a file selected by the user and returns one or several cases to submit to the server.'''

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


def select_input_files(filepath):
    """Submit a case to the grid.
    
    This function returns, from a selected file, one or several cases to run.
    Each case can be made of several input files.
    
    Args:
        filepath (str): Path of the file selected.
        
    Returns:
        str list: A list (or tuple) of cases. Each case is a list (or tuple) of input files required to process a case.
    """

    # In this example, only one case is returned, and that case contains only one file (the file selected)

    case_1 = (filepath,)      # list of input files needed for case_1
    return (case_1,)          # list of cases to run



