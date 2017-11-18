# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_socketstream')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_socketstream')
    _socketstream = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_socketstream', [dirname(__file__)])
        except ImportError:
            import _socketstream
            return _socketstream
        try:
            _mod = imp.load_module('_socketstream', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _socketstream = swig_import_helper()
    del swig_import_helper
else:
    import _socketstream
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


import mesh
import matrix
import vector
import array
import ostream_typemap
import operators
import ncmesh
import gridfunc
import coefficient
import intrules
import sparsemat
import densemat
import eltrans
import fe
import fespace
import fe_coll
import lininteg
import bilininteg
import linearform
import element
import geom
import table
import vertex
class socketbuf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, socketbuf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, socketbuf, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _socketstream.new_socketbuf(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def attach(self, sd):
        return _socketstream.socketbuf_attach(self, sd)

    def detach(self):
        return _socketstream.socketbuf_detach(self)

    def open(self, hostname, port):
        return _socketstream.socketbuf_open(self, hostname, port)

    def close(self):
        return _socketstream.socketbuf_close(self)

    def getsocketdescriptor(self):
        return _socketstream.socketbuf_getsocketdescriptor(self)

    def is_open(self):
        return _socketstream.socketbuf_is_open(self)
    __swig_destroy__ = _socketstream.delete_socketbuf
    __del__ = lambda self: None
socketbuf_swigregister = _socketstream.socketbuf_swigregister
socketbuf_swigregister(socketbuf)

class socketstream(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, socketstream, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, socketstream, name)
    __repr__ = _swig_repr
    secure_default = _socketstream.socketstream_secure_default

    def __init__(self, *args):
        this = _socketstream.new_socketstream(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def rdbuf(self):
        return _socketstream.socketstream_rdbuf(self)

    def open(self, hostname, port):
        return _socketstream.socketstream_open(self, hostname, port)

    def close(self):
        return _socketstream.socketstream_close(self)

    def is_open(self):
        return _socketstream.socketstream_is_open(self)
    __swig_destroy__ = _socketstream.delete_socketstream
    __del__ = lambda self: None

    def precision(self, *args):
        return _socketstream.socketstream_precision(self, *args)

    def send_solution(self, mesh, gf):
        return _socketstream.socketstream_send_solution(self, mesh, gf)

    def send_text(self, ostr):
        return _socketstream.socketstream_send_text(self, ostr)

    def flush(self):
        return _socketstream.socketstream_flush(self)

    def __lshift__(self, *args):
        return _socketstream.socketstream___lshift__(self, *args)

    def endline(self):
        return _socketstream.socketstream_endline(self)
socketstream_swigregister = _socketstream.socketstream_swigregister
socketstream_swigregister(socketstream)

class socketserver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, socketserver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, socketserver, name)
    __repr__ = _swig_repr

    def __init__(self, port, backlog=4):
        this = _socketstream.new_socketserver(port, backlog)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def good(self):
        return _socketstream.socketserver_good(self)

    def close(self):
        return _socketstream.socketserver_close(self)

    def accept(self, *args):
        return _socketstream.socketserver_accept(self, *args)
    __swig_destroy__ = _socketstream.delete_socketserver
    __del__ = lambda self: None
socketserver_swigregister = _socketstream.socketserver_swigregister
socketserver_swigregister(socketserver)

# This file is compatible with both classic and new-style classes.


