import sys
import os


class Manager():
    def __init__(self):
        self.__registered_paths = list()

    def registered_paths(self):
        '''
        Return the list of registered paths

        '''

        return self.__registered_paths


    def register_path(self, path):
        '''
        Register the path specified

        Example usage:
            register_path(r'x:\temporary')

        '''
        # Make sure that path is a string
        if not isinstance(path, str):
            #print ("The path should be a string. Found: %s. Ignoring.."
            #       % type(path))
            return

        # Check the path specified is a valid folder
        if not os.path.isdir(path):
            #print ("The path: '%s' is not a valid folder. Ignoring.." %
            #       path)
            return

        # Check if the path has been already added to the list
        if path in self.__registered_paths:
            #print ("The path: '%s' already exists in the "
            #       "self.__registered_paths list. Ignoring.." % path)
            return

        self.__registered_paths.append(path)


    def register_paths(self, path_list):
        '''
        Register all the paths in the list specified

        Example usage:
            register_paths([r'x:\temporary', r'x:\my_scripts'])

        '''

        assert isinstance(path_list, list), ("The argument specified needs to be "
                                             "a list. Found: %s" % type(path_list))

        for current_path in path_list:
            self.register_path(current_path)


    def deregister_path(self, path):
        '''
        Deregister the path specified

        Example usage:
            deregister_path(r'x:\temporary')

        '''

        # Make sure that path is a string
        if not isinstance(path, str):
            #print ("The path should be a string. Found: %s. Ignoring.."
            #       % type(path))
            return

        # Check if the path is already in list
        if path not in self.__registered_paths:
            #print ("The path: '%s' is not in the list. Ignoring.." % path)
            return

        self.__registered_paths.remove(path)


    def deregister_paths(self, path_list):
        '''
        Register all the paths in the list specified

        Example usage:
            deregister_paths([r'x:\temporary', r'x:\my_scripts'])

        '''

        assert isinstance(path_list, list), ("The argument specified needs to be "
                                             "a list. Found: %s" % type(path_list))

        for current_path in path_list:
            self.deregister_path(current_path)


    def discover_modules(self):
        '''
        List all the modules found in the registered paths

        '''

        if not self.__registered_paths:
            return

        for path in self.__registered_paths:
            modules = [os.path.splitext(f)[0] for f in os.listdir(path) if
                       os.path.isfile(os.path.join(path,f)) and
                       f.endswith('.py')]

            # print modules
            modules = list(set(modules))
            return modules


    def add_folders_to_pythonpath(self, folders):
        '''
        Add the folders within the list specified to the the Python path

        '''

        assert isinstance(folders, list), ("The argument specified needs to be "
                                           "a list. Found: %s" % type(path_list))

        if not folders:
            return

        for path in folders:
            if not path in sys.path:
                sys.path.append(path)


    def load_modules(self, modules_to_load):
        '''
        Load the modules in the list specified and return a reference to them.

        '''

        assert (isinstance(modules_to_load, type(None)) or
                isinstance(modules_to_load, list)), ("The argument specified "
                                                     "needs to be a list. Found: "
                                                     "%s" % type(modules_to_load))


        modules_loaded = list()

        if not modules_to_load:
            # print "No modules discovered. Nothing to do.."
            return

        for module in modules_to_load:
            module_name = __import__(module)
            modules_loaded.append(module_name)

        return modules_loaded
