# -*- coding: utf-8 -*-
import sys
import importlib.machinery
import importlib.util

def load_source(name, pathname, file=None):
    loader = importlib.machinery.SourceFileLoader(name, pathname)
    # spec = importlib.util.spec_from_file_location(name, pathname, loader=loader)
    spec = importlib.util.spec_from_loader(name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    sys.modules[name] = module
    return module
