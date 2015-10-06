# Module Manager

[![Documentation Status](https://readthedocs.org/projects/module-mgr/badge/?version=latest)](http://module-mgr.readthedocs.org/en/latest/?badge=latest)

Simple Python Module Manager

Usage example:

```python
import module_mgr as mm

mm.register_paths([r'x:\temporary', r'j:\\custom_scripts'])
registered_paths = mm.registered_paths()
mm.add_folders_to_pythonpath(registered_paths)

modules_discovered = mm.discover_modules()
modules_loaded = mm.load_modules(modules_discovered)

if modules_loaded:
    for current_module in modules_loaded:
        print "FILE NAME:", current_module.__file__
        # Assuming a common interface to the module, we can use something like:
        try:
            current_module.main()
        except Exception, e:
            print "EXCEPTION:", e
```
