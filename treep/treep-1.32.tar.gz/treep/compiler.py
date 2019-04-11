# Treep, copyright 2019 Max Planck Gesellschaft
# Author : Vincent Berenz 

# This file is part of Treep.

#    Treep is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Treep is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Treep.  If not, see <https://www.gnu.org/licenses/>.


import os,copy,sys

from .catkin_make import get_catkin_make_command
from .cmake import get_cmake_command
from .pip import get_pip_command


class Compiler:

    CMAKE = 1
    PIP = 2
    CATKIN_MAKE = 3

    COMPILATION_TYPES = [CMAKE,PIP,CATKIN_MAKE]
    
    YAML_TAGS = { "catkin":CATKIN_MAKE,
                  "cmake":CMAKE,
                  "pip":PIP }
    
    FUNCTIONS = { CATKIN_MAKE: get_catkin_make_command,
                  CMAKE: get_cmake_command,
                  PIP: get_pip_command }

    def __init__(self):

        self.configurations = {}

    # some compilation scripts are natively supported
    # (catkin,cmake,pip)
    # but users have the option to create new ones,
    # expected to be in the treep_xxx/compilation.py
    # file. Importing them here
    def add_compilation_script(self,path):

        def import_for_python_2(path):
            imported = {}
            execfile(path,globals(),imported)
            return imported

        def import_for_python_3(path):
            imported = {}
            exec(compile(open(path).read(), path, 'exec'),globals(),imported)
            return imported

        # import content of customized compilation.py
        if sys.version_info[0] < 3:
            imported = import_for_python_2(path)
        else:
            imported = import_for_python_3(path)

            
        # new non private variables
        new_functions = {k:v for k,v in imported.items()
                         if not k.startswith("_")}

        # new callables
        new_functions = {k:v for k,v in new_functions.items()
                         if hasattr(v,'__call__')}
        
        # adding each function to Compiler
        for name,function in new_functions.items():

            # creating a new compilation type
            index = min(self.__class__.COMPILATION_TYPES)-1
            setattr(self.__class__,name,index)
            self.__class__.COMPILATION_TYPES.append(index)
            
            # adding a new yaml tag
            self.__class__.YAML_TAGS[name]=index

            # adding a new function
            self.__class__.FUNCTIONS[index]=function

            # adding a configuration
            self.configurations[name]=(index,{})
            

    # category: catkin_make, cmake or pip
    def add(self,label,category,kwargs):

        self.configurations[label]=[category,kwargs]
        
        
    def get_script(self,
                   workspace_path,
                   package_name,
                   package_path,
                   label):

        category,kwargs = self.configurations[label]
        function = self.FUNCTIONS[category]

        return function(workspace_path,
                        package_name,
                        package_path,
                        **kwargs)

        
    
