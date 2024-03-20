r"""Wrapper for omapi.h

Generated with:
C:\Users\mikec\AppData\Local\Programs\Python\Python311\Scripts\ctypesgen -a -lomapi -o pylibomapi_win_wrapper.py omapi.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "lib%s64.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["omapi"] = load_library("omapi")

# 1 libraries
# End libraries

# No modules

# C:/msys64/ucrt64/include/_mingw.h: 641
for _lib in _libs.values():
    if not _lib.has("__mingw_get_crt_info", "cdecl"):
        continue
    __mingw_get_crt_info = _lib.get("__mingw_get_crt_info", "cdecl")
    __mingw_get_crt_info.argtypes = []
    __mingw_get_crt_info.restype = c_char_p
    break

ssize_t = c_int64# C:/msys64/ucrt64/include/corecrt.h: 45

rsize_t = c_size_t# C:/msys64/ucrt64/include/corecrt.h: 52

intptr_t = c_int64# C:/msys64/ucrt64/include/corecrt.h: 62

ptrdiff_t = c_int64# C:/msys64/ucrt64/include/corecrt.h: 88

wchar_t = c_ushort# C:/msys64/ucrt64/include/corecrt.h: 98

wint_t = c_ushort# C:/msys64/ucrt64/include/corecrt.h: 106

wctype_t = c_ushort# C:/msys64/ucrt64/include/corecrt.h: 107

errno_t = c_int# C:/msys64/ucrt64/include/corecrt.h: 113

__time32_t = c_long# C:/msys64/ucrt64/include/corecrt.h: 118

__time64_t = c_int64# C:/msys64/ucrt64/include/corecrt.h: 123

time_t = __time64_t# C:/msys64/ucrt64/include/corecrt.h: 138

# C:/msys64/ucrt64/include/corecrt.h: 452
class struct_threadlocaleinfostruct(Structure):
    pass

# C:/msys64/ucrt64/include/corecrt.h: 431
class struct_threadmbcinfostruct(Structure):
    pass

pthreadlocinfo = POINTER(struct_threadlocaleinfostruct)# C:/msys64/ucrt64/include/corecrt.h: 432

pthreadmbcinfo = POINTER(struct_threadmbcinfostruct)# C:/msys64/ucrt64/include/corecrt.h: 433

# C:/msys64/ucrt64/include/corecrt.h: 434
class struct___lc_time_data(Structure):
    pass

# C:/msys64/ucrt64/include/corecrt.h: 439
class struct_localeinfo_struct(Structure):
    pass

struct_localeinfo_struct.__slots__ = [
    'locinfo',
    'mbcinfo',
]
struct_localeinfo_struct._fields_ = [
    ('locinfo', pthreadlocinfo),
    ('mbcinfo', pthreadmbcinfo),
]

_locale_tstruct = struct_localeinfo_struct# C:/msys64/ucrt64/include/corecrt.h: 439

_locale_t = POINTER(struct_localeinfo_struct)# C:/msys64/ucrt64/include/corecrt.h: 439

# C:/msys64/ucrt64/include/corecrt.h: 447
class struct_tagLC_ID(Structure):
    pass

struct_tagLC_ID.__slots__ = [
    'wLanguage',
    'wCountry',
    'wCodePage',
]
struct_tagLC_ID._fields_ = [
    ('wLanguage', c_ushort),
    ('wCountry', c_ushort),
    ('wCodePage', c_ushort),
]

LC_ID = struct_tagLC_ID# C:/msys64/ucrt64/include/corecrt.h: 447

LPLC_ID = POINTER(struct_tagLC_ID)# C:/msys64/ucrt64/include/corecrt.h: 447

struct_threadlocaleinfostruct.__slots__ = [
    '_locale_pctype',
    '_locale_mb_cur_max',
    '_locale_lc_codepage',
]
struct_threadlocaleinfostruct._fields_ = [
    ('_locale_pctype', POINTER(c_ushort)),
    ('_locale_mb_cur_max', c_int),
    ('_locale_lc_codepage', c_uint),
]

threadlocinfo = struct_threadlocaleinfostruct# C:/msys64/ucrt64/include/corecrt.h: 482

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 15
for _lib in _libs.values():
    if not _lib.has("_itow_s", "cdecl"):
        continue
    _itow_s = _lib.get("_itow_s", "cdecl")
    _itow_s.argtypes = [c_int, POINTER(c_wchar), c_size_t, c_int]
    _itow_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 18
for _lib in _libs.values():
    if not _lib.has("_ltow_s", "cdecl"):
        continue
    _ltow_s = _lib.get("_ltow_s", "cdecl")
    _ltow_s.argtypes = [c_long, POINTER(c_wchar), c_size_t, c_int]
    _ltow_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 21
for _lib in _libs.values():
    if not _lib.has("_ultow_s", "cdecl"):
        continue
    _ultow_s = _lib.get("_ultow_s", "cdecl")
    _ultow_s.argtypes = [c_ulong, POINTER(c_wchar), c_size_t, c_int]
    _ultow_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 24
for _lib in _libs.values():
    if not _lib.has("_wgetenv_s", "cdecl"):
        continue
    _wgetenv_s = _lib.get("_wgetenv_s", "cdecl")
    _wgetenv_s.argtypes = [POINTER(c_size_t), POINTER(c_wchar), c_size_t, POINTER(c_wchar)]
    _wgetenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 27
for _lib in _libs.values():
    if not _lib.has("_wdupenv_s", "cdecl"):
        continue
    _wdupenv_s = _lib.get("_wdupenv_s", "cdecl")
    _wdupenv_s.argtypes = [POINTER(POINTER(c_wchar)), POINTER(c_size_t), POINTER(c_wchar)]
    _wdupenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 28
for _lib in _libs.values():
    if not _lib.has("_i64tow_s", "cdecl"):
        continue
    _i64tow_s = _lib.get("_i64tow_s", "cdecl")
    _i64tow_s.argtypes = [c_int64, POINTER(c_wchar), c_size_t, c_int]
    _i64tow_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 31
for _lib in _libs.values():
    if not _lib.has("_wmakepath_s", "cdecl"):
        continue
    _wmakepath_s = _lib.get("_wmakepath_s", "cdecl")
    _wmakepath_s.argtypes = [POINTER(c_wchar), c_size_t, POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar)]
    _wmakepath_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 34
for _lib in _libs.values():
    if not _lib.has("_wputenv_s", "cdecl"):
        continue
    _wputenv_s = _lib.get("_wputenv_s", "cdecl")
    _wputenv_s.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    _wputenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 36
for _lib in _libs.values():
    if not _lib.has("_wsearchenv_s", "cdecl"):
        continue
    _wsearchenv_s = _lib.get("_wsearchenv_s", "cdecl")
    _wsearchenv_s.argtypes = [POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    _wsearchenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/corecrt_wstdlib.h: 39
for _lib in _libs.values():
    if not _lib.has("_wsplitpath_s", "cdecl"):
        continue
    _wsplitpath_s = _lib.get("_wsplitpath_s", "cdecl")
    _wsplitpath_s.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t, POINTER(c_wchar), c_size_t, POINTER(c_wchar), c_size_t, POINTER(c_wchar), c_size_t]
    _wsplitpath_s.restype = errno_t
    break

_onexit_t = CFUNCTYPE(UNCHECKED(c_int), )# C:/msys64/ucrt64/include/stdlib.h: 50

# C:/msys64/ucrt64/include/stdlib.h: 63
class struct__div_t(Structure):
    pass

struct__div_t.__slots__ = [
    'quot',
    'rem',
]
struct__div_t._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]

div_t = struct__div_t# C:/msys64/ucrt64/include/stdlib.h: 63

# C:/msys64/ucrt64/include/stdlib.h: 68
class struct__ldiv_t(Structure):
    pass

struct__ldiv_t.__slots__ = [
    'quot',
    'rem',
]
struct__ldiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]

ldiv_t = struct__ldiv_t# C:/msys64/ucrt64/include/stdlib.h: 68

# C:/msys64/ucrt64/include/stdlib.h: 77
class struct_anon_1(Structure):
    pass

struct_anon_1._pack_ = 4
struct_anon_1.__slots__ = [
    'ld',
]
struct_anon_1._fields_ = [
    ('ld', c_ubyte * int(10)),
]

_LDOUBLE = struct_anon_1# C:/msys64/ucrt64/include/stdlib.h: 77

# C:/msys64/ucrt64/include/stdlib.h: 84
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'x',
]
struct_anon_2._fields_ = [
    ('x', c_double),
]

_CRT_DOUBLE = struct_anon_2# C:/msys64/ucrt64/include/stdlib.h: 84

# C:/msys64/ucrt64/include/stdlib.h: 88
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'f',
]
struct_anon_3._fields_ = [
    ('f', c_float),
]

_CRT_FLOAT = struct_anon_3# C:/msys64/ucrt64/include/stdlib.h: 88

# C:/msys64/ucrt64/include/stdlib.h: 95
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'x',
]
struct_anon_4._fields_ = [
    ('x', c_longdouble),
]

_LONGDOUBLE = struct_anon_4# C:/msys64/ucrt64/include/stdlib.h: 95

# C:/msys64/ucrt64/include/stdlib.h: 102
class struct_anon_5(Structure):
    pass

struct_anon_5._pack_ = 4
struct_anon_5.__slots__ = [
    'ld12',
]
struct_anon_5._fields_ = [
    ('ld12', c_ubyte * int(12)),
]

_LDBL12 = struct_anon_5# C:/msys64/ucrt64/include/stdlib.h: 102

# C:/msys64/ucrt64/include/stdlib.h: 121
for _lib in _libs.values():
    if not _lib.has("___mb_cur_max_func", "cdecl"):
        continue
    ___mb_cur_max_func = _lib.get("___mb_cur_max_func", "cdecl")
    ___mb_cur_max_func.argtypes = []
    ___mb_cur_max_func.restype = c_int
    break

_purecall_handler = CFUNCTYPE(UNCHECKED(None), )# C:/msys64/ucrt64/include/stdlib.h: 143

# C:/msys64/ucrt64/include/stdlib.h: 145
for _lib in _libs.values():
    if not _lib.has("_set_purecall_handler", "cdecl"):
        continue
    _set_purecall_handler = _lib.get("_set_purecall_handler", "cdecl")
    _set_purecall_handler.argtypes = [_purecall_handler]
    _set_purecall_handler.restype = _purecall_handler
    break

# C:/msys64/ucrt64/include/stdlib.h: 146
for _lib in _libs.values():
    if not _lib.has("_get_purecall_handler", "cdecl"):
        continue
    _get_purecall_handler = _lib.get("_get_purecall_handler", "cdecl")
    _get_purecall_handler.argtypes = []
    _get_purecall_handler.restype = _purecall_handler
    break

# C:/msys64/ucrt64/include/stdlib.h: 154
for _lib in _libs.values():
    if not _lib.has("_errno", "cdecl"):
        continue
    _errno = _lib.get("_errno", "cdecl")
    _errno.argtypes = []
    _errno.restype = POINTER(c_int)
    break

# C:/msys64/ucrt64/include/stdlib.h: 156
for _lib in _libs.values():
    if not _lib.has("_set_errno", "cdecl"):
        continue
    _set_errno = _lib.get("_set_errno", "cdecl")
    _set_errno.argtypes = [c_int]
    _set_errno.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 157
for _lib in _libs.values():
    if not _lib.has("_get_errno", "cdecl"):
        continue
    _get_errno = _lib.get("_get_errno", "cdecl")
    _get_errno.argtypes = [POINTER(c_int)]
    _get_errno.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 159
for _lib in _libs.values():
    if not _lib.has("__doserrno", "cdecl"):
        continue
    __doserrno = _lib.get("__doserrno", "cdecl")
    __doserrno.argtypes = []
    __doserrno.restype = POINTER(c_ulong)
    break

# C:/msys64/ucrt64/include/stdlib.h: 161
for _lib in _libs.values():
    if not _lib.has("_set_doserrno", "cdecl"):
        continue
    _set_doserrno = _lib.get("_set_doserrno", "cdecl")
    _set_doserrno.argtypes = [c_ulong]
    _set_doserrno.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 162
for _lib in _libs.values():
    if not _lib.has("_get_doserrno", "cdecl"):
        continue
    _get_doserrno = _lib.get("_get_doserrno", "cdecl")
    _get_doserrno.argtypes = [POINTER(c_ulong)]
    _get_doserrno.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 168
for _lib in _libs.values():
    if not _lib.has("__sys_errlist", "cdecl"):
        continue
    __sys_errlist = _lib.get("__sys_errlist", "cdecl")
    __sys_errlist.argtypes = []
    __sys_errlist.restype = POINTER(POINTER(c_char))
    break

# C:/msys64/ucrt64/include/stdlib.h: 169
for _lib in _libs.values():
    if not _lib.has("__sys_nerr", "cdecl"):
        continue
    __sys_nerr = _lib.get("__sys_nerr", "cdecl")
    __sys_nerr.argtypes = []
    __sys_nerr.restype = POINTER(c_int)
    break

# C:/msys64/ucrt64/include/stdlib.h: 180
for _lib in _libs.values():
    if not _lib.has("__p___argv", "cdecl"):
        continue
    __p___argv = _lib.get("__p___argv", "cdecl")
    __p___argv.argtypes = []
    __p___argv.restype = POINTER(POINTER(POINTER(c_char)))
    break

# C:/msys64/ucrt64/include/stdlib.h: 181
for _lib in _libs.values():
    if not _lib.has("__p__fmode", "cdecl"):
        continue
    __p__fmode = _lib.get("__p__fmode", "cdecl")
    __p__fmode.argtypes = []
    __p__fmode.restype = POINTER(c_int)
    break

# C:/msys64/ucrt64/include/stdlib.h: 183
for _lib in _libs.values():
    if not _lib.has("__p___argc", "cdecl"):
        continue
    __p___argc = _lib.get("__p___argc", "cdecl")
    __p___argc.argtypes = []
    __p___argc.restype = POINTER(c_int)
    break

# C:/msys64/ucrt64/include/stdlib.h: 184
for _lib in _libs.values():
    if not _lib.has("__p___wargv", "cdecl"):
        continue
    __p___wargv = _lib.get("__p___wargv", "cdecl")
    __p___wargv.argtypes = []
    __p___wargv.restype = POINTER(POINTER(POINTER(c_wchar)))
    break

# C:/msys64/ucrt64/include/stdlib.h: 185
for _lib in _libs.values():
    if not _lib.has("__p__environ", "cdecl"):
        continue
    __p__environ = _lib.get("__p__environ", "cdecl")
    __p__environ.argtypes = []
    __p__environ.restype = POINTER(POINTER(POINTER(c_char)))
    break

# C:/msys64/ucrt64/include/stdlib.h: 186
for _lib in _libs.values():
    if not _lib.has("__p__wenviron", "cdecl"):
        continue
    __p__wenviron = _lib.get("__p__wenviron", "cdecl")
    __p__wenviron.argtypes = []
    __p__wenviron.restype = POINTER(POINTER(POINTER(c_wchar)))
    break

# C:/msys64/ucrt64/include/stdlib.h: 187
for _lib in _libs.values():
    if not _lib.has("__p__pgmptr", "cdecl"):
        continue
    __p__pgmptr = _lib.get("__p__pgmptr", "cdecl")
    __p__pgmptr.argtypes = []
    __p__pgmptr.restype = POINTER(POINTER(c_char))
    break

# C:/msys64/ucrt64/include/stdlib.h: 188
for _lib in _libs.values():
    if not _lib.has("__p__wpgmptr", "cdecl"):
        continue
    __p__wpgmptr = _lib.get("__p__wpgmptr", "cdecl")
    __p__wpgmptr.argtypes = []
    __p__wpgmptr.restype = POINTER(POINTER(c_wchar))
    break

# C:/msys64/ucrt64/include/stdlib.h: 191
for _lib in _libs.values():
    if not _lib.has("_get_pgmptr", "cdecl"):
        continue
    _get_pgmptr = _lib.get("_get_pgmptr", "cdecl")
    _get_pgmptr.argtypes = [POINTER(POINTER(c_char))]
    _get_pgmptr.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 192
for _lib in _libs.values():
    if not _lib.has("_get_wpgmptr", "cdecl"):
        continue
    _get_wpgmptr = _lib.get("_get_wpgmptr", "cdecl")
    _get_wpgmptr.argtypes = [POINTER(POINTER(c_wchar))]
    _get_wpgmptr.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 193
for _lib in _libs.values():
    if not _lib.has("_set_fmode", "cdecl"):
        continue
    _set_fmode = _lib.get("_set_fmode", "cdecl")
    _set_fmode.argtypes = [c_int]
    _set_fmode.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 194
for _lib in _libs.values():
    if not _lib.has("_get_fmode", "cdecl"):
        continue
    _get_fmode = _lib.get("_get_fmode", "cdecl")
    _get_fmode.argtypes = [POINTER(c_int)]
    _get_fmode.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 370
for _lib in _libs.values():
    if not _lib.has("_get_osplatform", "cdecl"):
        continue
    _get_osplatform = _lib.get("_get_osplatform", "cdecl")
    _get_osplatform.argtypes = [POINTER(c_uint)]
    _get_osplatform.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 371
for _lib in _libs.values():
    if not _lib.has("_get_osver", "cdecl"):
        continue
    _get_osver = _lib.get("_get_osver", "cdecl")
    _get_osver.argtypes = [POINTER(c_uint)]
    _get_osver.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 372
for _lib in _libs.values():
    if not _lib.has("_get_winver", "cdecl"):
        continue
    _get_winver = _lib.get("_get_winver", "cdecl")
    _get_winver.argtypes = [POINTER(c_uint)]
    _get_winver.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 373
for _lib in _libs.values():
    if not _lib.has("_get_winmajor", "cdecl"):
        continue
    _get_winmajor = _lib.get("_get_winmajor", "cdecl")
    _get_winmajor.argtypes = [POINTER(c_uint)]
    _get_winmajor.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 374
for _lib in _libs.values():
    if not _lib.has("_get_winminor", "cdecl"):
        continue
    _get_winminor = _lib.get("_get_winminor", "cdecl")
    _get_winminor.argtypes = [POINTER(c_uint)]
    _get_winminor.restype = errno_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 388
for _lib in _libs.values():
    if not _lib.has("exit", "cdecl"):
        continue
    exit = _lib.get("exit", "cdecl")
    exit.argtypes = [c_int]
    exit.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 389
for _lib in _libs.values():
    if not _lib.has("_exit", "cdecl"):
        continue
    _exit = _lib.get("_exit", "cdecl")
    _exit.argtypes = [c_int]
    _exit.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 391
for _lib in _libs.values():
    if not _lib.has("quick_exit", "cdecl"):
        continue
    quick_exit = _lib.get("quick_exit", "cdecl")
    quick_exit.argtypes = [c_int]
    quick_exit.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 396
for _lib in _libs.values():
    if not _lib.has("_Exit", "cdecl"):
        continue
    _Exit = _lib.get("_Exit", "cdecl")
    _Exit.argtypes = [c_int]
    _Exit.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 410
for _lib in _libs.values():
    if not _lib.has("_set_abort_behavior", "cdecl"):
        continue
    _set_abort_behavior = _lib.get("_set_abort_behavior", "cdecl")
    _set_abort_behavior.argtypes = [c_uint, c_uint]
    _set_abort_behavior.restype = c_uint
    break

# C:/msys64/ucrt64/include/stdlib.h: 414
for _lib in _libs.values():
    if not _lib.has("abs", "cdecl"):
        continue
    abs = _lib.get("abs", "cdecl")
    abs.argtypes = [c_int]
    abs.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 415
for _lib in _libs.values():
    if not _lib.has("labs", "cdecl"):
        continue
    labs = _lib.get("labs", "cdecl")
    labs.argtypes = [c_long]
    labs.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 418
for _lib in _libs.values():
    if not _lib.has("_abs64", "cdecl"):
        continue
    _abs64 = _lib.get("_abs64", "cdecl")
    _abs64.argtypes = [c_int64]
    _abs64.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 425
for _lib in _libs.values():
    if not _lib.has("atexit", "cdecl"):
        continue
    atexit = _lib.get("atexit", "cdecl")
    atexit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    atexit.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 427
for _lib in _libs.values():
    if not _lib.has("at_quick_exit", "cdecl"):
        continue
    at_quick_exit = _lib.get("at_quick_exit", "cdecl")
    at_quick_exit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    at_quick_exit.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 431
for _lib in _libs.values():
    if not _lib.has("atof", "cdecl"):
        continue
    atof = _lib.get("atof", "cdecl")
    atof.argtypes = [String]
    atof.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 432
for _lib in _libs.values():
    if not _lib.has("_atof_l", "cdecl"):
        continue
    _atof_l = _lib.get("_atof_l", "cdecl")
    _atof_l.argtypes = [String, _locale_t]
    _atof_l.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 434
for _lib in _libs.values():
    if not _lib.has("atoi", "cdecl"):
        continue
    atoi = _lib.get("atoi", "cdecl")
    atoi.argtypes = [String]
    atoi.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 435
for _lib in _libs.values():
    if not _lib.has("_atoi_l", "cdecl"):
        continue
    _atoi_l = _lib.get("_atoi_l", "cdecl")
    _atoi_l.argtypes = [String, _locale_t]
    _atoi_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 436
for _lib in _libs.values():
    if not _lib.has("atol", "cdecl"):
        continue
    atol = _lib.get("atol", "cdecl")
    atol.argtypes = [String]
    atol.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 437
for _lib in _libs.values():
    if not _lib.has("_atol_l", "cdecl"):
        continue
    _atol_l = _lib.get("_atol_l", "cdecl")
    _atol_l.argtypes = [String, _locale_t]
    _atol_l.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 440
for _lib in _libs.values():
    if not _lib.has("bsearch", "cdecl"):
        continue
    bsearch = _lib.get("bsearch", "cdecl")
    bsearch.argtypes = [POINTER(None), POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    bsearch.restype = POINTER(c_ubyte)
    bsearch.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 441
for _lib in _libs.values():
    if not _lib.has("qsort", "cdecl"):
        continue
    qsort = _lib.get("qsort", "cdecl")
    qsort.argtypes = [POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    qsort.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 443
for _lib in _libs.values():
    if not _lib.has("_byteswap_ushort", "cdecl"):
        continue
    _byteswap_ushort = _lib.get("_byteswap_ushort", "cdecl")
    _byteswap_ushort.argtypes = [c_ushort]
    _byteswap_ushort.restype = c_ushort
    break

# C:/msys64/ucrt64/include/stdlib.h: 444
for _lib in _libs.values():
    if not _lib.has("_byteswap_ulong", "cdecl"):
        continue
    _byteswap_ulong = _lib.get("_byteswap_ulong", "cdecl")
    _byteswap_ulong.argtypes = [c_ulong]
    _byteswap_ulong.restype = c_ulong
    break

# C:/msys64/ucrt64/include/stdlib.h: 446
for _lib in _libs.values():
    if not _lib.has("div", "cdecl"):
        continue
    div = _lib.get("div", "cdecl")
    div.argtypes = [c_int, c_int]
    div.restype = div_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 447
for _lib in _libs.values():
    if not _lib.has("getenv", "cdecl"):
        continue
    getenv = _lib.get("getenv", "cdecl")
    getenv.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getenv.restype = ReturnString
    else:
        getenv.restype = String
        getenv.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 448
for _lib in _libs.values():
    if not _lib.has("_itoa", "cdecl"):
        continue
    _itoa = _lib.get("_itoa", "cdecl")
    _itoa.argtypes = [c_int, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        _itoa.restype = ReturnString
    else:
        _itoa.restype = String
        _itoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 449
for _lib in _libs.values():
    if not _lib.has("_i64toa", "cdecl"):
        continue
    _i64toa = _lib.get("_i64toa", "cdecl")
    _i64toa.argtypes = [c_int64, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        _i64toa.restype = ReturnString
    else:
        _i64toa.restype = String
        _i64toa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 451
for _lib in _libs.values():
    if not _lib.has("_atoi64", "cdecl"):
        continue
    _atoi64 = _lib.get("_atoi64", "cdecl")
    _atoi64.argtypes = [String]
    _atoi64.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 452
for _lib in _libs.values():
    if not _lib.has("_atoi64_l", "cdecl"):
        continue
    _atoi64_l = _lib.get("_atoi64_l", "cdecl")
    _atoi64_l.argtypes = [String, _locale_t]
    _atoi64_l.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 453
for _lib in _libs.values():
    if not _lib.has("_strtoi64", "cdecl"):
        continue
    _strtoi64 = _lib.get("_strtoi64", "cdecl")
    _strtoi64.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    _strtoi64.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 454
for _lib in _libs.values():
    if not _lib.has("_strtoi64_l", "cdecl"):
        continue
    _strtoi64_l = _lib.get("_strtoi64_l", "cdecl")
    _strtoi64_l.argtypes = [String, POINTER(POINTER(c_char)), c_int, _locale_t]
    _strtoi64_l.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 457
for _lib in _libs.values():
    if not _lib.has("ldiv", "cdecl"):
        continue
    ldiv = _lib.get("ldiv", "cdecl")
    ldiv.argtypes = [c_long, c_long]
    ldiv.restype = ldiv_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 458
for _lib in _libs.values():
    if not _lib.has("_ltoa", "cdecl"):
        continue
    _ltoa = _lib.get("_ltoa", "cdecl")
    _ltoa.argtypes = [c_long, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        _ltoa.restype = ReturnString
    else:
        _ltoa.restype = String
        _ltoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 459
for _lib in _libs.values():
    if not _lib.has("mblen", "cdecl"):
        continue
    mblen = _lib.get("mblen", "cdecl")
    mblen.argtypes = [String, c_size_t]
    mblen.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 460
for _lib in _libs.values():
    if not _lib.has("_mblen_l", "cdecl"):
        continue
    _mblen_l = _lib.get("_mblen_l", "cdecl")
    _mblen_l.argtypes = [String, c_size_t, _locale_t]
    _mblen_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 461
for _lib in _libs.values():
    if not _lib.has("_mbstrlen", "cdecl"):
        continue
    _mbstrlen = _lib.get("_mbstrlen", "cdecl")
    _mbstrlen.argtypes = [String]
    _mbstrlen.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 462
for _lib in _libs.values():
    if not _lib.has("_mbstrlen_l", "cdecl"):
        continue
    _mbstrlen_l = _lib.get("_mbstrlen_l", "cdecl")
    _mbstrlen_l.argtypes = [String, _locale_t]
    _mbstrlen_l.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 463
for _lib in _libs.values():
    if not _lib.has("_mbstrnlen", "cdecl"):
        continue
    _mbstrnlen = _lib.get("_mbstrnlen", "cdecl")
    _mbstrnlen.argtypes = [String, c_size_t]
    _mbstrnlen.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 464
for _lib in _libs.values():
    if not _lib.has("_mbstrnlen_l", "cdecl"):
        continue
    _mbstrnlen_l = _lib.get("_mbstrnlen_l", "cdecl")
    _mbstrnlen_l.argtypes = [String, c_size_t, _locale_t]
    _mbstrnlen_l.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 465
for _lib in _libs.values():
    if not _lib.has("mbtowc", "cdecl"):
        continue
    mbtowc = _lib.get("mbtowc", "cdecl")
    mbtowc.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbtowc.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 466
for _lib in _libs.values():
    if not _lib.has("_mbtowc_l", "cdecl"):
        continue
    _mbtowc_l = _lib.get("_mbtowc_l", "cdecl")
    _mbtowc_l.argtypes = [POINTER(c_wchar), String, c_size_t, _locale_t]
    _mbtowc_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 467
for _lib in _libs.values():
    if not _lib.has("mbstowcs", "cdecl"):
        continue
    mbstowcs = _lib.get("mbstowcs", "cdecl")
    mbstowcs.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbstowcs.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 468
for _lib in _libs.values():
    if not _lib.has("_mbstowcs_l", "cdecl"):
        continue
    _mbstowcs_l = _lib.get("_mbstowcs_l", "cdecl")
    _mbstowcs_l.argtypes = [POINTER(c_wchar), String, c_size_t, _locale_t]
    _mbstowcs_l.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 469
for _lib in _libs.values():
    if not _lib.has("mkstemp", "cdecl"):
        continue
    mkstemp = _lib.get("mkstemp", "cdecl")
    mkstemp.argtypes = [String]
    mkstemp.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 470
for _lib in _libs.values():
    if not _lib.has("rand", "cdecl"):
        continue
    rand = _lib.get("rand", "cdecl")
    rand.argtypes = []
    rand.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 471
for _lib in _libs.values():
    if not _lib.has("_set_error_mode", "cdecl"):
        continue
    _set_error_mode = _lib.get("_set_error_mode", "cdecl")
    _set_error_mode.argtypes = [c_int]
    _set_error_mode.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 472
for _lib in _libs.values():
    if not _lib.has("srand", "cdecl"):
        continue
    srand = _lib.get("srand", "cdecl")
    srand.argtypes = [c_uint]
    srand.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 499
for _lib in _libs.values():
    if not _lib.has("strtod", "cdecl"):
        continue
    strtod = _lib.get("strtod", "cdecl")
    strtod.argtypes = [String, POINTER(POINTER(c_char))]
    strtod.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 500
for _lib in _libs.values():
    if not _lib.has("strtof", "cdecl"):
        continue
    strtof = _lib.get("strtof", "cdecl")
    strtof.argtypes = [String, POINTER(POINTER(c_char))]
    strtof.restype = c_float
    break

# C:/msys64/ucrt64/include/stdlib.h: 502
for _lib in _libs.values():
    if not _lib.has("strtold", "cdecl"):
        continue
    strtold = _lib.get("strtold", "cdecl")
    strtold.argtypes = [String, POINTER(POINTER(c_char))]
    strtold.restype = c_longdouble
    break

# C:/msys64/ucrt64/include/stdlib.h: 506
for _lib in _libs.values():
    if not _lib.has("__strtod", "cdecl"):
        continue
    __strtod = _lib.get("__strtod", "cdecl")
    __strtod.argtypes = [String, POINTER(POINTER(c_char))]
    __strtod.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 514
for _lib in _libs.values():
    if not _lib.has("__mingw_strtof", "cdecl"):
        continue
    __mingw_strtof = _lib.get("__mingw_strtof", "cdecl")
    __mingw_strtof.argtypes = [String, POINTER(POINTER(c_char))]
    __mingw_strtof.restype = c_float
    break

# C:/msys64/ucrt64/include/stdlib.h: 515
for _lib in _libs.values():
    if not _lib.has("__mingw_strtod", "cdecl"):
        continue
    __mingw_strtod = _lib.get("__mingw_strtod", "cdecl")
    __mingw_strtod.argtypes = [String, POINTER(POINTER(c_char))]
    __mingw_strtod.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 516
for _lib in _libs.values():
    if not _lib.has("__mingw_strtold", "cdecl"):
        continue
    __mingw_strtold = _lib.get("__mingw_strtold", "cdecl")
    __mingw_strtold.argtypes = [String, POINTER(POINTER(c_char))]
    __mingw_strtold.restype = c_longdouble
    break

# C:/msys64/ucrt64/include/stdlib.h: 518
for _lib in _libs.values():
    if not _lib.has("_strtof_l", "cdecl"):
        continue
    _strtof_l = _lib.get("_strtof_l", "cdecl")
    _strtof_l.argtypes = [String, POINTER(POINTER(c_char)), _locale_t]
    _strtof_l.restype = c_float
    break

# C:/msys64/ucrt64/include/stdlib.h: 519
for _lib in _libs.values():
    if not _lib.has("_strtod_l", "cdecl"):
        continue
    _strtod_l = _lib.get("_strtod_l", "cdecl")
    _strtod_l.argtypes = [String, POINTER(POINTER(c_char)), _locale_t]
    _strtod_l.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 520
for _lib in _libs.values():
    if not _lib.has("strtol", "cdecl"):
        continue
    strtol = _lib.get("strtol", "cdecl")
    strtol.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtol.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 521
for _lib in _libs.values():
    if not _lib.has("_strtol_l", "cdecl"):
        continue
    _strtol_l = _lib.get("_strtol_l", "cdecl")
    _strtol_l.argtypes = [String, POINTER(POINTER(c_char)), c_int, _locale_t]
    _strtol_l.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 522
for _lib in _libs.values():
    if not _lib.has("strtoul", "cdecl"):
        continue
    strtoul = _lib.get("strtoul", "cdecl")
    strtoul.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoul.restype = c_ulong
    break

# C:/msys64/ucrt64/include/stdlib.h: 523
for _lib in _libs.values():
    if not _lib.has("_strtoul_l", "cdecl"):
        continue
    _strtoul_l = _lib.get("_strtoul_l", "cdecl")
    _strtoul_l.argtypes = [String, POINTER(POINTER(c_char)), c_int, _locale_t]
    _strtoul_l.restype = c_ulong
    break

# C:/msys64/ucrt64/include/stdlib.h: 526
for _lib in _libs.values():
    if not _lib.has("system", "cdecl"):
        continue
    system = _lib.get("system", "cdecl")
    system.argtypes = [String]
    system.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 528
for _lib in _libs.values():
    if not _lib.has("_ultoa", "cdecl"):
        continue
    _ultoa = _lib.get("_ultoa", "cdecl")
    _ultoa.argtypes = [c_ulong, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        _ultoa.restype = ReturnString
    else:
        _ultoa.restype = String
        _ultoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 529
for _lib in _libs.values():
    if not _lib.has("wctomb", "cdecl"):
        continue
    wctomb = _lib.get("wctomb", "cdecl")
    wctomb.argtypes = [String, c_wchar]
    wctomb.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 530
for _lib in _libs.values():
    if not _lib.has("_wctomb_l", "cdecl"):
        continue
    _wctomb_l = _lib.get("_wctomb_l", "cdecl")
    _wctomb_l.argtypes = [String, c_wchar, _locale_t]
    _wctomb_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 531
for _lib in _libs.values():
    if not _lib.has("wcstombs", "cdecl"):
        continue
    wcstombs = _lib.get("wcstombs", "cdecl")
    wcstombs.argtypes = [String, POINTER(c_wchar), c_size_t]
    wcstombs.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 532
for _lib in _libs.values():
    if not _lib.has("_wcstombs_l", "cdecl"):
        continue
    _wcstombs_l = _lib.get("_wcstombs_l", "cdecl")
    _wcstombs_l.argtypes = [String, POINTER(c_wchar), c_size_t, _locale_t]
    _wcstombs_l.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 536
for _lib in _libs.values():
    if not _lib.has("calloc", "cdecl"):
        continue
    calloc = _lib.get("calloc", "cdecl")
    calloc.argtypes = [c_size_t, c_size_t]
    calloc.restype = POINTER(c_ubyte)
    calloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 537
for _lib in _libs.values():
    if not _lib.has("free", "cdecl"):
        continue
    free = _lib.get("free", "cdecl")
    free.argtypes = [POINTER(None)]
    free.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 538
for _lib in _libs.values():
    if not _lib.has("malloc", "cdecl"):
        continue
    malloc = _lib.get("malloc", "cdecl")
    malloc.argtypes = [c_size_t]
    malloc.restype = POINTER(c_ubyte)
    malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 539
for _lib in _libs.values():
    if not _lib.has("realloc", "cdecl"):
        continue
    realloc = _lib.get("realloc", "cdecl")
    realloc.argtypes = [POINTER(None), c_size_t]
    realloc.restype = POINTER(c_ubyte)
    realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 540
for _lib in _libs.values():
    if not _lib.has("_aligned_free", "cdecl"):
        continue
    _aligned_free = _lib.get("_aligned_free", "cdecl")
    _aligned_free.argtypes = [POINTER(None)]
    _aligned_free.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 541
for _lib in _libs.values():
    if not _lib.has("_aligned_malloc", "cdecl"):
        continue
    _aligned_malloc = _lib.get("_aligned_malloc", "cdecl")
    _aligned_malloc.argtypes = [c_size_t, c_size_t]
    _aligned_malloc.restype = POINTER(c_ubyte)
    _aligned_malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 542
for _lib in _libs.values():
    if not _lib.has("_aligned_offset_malloc", "cdecl"):
        continue
    _aligned_offset_malloc = _lib.get("_aligned_offset_malloc", "cdecl")
    _aligned_offset_malloc.argtypes = [c_size_t, c_size_t, c_size_t]
    _aligned_offset_malloc.restype = POINTER(c_ubyte)
    _aligned_offset_malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 543
for _lib in _libs.values():
    if not _lib.has("_aligned_realloc", "cdecl"):
        continue
    _aligned_realloc = _lib.get("_aligned_realloc", "cdecl")
    _aligned_realloc.argtypes = [POINTER(None), c_size_t, c_size_t]
    _aligned_realloc.restype = POINTER(c_ubyte)
    _aligned_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 544
for _lib in _libs.values():
    if not _lib.has("_aligned_offset_realloc", "cdecl"):
        continue
    _aligned_offset_realloc = _lib.get("_aligned_offset_realloc", "cdecl")
    _aligned_offset_realloc.argtypes = [POINTER(None), c_size_t, c_size_t, c_size_t]
    _aligned_offset_realloc.restype = POINTER(c_ubyte)
    _aligned_offset_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 546
for _lib in _libs.values():
    if not _lib.has("_recalloc", "cdecl"):
        continue
    _recalloc = _lib.get("_recalloc", "cdecl")
    _recalloc.argtypes = [POINTER(None), c_size_t, c_size_t]
    _recalloc.restype = POINTER(c_ubyte)
    _recalloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 547
for _lib in _libs.values():
    if not _lib.has("_aligned_recalloc", "cdecl"):
        continue
    _aligned_recalloc = _lib.get("_aligned_recalloc", "cdecl")
    _aligned_recalloc.argtypes = [POINTER(None), c_size_t, c_size_t, c_size_t]
    _aligned_recalloc.restype = POINTER(c_ubyte)
    _aligned_recalloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 548
for _lib in _libs.values():
    if not _lib.has("_aligned_offset_recalloc", "cdecl"):
        continue
    _aligned_offset_recalloc = _lib.get("_aligned_offset_recalloc", "cdecl")
    _aligned_offset_recalloc.argtypes = [POINTER(None), c_size_t, c_size_t, c_size_t, c_size_t]
    _aligned_offset_recalloc.restype = POINTER(c_ubyte)
    _aligned_offset_recalloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/stdlib.h: 549
for _lib in _libs.values():
    if not _lib.has("_aligned_msize", "cdecl"):
        continue
    _aligned_msize = _lib.get("_aligned_msize", "cdecl")
    _aligned_msize.argtypes = [POINTER(None), c_size_t, c_size_t]
    _aligned_msize.restype = c_size_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 556
for _lib in _libs.values():
    if not _lib.has("_itow", "cdecl"):
        continue
    _itow = _lib.get("_itow", "cdecl")
    _itow.argtypes = [c_int, POINTER(c_wchar), c_int]
    _itow.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/stdlib.h: 557
for _lib in _libs.values():
    if not _lib.has("_ltow", "cdecl"):
        continue
    _ltow = _lib.get("_ltow", "cdecl")
    _ltow.argtypes = [c_long, POINTER(c_wchar), c_int]
    _ltow.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/stdlib.h: 558
for _lib in _libs.values():
    if not _lib.has("_ultow", "cdecl"):
        continue
    _ultow = _lib.get("_ultow", "cdecl")
    _ultow.argtypes = [c_ulong, POINTER(c_wchar), c_int]
    _ultow.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/stdlib.h: 560
for _lib in _libs.values():
    if not _lib.has("__mingw_wcstod", "cdecl"):
        continue
    __mingw_wcstod = _lib.get("__mingw_wcstod", "cdecl")
    __mingw_wcstod.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar))]
    __mingw_wcstod.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 561
for _lib in _libs.values():
    if not _lib.has("__mingw_wcstof", "cdecl"):
        continue
    __mingw_wcstof = _lib.get("__mingw_wcstof", "cdecl")
    __mingw_wcstof.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar))]
    __mingw_wcstof.restype = c_float
    break

# C:/msys64/ucrt64/include/stdlib.h: 562
for _lib in _libs.values():
    if not _lib.has("__mingw_wcstold", "cdecl"):
        continue
    __mingw_wcstold = _lib.get("__mingw_wcstold", "cdecl")
    __mingw_wcstold.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar))]
    __mingw_wcstold.restype = c_longdouble
    break

# C:/msys64/ucrt64/include/stdlib.h: 575
for _lib in _libs.values():
    if not _lib.has("wcstod", "cdecl"):
        continue
    wcstod = _lib.get("wcstod", "cdecl")
    wcstod.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar))]
    wcstod.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 576
for _lib in _libs.values():
    if not _lib.has("wcstof", "cdecl"):
        continue
    wcstof = _lib.get("wcstof", "cdecl")
    wcstof.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar))]
    wcstof.restype = c_float
    break

# C:/msys64/ucrt64/include/stdlib.h: 579
for _lib in _libs.values():
    if not _lib.has("wcstold", "cdecl"):
        continue
    wcstold = _lib.get("wcstold", "cdecl")
    wcstold.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar))]
    wcstold.restype = c_longdouble
    break

# C:/msys64/ucrt64/include/stdlib.h: 581
for _lib in _libs.values():
    if not _lib.has("_wcstod_l", "cdecl"):
        continue
    _wcstod_l = _lib.get("_wcstod_l", "cdecl")
    _wcstod_l.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), _locale_t]
    _wcstod_l.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 582
for _lib in _libs.values():
    if not _lib.has("_wcstof_l", "cdecl"):
        continue
    _wcstof_l = _lib.get("_wcstof_l", "cdecl")
    _wcstof_l.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), _locale_t]
    _wcstof_l.restype = c_float
    break

# C:/msys64/ucrt64/include/stdlib.h: 583
for _lib in _libs.values():
    if not _lib.has("wcstol", "cdecl"):
        continue
    wcstol = _lib.get("wcstol", "cdecl")
    wcstol.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), c_int]
    wcstol.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 584
for _lib in _libs.values():
    if not _lib.has("_wcstol_l", "cdecl"):
        continue
    _wcstol_l = _lib.get("_wcstol_l", "cdecl")
    _wcstol_l.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), c_int, _locale_t]
    _wcstol_l.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 585
for _lib in _libs.values():
    if not _lib.has("wcstoul", "cdecl"):
        continue
    wcstoul = _lib.get("wcstoul", "cdecl")
    wcstoul.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), c_int]
    wcstoul.restype = c_ulong
    break

# C:/msys64/ucrt64/include/stdlib.h: 586
for _lib in _libs.values():
    if not _lib.has("_wcstoul_l", "cdecl"):
        continue
    _wcstoul_l = _lib.get("_wcstoul_l", "cdecl")
    _wcstoul_l.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), c_int, _locale_t]
    _wcstoul_l.restype = c_ulong
    break

# C:/msys64/ucrt64/include/stdlib.h: 587
for _lib in _libs.values():
    if not _lib.has("_wgetenv", "cdecl"):
        continue
    _wgetenv = _lib.get("_wgetenv", "cdecl")
    _wgetenv.argtypes = [POINTER(c_wchar)]
    _wgetenv.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/stdlib.h: 590
for _lib in _libs.values():
    if not _lib.has("_wsystem", "cdecl"):
        continue
    _wsystem = _lib.get("_wsystem", "cdecl")
    _wsystem.argtypes = [POINTER(c_wchar)]
    _wsystem.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 592
for _lib in _libs.values():
    if not _lib.has("_wtof", "cdecl"):
        continue
    _wtof = _lib.get("_wtof", "cdecl")
    _wtof.argtypes = [POINTER(c_wchar)]
    _wtof.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 593
for _lib in _libs.values():
    if not _lib.has("_wtof_l", "cdecl"):
        continue
    _wtof_l = _lib.get("_wtof_l", "cdecl")
    _wtof_l.argtypes = [POINTER(c_wchar), _locale_t]
    _wtof_l.restype = c_double
    break

# C:/msys64/ucrt64/include/stdlib.h: 594
for _lib in _libs.values():
    if not _lib.has("_wtoi", "cdecl"):
        continue
    _wtoi = _lib.get("_wtoi", "cdecl")
    _wtoi.argtypes = [POINTER(c_wchar)]
    _wtoi.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 595
for _lib in _libs.values():
    if not _lib.has("_wtoi_l", "cdecl"):
        continue
    _wtoi_l = _lib.get("_wtoi_l", "cdecl")
    _wtoi_l.argtypes = [POINTER(c_wchar), _locale_t]
    _wtoi_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 596
for _lib in _libs.values():
    if not _lib.has("_wtol", "cdecl"):
        continue
    _wtol = _lib.get("_wtol", "cdecl")
    _wtol.argtypes = [POINTER(c_wchar)]
    _wtol.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 597
for _lib in _libs.values():
    if not _lib.has("_wtol_l", "cdecl"):
        continue
    _wtol_l = _lib.get("_wtol_l", "cdecl")
    _wtol_l.argtypes = [POINTER(c_wchar), _locale_t]
    _wtol_l.restype = c_long
    break

# C:/msys64/ucrt64/include/stdlib.h: 599
for _lib in _libs.values():
    if not _lib.has("_i64tow", "cdecl"):
        continue
    _i64tow = _lib.get("_i64tow", "cdecl")
    _i64tow.argtypes = [c_int64, POINTER(c_wchar), c_int]
    _i64tow.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/stdlib.h: 601
for _lib in _libs.values():
    if not _lib.has("_wtoi64", "cdecl"):
        continue
    _wtoi64 = _lib.get("_wtoi64", "cdecl")
    _wtoi64.argtypes = [POINTER(c_wchar)]
    _wtoi64.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 602
for _lib in _libs.values():
    if not _lib.has("_wtoi64_l", "cdecl"):
        continue
    _wtoi64_l = _lib.get("_wtoi64_l", "cdecl")
    _wtoi64_l.argtypes = [POINTER(c_wchar), _locale_t]
    _wtoi64_l.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 603
for _lib in _libs.values():
    if not _lib.has("_wcstoi64", "cdecl"):
        continue
    _wcstoi64 = _lib.get("_wcstoi64", "cdecl")
    _wcstoi64.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), c_int]
    _wcstoi64.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 604
for _lib in _libs.values():
    if not _lib.has("_wcstoi64_l", "cdecl"):
        continue
    _wcstoi64_l = _lib.get("_wcstoi64_l", "cdecl")
    _wcstoi64_l.argtypes = [POINTER(c_wchar), POINTER(POINTER(c_wchar)), c_int, _locale_t]
    _wcstoi64_l.restype = c_int64
    break

# C:/msys64/ucrt64/include/stdlib.h: 609
for _lib in _libs.values():
    if not _lib.has("_putenv", "cdecl"):
        continue
    _putenv = _lib.get("_putenv", "cdecl")
    _putenv.argtypes = [String]
    _putenv.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 610
for _lib in _libs.values():
    if not _lib.has("_wputenv", "cdecl"):
        continue
    _wputenv = _lib.get("_wputenv", "cdecl")
    _wputenv.argtypes = [POINTER(c_wchar)]
    _wputenv.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 614
for _lib in _libs.values():
    if not _lib.has("_fullpath", "cdecl"):
        continue
    _fullpath = _lib.get("_fullpath", "cdecl")
    _fullpath.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        _fullpath.restype = ReturnString
    else:
        _fullpath.restype = String
        _fullpath.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 615
for _lib in _libs.values():
    if not _lib.has("_ecvt", "cdecl"):
        continue
    _ecvt = _lib.get("_ecvt", "cdecl")
    _ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        _ecvt.restype = ReturnString
    else:
        _ecvt.restype = String
        _ecvt.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 616
for _lib in _libs.values():
    if not _lib.has("_fcvt", "cdecl"):
        continue
    _fcvt = _lib.get("_fcvt", "cdecl")
    _fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        _fcvt.restype = ReturnString
    else:
        _fcvt.restype = String
        _fcvt.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 617
for _lib in _libs.values():
    if not _lib.has("_gcvt", "cdecl"):
        continue
    _gcvt = _lib.get("_gcvt", "cdecl")
    _gcvt.argtypes = [c_double, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        _gcvt.restype = ReturnString
    else:
        _gcvt.restype = String
        _gcvt.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 618
for _lib in _libs.values():
    if not _lib.has("_atodbl", "cdecl"):
        continue
    _atodbl = _lib.get("_atodbl", "cdecl")
    _atodbl.argtypes = [POINTER(_CRT_DOUBLE), String]
    _atodbl.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 619
for _lib in _libs.values():
    if not _lib.has("_atoldbl", "cdecl"):
        continue
    _atoldbl = _lib.get("_atoldbl", "cdecl")
    _atoldbl.argtypes = [POINTER(_LDOUBLE), String]
    _atoldbl.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 620
for _lib in _libs.values():
    if not _lib.has("_atoflt", "cdecl"):
        continue
    _atoflt = _lib.get("_atoflt", "cdecl")
    _atoflt.argtypes = [POINTER(_CRT_FLOAT), String]
    _atoflt.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 621
for _lib in _libs.values():
    if not _lib.has("_atodbl_l", "cdecl"):
        continue
    _atodbl_l = _lib.get("_atodbl_l", "cdecl")
    _atodbl_l.argtypes = [POINTER(_CRT_DOUBLE), String, _locale_t]
    _atodbl_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 622
for _lib in _libs.values():
    if not _lib.has("_atoldbl_l", "cdecl"):
        continue
    _atoldbl_l = _lib.get("_atoldbl_l", "cdecl")
    _atoldbl_l.argtypes = [POINTER(_LDOUBLE), String, _locale_t]
    _atoldbl_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 623
for _lib in _libs.values():
    if not _lib.has("_atoflt_l", "cdecl"):
        continue
    _atoflt_l = _lib.get("_atoflt_l", "cdecl")
    _atoflt_l.argtypes = [POINTER(_CRT_FLOAT), String, _locale_t]
    _atoflt_l.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 646
for _lib in _libs.values():
    if not _lib.has("_makepath", "cdecl"):
        continue
    _makepath = _lib.get("_makepath", "cdecl")
    _makepath.argtypes = [String, String, String, String, String]
    _makepath.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 647
for _lib in _libs.values():
    if not _lib.has("_onexit", "cdecl"):
        continue
    _onexit = _lib.get("_onexit", "cdecl")
    _onexit.argtypes = [_onexit_t]
    _onexit.restype = _onexit_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 651
for _lib in _libs.values():
    if not _lib.has("perror", "cdecl"):
        continue
    perror = _lib.get("perror", "cdecl")
    perror.argtypes = [String]
    perror.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 670
for _lib in _libs.values():
    if not _lib.has("_searchenv", "cdecl"):
        continue
    _searchenv = _lib.get("_searchenv", "cdecl")
    _searchenv.argtypes = [String, String, String]
    _searchenv.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 671
for _lib in _libs.values():
    if not _lib.has("_splitpath", "cdecl"):
        continue
    _splitpath = _lib.get("_splitpath", "cdecl")
    _splitpath.argtypes = [String, String, String, String, String]
    _splitpath.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 672
for _lib in _libs.values():
    if not _lib.has("_swab", "cdecl"):
        continue
    _swab = _lib.get("_swab", "cdecl")
    _swab.argtypes = [String, String, c_int]
    _swab.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 676
for _lib in _libs.values():
    if not _lib.has("_wfullpath", "cdecl"):
        continue
    _wfullpath = _lib.get("_wfullpath", "cdecl")
    _wfullpath.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    _wfullpath.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/stdlib.h: 677
for _lib in _libs.values():
    if not _lib.has("_wmakepath", "cdecl"):
        continue
    _wmakepath = _lib.get("_wmakepath", "cdecl")
    _wmakepath.argtypes = [POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar)]
    _wmakepath.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 680
for _lib in _libs.values():
    if not _lib.has("_wperror", "cdecl"):
        continue
    _wperror = _lib.get("_wperror", "cdecl")
    _wperror.argtypes = [POINTER(c_wchar)]
    _wperror.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 682
for _lib in _libs.values():
    if not _lib.has("_wsearchenv", "cdecl"):
        continue
    _wsearchenv = _lib.get("_wsearchenv", "cdecl")
    _wsearchenv.argtypes = [POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar)]
    _wsearchenv.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 683
for _lib in _libs.values():
    if not _lib.has("_wsplitpath", "cdecl"):
        continue
    _wsplitpath = _lib.get("_wsplitpath", "cdecl")
    _wsplitpath.argtypes = [POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar), POINTER(c_wchar)]
    _wsplitpath.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 686
for _lib in _libs.values():
    if not _lib.has("_beep", "cdecl"):
        continue
    _beep = _lib.get("_beep", "cdecl")
    _beep.argtypes = [c_uint, c_uint]
    _beep.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 688
for _lib in _libs.values():
    if not _lib.has("_seterrormode", "cdecl"):
        continue
    _seterrormode = _lib.get("_seterrormode", "cdecl")
    _seterrormode.argtypes = [c_int]
    _seterrormode.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 689
for _lib in _libs.values():
    if not _lib.has("_sleep", "cdecl"):
        continue
    _sleep = _lib.get("_sleep", "cdecl")
    _sleep.argtypes = [c_ulong]
    _sleep.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 710
for _lib in _libs.values():
    if not _lib.has("ecvt", "cdecl"):
        continue
    ecvt = _lib.get("ecvt", "cdecl")
    ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecvt.restype = ReturnString
    else:
        ecvt.restype = String
        ecvt.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 711
for _lib in _libs.values():
    if not _lib.has("fcvt", "cdecl"):
        continue
    fcvt = _lib.get("fcvt", "cdecl")
    fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        fcvt.restype = ReturnString
    else:
        fcvt.restype = String
        fcvt.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 712
for _lib in _libs.values():
    if not _lib.has("gcvt", "cdecl"):
        continue
    gcvt = _lib.get("gcvt", "cdecl")
    gcvt.argtypes = [c_double, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        gcvt.restype = ReturnString
    else:
        gcvt.restype = String
        gcvt.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 713
for _lib in _libs.values():
    if not _lib.has("itoa", "cdecl"):
        continue
    itoa = _lib.get("itoa", "cdecl")
    itoa.argtypes = [c_int, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        itoa.restype = ReturnString
    else:
        itoa.restype = String
        itoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 714
for _lib in _libs.values():
    if not _lib.has("ltoa", "cdecl"):
        continue
    ltoa = _lib.get("ltoa", "cdecl")
    ltoa.argtypes = [c_long, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ltoa.restype = ReturnString
    else:
        ltoa.restype = String
        ltoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 715
for _lib in _libs.values():
    if not _lib.has("putenv", "cdecl"):
        continue
    putenv = _lib.get("putenv", "cdecl")
    putenv.argtypes = [String]
    putenv.restype = c_int
    break

# C:/msys64/ucrt64/include/stdlib.h: 719
for _lib in _libs.values():
    if not _lib.has("swab", "cdecl"):
        continue
    swab = _lib.get("swab", "cdecl")
    swab.argtypes = [String, String, c_int]
    swab.restype = None
    break

# C:/msys64/ucrt64/include/stdlib.h: 722
for _lib in _libs.values():
    if not _lib.has("ultoa", "cdecl"):
        continue
    ultoa = _lib.get("ultoa", "cdecl")
    ultoa.argtypes = [c_ulong, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ultoa.restype = ReturnString
    else:
        ultoa.restype = String
        ultoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 723
for _lib in _libs.values():
    if not _lib.has("onexit", "cdecl"):
        continue
    onexit = _lib.get("onexit", "cdecl")
    onexit.argtypes = [_onexit_t]
    onexit.restype = _onexit_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 729
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'quot',
    'rem',
]
struct_anon_6._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]

lldiv_t = struct_anon_6# C:/msys64/ucrt64/include/stdlib.h: 729

# C:/msys64/ucrt64/include/stdlib.h: 731
for _lib in _libs.values():
    if not _lib.has("lldiv", "cdecl"):
        continue
    lldiv = _lib.get("lldiv", "cdecl")
    lldiv.argtypes = [c_longlong, c_longlong]
    lldiv.restype = lldiv_t
    break

# C:/msys64/ucrt64/include/stdlib.h: 733
for _lib in _libs.values():
    if not _lib.has("llabs", "cdecl"):
        continue
    llabs = _lib.get("llabs", "cdecl")
    llabs.argtypes = [c_longlong]
    llabs.restype = c_longlong
    break

# C:/msys64/ucrt64/include/stdlib.h: 738
for _lib in _libs.values():
    if not _lib.has("strtoll", "cdecl"):
        continue
    strtoll = _lib.get("strtoll", "cdecl")
    strtoll.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoll.restype = c_longlong
    break

# C:/msys64/ucrt64/include/stdlib.h: 739
for _lib in _libs.values():
    if not _lib.has("strtoull", "cdecl"):
        continue
    strtoull = _lib.get("strtoull", "cdecl")
    strtoull.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoull.restype = c_ulonglong
    break

# C:/msys64/ucrt64/include/stdlib.h: 742
for _lib in _libs.values():
    if not _lib.has("atoll", "cdecl"):
        continue
    atoll = _lib.get("atoll", "cdecl")
    atoll.argtypes = [String]
    atoll.restype = c_longlong
    break

# C:/msys64/ucrt64/include/stdlib.h: 745
for _lib in _libs.values():
    if not _lib.has("wtoll", "cdecl"):
        continue
    wtoll = _lib.get("wtoll", "cdecl")
    wtoll.argtypes = [POINTER(c_wchar)]
    wtoll.restype = c_longlong
    break

# C:/msys64/ucrt64/include/stdlib.h: 746
for _lib in _libs.values():
    if not _lib.has("lltoa", "cdecl"):
        continue
    lltoa = _lib.get("lltoa", "cdecl")
    lltoa.argtypes = [c_longlong, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        lltoa.restype = ReturnString
    else:
        lltoa.restype = String
        lltoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 747
for _lib in _libs.values():
    if not _lib.has("ulltoa", "cdecl"):
        continue
    ulltoa = _lib.get("ulltoa", "cdecl")
    ulltoa.argtypes = [c_ulonglong, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ulltoa.restype = ReturnString
    else:
        ulltoa.restype = String
        ulltoa.errcheck = ReturnString
    break

# C:/msys64/ucrt64/include/stdlib.h: 748
for _lib in _libs.values():
    if not _lib.has("lltow", "cdecl"):
        continue
    lltow = _lib.get("lltow", "cdecl")
    lltow.argtypes = [c_longlong, POINTER(c_wchar), c_int]
    lltow.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/stdlib.h: 749
for _lib in _libs.values():
    if not _lib.has("ulltow", "cdecl"):
        continue
    ulltow = _lib.get("ulltow", "cdecl")
    ulltow.argtypes = [c_ulonglong, POINTER(c_wchar), c_int]
    ulltow.restype = POINTER(c_wchar)
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 15
for _lib in _libs.values():
    if not _lib.has("bsearch_s", "cdecl"):
        continue
    bsearch_s = _lib.get("bsearch_s", "cdecl")
    bsearch_s.argtypes = [POINTER(None), POINTER(None), rsize_t, rsize_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), POINTER(None)), POINTER(None)]
    bsearch_s.restype = POINTER(c_ubyte)
    bsearch_s.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 16
for _lib in _libs.values():
    if not _lib.has("_dupenv_s", "cdecl"):
        continue
    _dupenv_s = _lib.get("_dupenv_s", "cdecl")
    _dupenv_s.argtypes = [POINTER(POINTER(c_char)), POINTER(c_size_t), String]
    _dupenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 17
for _lib in _libs.values():
    if not _lib.has("getenv_s", "cdecl"):
        continue
    getenv_s = _lib.get("getenv_s", "cdecl")
    getenv_s.argtypes = [POINTER(c_size_t), String, rsize_t, String]
    getenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 19
for _lib in _libs.values():
    if not _lib.has("_itoa_s", "cdecl"):
        continue
    _itoa_s = _lib.get("_itoa_s", "cdecl")
    _itoa_s.argtypes = [c_int, String, c_size_t, c_int]
    _itoa_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 21
for _lib in _libs.values():
    if not _lib.has("_i64toa_s", "cdecl"):
        continue
    _i64toa_s = _lib.get("_i64toa_s", "cdecl")
    _i64toa_s.argtypes = [c_int64, String, c_size_t, c_int]
    _i64toa_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 23
for _lib in _libs.values():
    if not _lib.has("_ltoa_s", "cdecl"):
        continue
    _ltoa_s = _lib.get("_ltoa_s", "cdecl")
    _ltoa_s.argtypes = [c_long, String, c_size_t, c_int]
    _ltoa_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 25
for _lib in _libs.values():
    if not _lib.has("mbstowcs_s", "cdecl"):
        continue
    mbstowcs_s = _lib.get("mbstowcs_s", "cdecl")
    mbstowcs_s.argtypes = [POINTER(c_size_t), POINTER(c_wchar), c_size_t, String, c_size_t]
    mbstowcs_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 27
for _lib in _libs.values():
    if not _lib.has("_mbstowcs_s_l", "cdecl"):
        continue
    _mbstowcs_s_l = _lib.get("_mbstowcs_s_l", "cdecl")
    _mbstowcs_s_l.argtypes = [POINTER(c_size_t), POINTER(c_wchar), c_size_t, String, c_size_t, _locale_t]
    _mbstowcs_s_l.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 29
for _lib in _libs.values():
    if not _lib.has("_ultoa_s", "cdecl"):
        continue
    _ultoa_s = _lib.get("_ultoa_s", "cdecl")
    _ultoa_s.argtypes = [c_ulong, String, c_size_t, c_int]
    _ultoa_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 31
for _lib in _libs.values():
    if not _lib.has("wctomb_s", "cdecl"):
        continue
    wctomb_s = _lib.get("wctomb_s", "cdecl")
    wctomb_s.argtypes = [POINTER(c_int), String, rsize_t, c_wchar]
    wctomb_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 32
for _lib in _libs.values():
    if not _lib.has("_wctomb_s_l", "cdecl"):
        continue
    _wctomb_s_l = _lib.get("_wctomb_s_l", "cdecl")
    _wctomb_s_l.argtypes = [POINTER(c_int), String, c_size_t, c_wchar, _locale_t]
    _wctomb_s_l.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 33
for _lib in _libs.values():
    if not _lib.has("wcstombs_s", "cdecl"):
        continue
    wcstombs_s = _lib.get("wcstombs_s", "cdecl")
    wcstombs_s.argtypes = [POINTER(c_size_t), String, c_size_t, POINTER(c_wchar), c_size_t]
    wcstombs_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 35
for _lib in _libs.values():
    if not _lib.has("_wcstombs_s_l", "cdecl"):
        continue
    _wcstombs_s_l = _lib.get("_wcstombs_s_l", "cdecl")
    _wcstombs_s_l.argtypes = [POINTER(c_size_t), String, c_size_t, POINTER(c_wchar), c_size_t, _locale_t]
    _wcstombs_s_l.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 39
for _lib in _libs.values():
    if not _lib.has("_ecvt_s", "cdecl"):
        continue
    _ecvt_s = _lib.get("_ecvt_s", "cdecl")
    _ecvt_s.argtypes = [String, c_size_t, c_double, c_int, POINTER(c_int), POINTER(c_int)]
    _ecvt_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 40
for _lib in _libs.values():
    if not _lib.has("_fcvt_s", "cdecl"):
        continue
    _fcvt_s = _lib.get("_fcvt_s", "cdecl")
    _fcvt_s.argtypes = [String, c_size_t, c_double, c_int, POINTER(c_int), POINTER(c_int)]
    _fcvt_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 41
for _lib in _libs.values():
    if not _lib.has("_gcvt_s", "cdecl"):
        continue
    _gcvt_s = _lib.get("_gcvt_s", "cdecl")
    _gcvt_s.argtypes = [String, c_size_t, c_double, c_int]
    _gcvt_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 42
for _lib in _libs.values():
    if not _lib.has("_makepath_s", "cdecl"):
        continue
    _makepath_s = _lib.get("_makepath_s", "cdecl")
    _makepath_s.argtypes = [String, c_size_t, String, String, String, String]
    _makepath_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 44
for _lib in _libs.values():
    if not _lib.has("_putenv_s", "cdecl"):
        continue
    _putenv_s = _lib.get("_putenv_s", "cdecl")
    _putenv_s.argtypes = [String, String]
    _putenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 45
for _lib in _libs.values():
    if not _lib.has("_searchenv_s", "cdecl"):
        continue
    _searchenv_s = _lib.get("_searchenv_s", "cdecl")
    _searchenv_s.argtypes = [String, String, String, c_size_t]
    _searchenv_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 47
for _lib in _libs.values():
    if not _lib.has("_splitpath_s", "cdecl"):
        continue
    _splitpath_s = _lib.get("_splitpath_s", "cdecl")
    _splitpath_s.argtypes = [String, String, c_size_t, String, c_size_t, String, c_size_t, String, c_size_t]
    _splitpath_s.restype = errno_t
    break

# C:/msys64/ucrt64/include/sec_api/stdlib_s.h: 52
for _lib in _libs.values():
    if not _lib.has("qsort_s", "cdecl"):
        continue
    qsort_s = _lib.get("qsort_s", "cdecl")
    qsort_s.argtypes = [POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), POINTER(None)), POINTER(None)]
    qsort_s.restype = None
    break

# C:/msys64/ucrt64/include/malloc.h: 50
class struct__heapinfo(Structure):
    pass

struct__heapinfo.__slots__ = [
    '_pentry',
    '_size',
    '_useflag',
]
struct__heapinfo._fields_ = [
    ('_pentry', POINTER(c_int)),
    ('_size', c_size_t),
    ('_useflag', c_int),
]

_HEAPINFO = struct__heapinfo# C:/msys64/ucrt64/include/malloc.h: 50

# C:/msys64/ucrt64/include/malloc.h: 53
for _lib in _libs.values():
    try:
        _amblksiz = (c_uint).in_dll(_lib, "_amblksiz")
        break
    except:
        pass

# C:/msys64/ucrt64/include/malloc.h: 77
for _lib in _libs.values():
    if not _lib.has("__mingw_aligned_malloc", "cdecl"):
        continue
    __mingw_aligned_malloc = _lib.get("__mingw_aligned_malloc", "cdecl")
    __mingw_aligned_malloc.argtypes = [c_size_t, c_size_t]
    __mingw_aligned_malloc.restype = POINTER(c_ubyte)
    __mingw_aligned_malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/malloc.h: 78
for _lib in _libs.values():
    if not _lib.has("__mingw_aligned_free", "cdecl"):
        continue
    __mingw_aligned_free = _lib.get("__mingw_aligned_free", "cdecl")
    __mingw_aligned_free.argtypes = [POINTER(None)]
    __mingw_aligned_free.restype = None
    break

# C:/msys64/ucrt64/include/malloc.h: 79
for _lib in _libs.values():
    if not _lib.has("__mingw_aligned_offset_realloc", "cdecl"):
        continue
    __mingw_aligned_offset_realloc = _lib.get("__mingw_aligned_offset_realloc", "cdecl")
    __mingw_aligned_offset_realloc.argtypes = [POINTER(None), c_size_t, c_size_t, c_size_t]
    __mingw_aligned_offset_realloc.restype = POINTER(c_ubyte)
    __mingw_aligned_offset_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/malloc.h: 80
for _lib in _libs.values():
    if not _lib.has("__mingw_aligned_realloc", "cdecl"):
        continue
    __mingw_aligned_realloc = _lib.get("__mingw_aligned_realloc", "cdecl")
    __mingw_aligned_realloc.argtypes = [POINTER(None), c_size_t, c_size_t]
    __mingw_aligned_realloc.restype = POINTER(c_ubyte)
    __mingw_aligned_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/mm_malloc.h: 35
for _lib in _libs.values():
    try:
        __malloc_ptr = (POINTER(None)).in_dll(_lib, "__malloc_ptr")
        break
    except:
        pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/mm_malloc.h: 36
for _lib in _libs.values():
    try:
        __aligned_ptr = (POINTER(None)).in_dll(_lib, "__aligned_ptr")
        break
    except:
        pass

# C:/msys64/ucrt64/include/malloc.h: 90
for _lib in _libs.values():
    if not _lib.has("_resetstkoflw", "cdecl"):
        continue
    _resetstkoflw = _lib.get("_resetstkoflw", "cdecl")
    _resetstkoflw.argtypes = []
    _resetstkoflw.restype = c_int
    break

# C:/msys64/ucrt64/include/malloc.h: 92
for _lib in _libs.values():
    if not _lib.has("_set_malloc_crt_max_wait", "cdecl"):
        continue
    _set_malloc_crt_max_wait = _lib.get("_set_malloc_crt_max_wait", "cdecl")
    _set_malloc_crt_max_wait.argtypes = [c_ulong]
    _set_malloc_crt_max_wait.restype = c_ulong
    break

# C:/msys64/ucrt64/include/malloc.h: 94
for _lib in _libs.values():
    if not _lib.has("_expand", "cdecl"):
        continue
    _expand = _lib.get("_expand", "cdecl")
    _expand.argtypes = [POINTER(None), c_size_t]
    _expand.restype = POINTER(c_ubyte)
    _expand.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/malloc.h: 95
for _lib in _libs.values():
    if not _lib.has("_msize", "cdecl"):
        continue
    _msize = _lib.get("_msize", "cdecl")
    _msize.argtypes = [POINTER(None)]
    _msize.restype = c_size_t
    break

# C:/msys64/ucrt64/include/malloc.h: 100
for _lib in _libs.values():
    if not _lib.has("_alloca", "cdecl"):
        continue
    _alloca = _lib.get("_alloca", "cdecl")
    _alloca.argtypes = [c_size_t]
    _alloca.restype = POINTER(c_ubyte)
    _alloca.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/ucrt64/include/malloc.h: 102
for _lib in _libs.values():
    if not _lib.has("_get_sbh_threshold", "cdecl"):
        continue
    _get_sbh_threshold = _lib.get("_get_sbh_threshold", "cdecl")
    _get_sbh_threshold.argtypes = []
    _get_sbh_threshold.restype = c_size_t
    break

# C:/msys64/ucrt64/include/malloc.h: 103
for _lib in _libs.values():
    if not _lib.has("_set_sbh_threshold", "cdecl"):
        continue
    _set_sbh_threshold = _lib.get("_set_sbh_threshold", "cdecl")
    _set_sbh_threshold.argtypes = [c_size_t]
    _set_sbh_threshold.restype = c_int
    break

# C:/msys64/ucrt64/include/malloc.h: 104
for _lib in _libs.values():
    if not _lib.has("_set_amblksiz", "cdecl"):
        continue
    _set_amblksiz = _lib.get("_set_amblksiz", "cdecl")
    _set_amblksiz.argtypes = [c_size_t]
    _set_amblksiz.restype = errno_t
    break

# C:/msys64/ucrt64/include/malloc.h: 105
for _lib in _libs.values():
    if not _lib.has("_get_amblksiz", "cdecl"):
        continue
    _get_amblksiz = _lib.get("_get_amblksiz", "cdecl")
    _get_amblksiz.argtypes = [POINTER(c_size_t)]
    _get_amblksiz.restype = errno_t
    break

# C:/msys64/ucrt64/include/malloc.h: 106
for _lib in _libs.values():
    if not _lib.has("_heapadd", "cdecl"):
        continue
    _heapadd = _lib.get("_heapadd", "cdecl")
    _heapadd.argtypes = [POINTER(None), c_size_t]
    _heapadd.restype = c_int
    break

# C:/msys64/ucrt64/include/malloc.h: 107
for _lib in _libs.values():
    if not _lib.has("_heapchk", "cdecl"):
        continue
    _heapchk = _lib.get("_heapchk", "cdecl")
    _heapchk.argtypes = []
    _heapchk.restype = c_int
    break

# C:/msys64/ucrt64/include/malloc.h: 108
for _lib in _libs.values():
    if not _lib.has("_heapmin", "cdecl"):
        continue
    _heapmin = _lib.get("_heapmin", "cdecl")
    _heapmin.argtypes = []
    _heapmin.restype = c_int
    break

# C:/msys64/ucrt64/include/malloc.h: 109
for _lib in _libs.values():
    if not _lib.has("_heapset", "cdecl"):
        continue
    _heapset = _lib.get("_heapset", "cdecl")
    _heapset.argtypes = [c_uint]
    _heapset.restype = c_int
    break

# C:/msys64/ucrt64/include/malloc.h: 110
for _lib in _libs.values():
    if not _lib.has("_heapwalk", "cdecl"):
        continue
    _heapwalk = _lib.get("_heapwalk", "cdecl")
    _heapwalk.argtypes = [POINTER(_HEAPINFO)]
    _heapwalk.restype = c_int
    break

# C:/msys64/ucrt64/include/malloc.h: 111
for _lib in _libs.values():
    if not _lib.has("_heapused", "cdecl"):
        continue
    _heapused = _lib.get("_heapused", "cdecl")
    _heapused.argtypes = [POINTER(c_size_t), POINTER(c_size_t)]
    _heapused.restype = c_size_t
    break

# C:/msys64/ucrt64/include/malloc.h: 112
for _lib in _libs.values():
    if not _lib.has("_get_heap_handle", "cdecl"):
        continue
    _get_heap_handle = _lib.get("_get_heap_handle", "cdecl")
    _get_heap_handle.argtypes = []
    _get_heap_handle.restype = intptr_t
    break

# C:/msys64/ucrt64/include/malloc.h: 145
for _lib in _libs.values():
    try:
        _Marker = (c_uint).in_dll(_lib, "_Marker")
        break
    except:
        pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 242
for _lib in _libs.values():
    if not _lib.has("OmStartup", "cdecl"):
        continue
    OmStartup = _lib.get("OmStartup", "cdecl")
    OmStartup.argtypes = [c_int]
    OmStartup.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 253
for _lib in _libs.values():
    if not _lib.has("OmShutdown", "cdecl"):
        continue
    OmShutdown = _lib.get("OmShutdown", "cdecl")
    OmShutdown.argtypes = []
    OmShutdown.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 263
for _lib in _libs.values():
    if not _lib.has("OmSetLogStream", "cdecl"):
        continue
    OmSetLogStream = _lib.get("OmSetLogStream", "cdecl")
    OmSetLogStream.argtypes = [c_int]
    OmSetLogStream.restype = c_int
    break

OmLogCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 273

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 283
for _lib in _libs.values():
    if not _lib.has("OmSetLogCallback", "cdecl"):
        continue
    OmSetLogCallback = _lib.get("OmSetLogCallback", "cdecl")
    OmSetLogCallback.argtypes = [OmLogCallback, POINTER(None)]
    OmSetLogCallback.restype = c_int
    break

enum_anon_7 = c_int# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 294

OM_DEVICE_REMOVED = 0# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 294

OM_DEVICE_CONNECTED = (OM_DEVICE_REMOVED + 1)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 294

OM_DEVICE_STATUS = enum_anon_7# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 294

OmDeviceCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, OM_DEVICE_STATUS)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 303

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 313
for _lib in _libs.values():
    if not _lib.has("OmSetDeviceCallback", "cdecl"):
        continue
    OmSetDeviceCallback = _lib.get("OmSetDeviceCallback", "cdecl")
    OmSetDeviceCallback.argtypes = [OmDeviceCallback, POINTER(None)]
    OmSetDeviceCallback.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 325
for _lib in _libs.values():
    if not _lib.has("OmGetDeviceIds", "cdecl"):
        continue
    OmGetDeviceIds = _lib.get("OmGetDeviceIds", "cdecl")
    OmGetDeviceIds.argtypes = [POINTER(c_int), c_int]
    OmGetDeviceIds.restype = c_int
    break

OM_DATETIME = c_ulong# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 335

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 370
for _lib in _libs.values():
    if not _lib.has("OmGetVersion", "cdecl"):
        continue
    OmGetVersion = _lib.get("OmGetVersion", "cdecl")
    OmGetVersion.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    OmGetVersion.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 379
for _lib in _libs.values():
    if not _lib.has("OmGetDeviceSerial", "cdecl"):
        continue
    OmGetDeviceSerial = _lib.get("OmGetDeviceSerial", "cdecl")
    OmGetDeviceSerial.argtypes = [c_int, String]
    OmGetDeviceSerial.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 389
for _lib in _libs.values():
    if not _lib.has("OmGetDevicePort", "cdecl"):
        continue
    OmGetDevicePort = _lib.get("OmGetDevicePort", "cdecl")
    OmGetDevicePort.argtypes = [c_int, String]
    OmGetDevicePort.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 399
for _lib in _libs.values():
    if not _lib.has("OmGetDevicePath", "cdecl"):
        continue
    OmGetDevicePath = _lib.get("OmGetDevicePath", "cdecl")
    OmGetDevicePath.argtypes = [c_int, String]
    OmGetDevicePath.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 408
for _lib in _libs.values():
    if not _lib.has("OmGetBatteryLevel", "cdecl"):
        continue
    OmGetBatteryLevel = _lib.get("OmGetBatteryLevel", "cdecl")
    OmGetBatteryLevel.argtypes = [c_int]
    OmGetBatteryLevel.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 419
for _lib in _libs.values():
    if not _lib.has("OmSelfTest", "cdecl"):
        continue
    OmSelfTest = _lib.get("OmSelfTest", "cdecl")
    OmSelfTest.argtypes = [c_int]
    OmSelfTest.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 432
for _lib in _libs.values():
    if not _lib.has("OmGetMemoryHealth", "cdecl"):
        continue
    OmGetMemoryHealth = _lib.get("OmGetMemoryHealth", "cdecl")
    OmGetMemoryHealth.argtypes = [c_int]
    OmGetMemoryHealth.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 446
for _lib in _libs.values():
    if not _lib.has("OmGetBatteryHealth", "cdecl"):
        continue
    OmGetBatteryHealth = _lib.get("OmGetBatteryHealth", "cdecl")
    OmGetBatteryHealth.argtypes = [c_int]
    OmGetBatteryHealth.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 458
for _lib in _libs.values():
    if not _lib.has("OmGetAccelerometer", "cdecl"):
        continue
    OmGetAccelerometer = _lib.get("OmGetAccelerometer", "cdecl")
    OmGetAccelerometer.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    OmGetAccelerometer.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 467
for _lib in _libs.values():
    if not _lib.has("OmGetTime", "cdecl"):
        continue
    OmGetTime = _lib.get("OmGetTime", "cdecl")
    OmGetTime.argtypes = [c_int, POINTER(OM_DATETIME)]
    OmGetTime.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 476
for _lib in _libs.values():
    if not _lib.has("OmSetTime", "cdecl"):
        continue
    OmSetTime = _lib.get("OmSetTime", "cdecl")
    OmSetTime.argtypes = [c_int, OM_DATETIME]
    OmSetTime.restype = c_int
    break

enum_anon_8 = c_int# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_AUTO = (-1)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_OFF = 0# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_BLUE = 1# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_GREEN = 2# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_CYAN = 3# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_RED = 4# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_MAGENTA = 5# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_YELLOW = 6# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_WHITE = 7# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

OM_LED_STATE = enum_anon_8# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 498

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 508
for _lib in _libs.values():
    if not _lib.has("OmSetLed", "cdecl"):
        continue
    OmSetLed = _lib.get("OmSetLed", "cdecl")
    OmSetLed.argtypes = [c_int, OM_LED_STATE]
    OmSetLed.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 518
for _lib in _libs.values():
    if not _lib.has("OmIsLocked", "cdecl"):
        continue
    OmIsLocked = _lib.get("OmIsLocked", "cdecl")
    OmIsLocked.argtypes = [c_int, POINTER(c_int)]
    OmIsLocked.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 529
for _lib in _libs.values():
    if not _lib.has("OmSetLock", "cdecl"):
        continue
    OmSetLock = _lib.get("OmSetLock", "cdecl")
    OmSetLock.argtypes = [c_int, c_ushort]
    OmSetLock.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 540
for _lib in _libs.values():
    if not _lib.has("OmUnlock", "cdecl"):
        continue
    OmUnlock = _lib.get("OmUnlock", "cdecl")
    OmUnlock.argtypes = [c_int, c_ushort]
    OmUnlock.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 550
for _lib in _libs.values():
    if not _lib.has("OmSetEcc", "cdecl"):
        continue
    OmSetEcc = _lib.get("OmSetEcc", "cdecl")
    OmSetEcc.argtypes = [c_int, c_int]
    OmSetEcc.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 559
for _lib in _libs.values():
    if not _lib.has("OmGetEcc", "cdecl"):
        continue
    OmGetEcc = _lib.get("OmGetEcc", "cdecl")
    OmGetEcc.argtypes = [c_int]
    OmGetEcc.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 578
for _lib in _libs.values():
    if not _lib.has("OmCommand", "cdecl"):
        continue
    OmCommand = _lib.get("OmCommand", "cdecl")
    OmCommand.argtypes = [c_int, String, String, c_size_t, String, c_uint, POINTER(POINTER(c_char)), c_int]
    OmCommand.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 611
for _lib in _libs.values():
    if not _lib.has("OmGetDelays", "cdecl"):
        continue
    OmGetDelays = _lib.get("OmGetDelays", "cdecl")
    OmGetDelays.argtypes = [c_int, POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmGetDelays.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 629
for _lib in _libs.values():
    if not _lib.has("OmSetDelays", "cdecl"):
        continue
    OmSetDelays = _lib.get("OmSetDelays", "cdecl")
    OmSetDelays.argtypes = [c_int, OM_DATETIME, OM_DATETIME]
    OmSetDelays.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 638
for _lib in _libs.values():
    if not _lib.has("OmGetSessionId", "cdecl"):
        continue
    OmGetSessionId = _lib.get("OmGetSessionId", "cdecl")
    OmGetSessionId.argtypes = [c_int, POINTER(c_uint)]
    OmGetSessionId.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 649
for _lib in _libs.values():
    if not _lib.has("OmSetSessionId", "cdecl"):
        continue
    OmSetSessionId = _lib.get("OmSetSessionId", "cdecl")
    OmSetSessionId.argtypes = [c_int, c_uint]
    OmSetSessionId.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 666
for _lib in _libs.values():
    if not _lib.has("OmGetMetadata", "cdecl"):
        continue
    OmGetMetadata = _lib.get("OmGetMetadata", "cdecl")
    OmGetMetadata.argtypes = [c_int, String]
    OmGetMetadata.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 679
for _lib in _libs.values():
    if not _lib.has("OmSetMetadata", "cdecl"):
        continue
    OmSetMetadata = _lib.get("OmSetMetadata", "cdecl")
    OmSetMetadata.argtypes = [c_int, String, c_int]
    OmSetMetadata.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 688
for _lib in _libs.values():
    if not _lib.has("OmGetLastConfigTime", "cdecl"):
        continue
    OmGetLastConfigTime = _lib.get("OmGetLastConfigTime", "cdecl")
    OmGetLastConfigTime.argtypes = [c_int, POINTER(OM_DATETIME)]
    OmGetLastConfigTime.restype = c_int
    break

enum_anon_9 = c_int# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 702

OM_ERASE_NONE = 0# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 702

OM_ERASE_DELETE = 1# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 702

OM_ERASE_QUICKFORMAT = 2# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 702

OM_ERASE_WIPE = 3# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 702

OM_ERASE_LEVEL = enum_anon_9# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 702

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 723
for _lib in _libs.values():
    if not _lib.has("OmEraseDataAndCommit", "cdecl"):
        continue
    OmEraseDataAndCommit = _lib.get("OmEraseDataAndCommit", "cdecl")
    OmEraseDataAndCommit.argtypes = [c_int, OM_ERASE_LEVEL]
    OmEraseDataAndCommit.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 776
for _lib in _libs.values():
    if not _lib.has("OmGetAccelConfig", "cdecl"):
        continue
    OmGetAccelConfig = _lib.get("OmGetAccelConfig", "cdecl")
    OmGetAccelConfig.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    OmGetAccelConfig.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 789
for _lib in _libs.values():
    if not _lib.has("OmSetAccelConfig", "cdecl"):
        continue
    OmSetAccelConfig = _lib.get("OmSetAccelConfig", "cdecl")
    OmSetAccelConfig.argtypes = [c_int, c_int, c_int]
    OmSetAccelConfig.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 800
for _lib in _libs.values():
    if not _lib.has("OmGetMaxSamples", "cdecl"):
        continue
    OmGetMaxSamples = _lib.get("OmGetMaxSamples", "cdecl")
    OmGetMaxSamples.argtypes = [c_int, POINTER(c_int)]
    OmGetMaxSamples.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 812
for _lib in _libs.values():
    if not _lib.has("OmSetMaxSamples", "cdecl"):
        continue
    OmSetMaxSamples = _lib.get("OmSetMaxSamples", "cdecl")
    OmSetMaxSamples.argtypes = [c_int, c_int]
    OmSetMaxSamples.restype = c_int
    break

enum_anon_10 = c_int# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 857

OM_DOWNLOAD_NONE = 0# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 857

OM_DOWNLOAD_ERROR = (OM_DOWNLOAD_NONE + 1)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 857

OM_DOWNLOAD_PROGRESS = (OM_DOWNLOAD_ERROR + 1)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 857

OM_DOWNLOAD_COMPLETE = (OM_DOWNLOAD_PROGRESS + 1)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 857

OM_DOWNLOAD_CANCELLED = (OM_DOWNLOAD_COMPLETE + 1)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 857

OM_DOWNLOAD_STATUS = enum_anon_10# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 857

OmDownloadCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, OM_DOWNLOAD_STATUS, c_int)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 866

OmDownloadChunkCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, POINTER(None), c_int, c_int)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 876

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 885
for _lib in _libs.values():
    if not _lib.has("OmSetDownloadCallback", "cdecl"):
        continue
    OmSetDownloadCallback = _lib.get("OmSetDownloadCallback", "cdecl")
    OmSetDownloadCallback.argtypes = [OmDownloadCallback, POINTER(None)]
    OmSetDownloadCallback.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 895
for _lib in _libs.values():
    if not _lib.has("OmSetDownloadChunkCallback", "cdecl"):
        continue
    OmSetDownloadChunkCallback = _lib.get("OmSetDownloadChunkCallback", "cdecl")
    OmSetDownloadChunkCallback.argtypes = [OmDownloadChunkCallback, POINTER(None)]
    OmSetDownloadChunkCallback.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 904
for _lib in _libs.values():
    if not _lib.has("OmGetDataFileSize", "cdecl"):
        continue
    OmGetDataFileSize = _lib.get("OmGetDataFileSize", "cdecl")
    OmGetDataFileSize.argtypes = [c_int]
    OmGetDataFileSize.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 914
for _lib in _libs.values():
    if not _lib.has("OmGetDataFilename", "cdecl"):
        continue
    OmGetDataFilename = _lib.get("OmGetDataFilename", "cdecl")
    OmGetDataFilename.argtypes = [c_int, String]
    OmGetDataFilename.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 927
for _lib in _libs.values():
    if not _lib.has("OmGetDataRange", "cdecl"):
        continue
    OmGetDataRange = _lib.get("OmGetDataRange", "cdecl")
    OmGetDataRange.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmGetDataRange.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 943
for _lib in _libs.values():
    if not _lib.has("OmBeginDownloading", "cdecl"):
        continue
    OmBeginDownloading = _lib.get("OmBeginDownloading", "cdecl")
    OmBeginDownloading.argtypes = [c_int, c_int, c_int, String]
    OmBeginDownloading.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 961
for _lib in _libs.values():
    if not _lib.has("OmBeginDownloadingReference", "cdecl"):
        continue
    OmBeginDownloadingReference = _lib.get("OmBeginDownloadingReference", "cdecl")
    OmBeginDownloadingReference.argtypes = [c_int, c_int, c_int, String, POINTER(None)]
    OmBeginDownloadingReference.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 976
for _lib in _libs.values():
    if not _lib.has("OmQueryDownload", "cdecl"):
        continue
    OmQueryDownload = _lib.get("OmQueryDownload", "cdecl")
    OmQueryDownload.argtypes = [c_int, POINTER(OM_DOWNLOAD_STATUS), POINTER(c_int)]
    OmQueryDownload.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 991
for _lib in _libs.values():
    if not _lib.has("OmWaitForDownload", "cdecl"):
        continue
    OmWaitForDownload = _lib.get("OmWaitForDownload", "cdecl")
    OmWaitForDownload.argtypes = [c_int, POINTER(OM_DOWNLOAD_STATUS), POINTER(c_int)]
    OmWaitForDownload.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1001
for _lib in _libs.values():
    if not _lib.has("OmCancelDownload", "cdecl"):
        continue
    OmCancelDownload = _lib.get("OmCancelDownload", "cdecl")
    OmCancelDownload.argtypes = [c_int]
    OmCancelDownload.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1044
for _lib in _libs.values():
    if not _lib.has("OmErrorString", "cdecl"):
        continue
    OmErrorString = _lib.get("OmErrorString", "cdecl")
    OmErrorString.argtypes = [c_int]
    OmErrorString.restype = c_char_p
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1099
for _lib in _libs.values():
    if not _lib.has("OmDateTimeFromString", "cdecl"):
        continue
    OmDateTimeFromString = _lib.get("OmDateTimeFromString", "cdecl")
    OmDateTimeFromString.argtypes = [String]
    OmDateTimeFromString.restype = OM_DATETIME
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1103
for _lib in _libs.values():
    if not _lib.has("OmDateTimeToString", "cdecl"):
        continue
    OmDateTimeToString = _lib.get("OmDateTimeToString", "cdecl")
    OmDateTimeToString.argtypes = [OM_DATETIME, String]
    if sizeof(c_int) == sizeof(c_void_p):
        OmDateTimeToString.restype = ReturnString
    else:
        OmDateTimeToString.restype = String
        OmDateTimeToString.errcheck = ReturnString
    break

OmReaderHandle = POINTER(None)# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1130

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1161
for _lib in _libs.values():
    if not _lib.has("OmReaderOpen", "cdecl"):
        continue
    OmReaderOpen = _lib.get("OmReaderOpen", "cdecl")
    OmReaderOpen.argtypes = [String]
    OmReaderOpen.restype = OmReaderHandle
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1174
for _lib in _libs.values():
    if not _lib.has("OmReaderDataRange", "cdecl"):
        continue
    OmReaderDataRange = _lib.get("OmReaderDataRange", "cdecl")
    OmReaderDataRange.argtypes = [OmReaderHandle, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmReaderDataRange.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1184
for _lib in _libs.values():
    if not _lib.has("OmReaderMetadata", "cdecl"):
        continue
    OmReaderMetadata = _lib.get("OmReaderMetadata", "cdecl")
    OmReaderMetadata.argtypes = [OmReaderHandle, POINTER(c_int), POINTER(c_uint)]
    OmReaderMetadata.restype = c_char_p
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1192
for _lib in _libs.values():
    if not _lib.has("OmReaderDataBlockPosition", "cdecl"):
        continue
    OmReaderDataBlockPosition = _lib.get("OmReaderDataBlockPosition", "cdecl")
    OmReaderDataBlockPosition.argtypes = [OmReaderHandle]
    OmReaderDataBlockPosition.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1201
for _lib in _libs.values():
    if not _lib.has("OmReaderDataBlockSeek", "cdecl"):
        continue
    OmReaderDataBlockSeek = _lib.get("OmReaderDataBlockSeek", "cdecl")
    OmReaderDataBlockSeek.argtypes = [OmReaderHandle, c_int]
    OmReaderDataBlockSeek.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1213
for _lib in _libs.values():
    if not _lib.has("OmReaderNextBlock", "cdecl"):
        continue
    OmReaderNextBlock = _lib.get("OmReaderNextBlock", "cdecl")
    OmReaderNextBlock.argtypes = [OmReaderHandle]
    OmReaderNextBlock.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1225
for _lib in _libs.values():
    if not _lib.has("OmReaderBuffer", "cdecl"):
        continue
    OmReaderBuffer = _lib.get("OmReaderBuffer", "cdecl")
    OmReaderBuffer.argtypes = [OmReaderHandle]
    OmReaderBuffer.restype = POINTER(c_short)
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1240
for _lib in _libs.values():
    if not _lib.has("OmReaderTimestamp", "cdecl"):
        continue
    OmReaderTimestamp = _lib.get("OmReaderTimestamp", "cdecl")
    OmReaderTimestamp.argtypes = [OmReaderHandle, c_int, POINTER(c_ushort)]
    OmReaderTimestamp.restype = OM_DATETIME
    break

enum_anon_11 = c_int# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_DEVICEID = 3# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_SESSIONID = 4# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_SEQUENCEID = 5# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_LIGHT = 7# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_TEMPERATURE = 8# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_EVENTS = 9# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_BATTERY = 10# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_SAMPLERATE = 11# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_LIGHT_LOG10LUXTIMES10POWER3 = 107# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_TEMPERATURE_MC = 108# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_BATTERY_MV = 110# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_BATTERY_PERCENT = 210# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_AXES = 12# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_SCALE_ACCEL = 13# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_SCALE_GYRO = 14# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_SCALE_MAG = 15# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_ACCEL_AXIS = 16# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_GYRO_AXIS = 17# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_VALUE_MAG_AXIS = 18# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

OM_READER_VALUE_TYPE = enum_anon_11# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1275

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1287
for _lib in _libs.values():
    if not _lib.has("OmReaderGetValue", "cdecl"):
        continue
    OmReaderGetValue = _lib.get("OmReaderGetValue", "cdecl")
    OmReaderGetValue.argtypes = [OmReaderHandle, OM_READER_VALUE_TYPE]
    OmReaderGetValue.restype = c_int
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1314
class struct_anon_12(Structure):
    pass

struct_anon_12._pack_ = 1
struct_anon_12.__slots__ = [
    'packetHeader',
    'packetLength',
    'reserved1',
    'deviceId',
    'sessionId',
    'reserved2',
    'loggingStartTime',
    'loggingEndTime',
    'loggingCapacity',
    'reserved3',
    'samplingRate',
    'lastChangeTime',
    'firmwareRevision',
    'timeZone',
    'reserved4',
    'annotation',
    'reserved',
]
struct_anon_12._fields_ = [
    ('packetHeader', c_ushort),
    ('packetLength', c_ushort),
    ('reserved1', c_ubyte),
    ('deviceId', c_ushort),
    ('sessionId', c_uint),
    ('reserved2', c_ushort),
    ('loggingStartTime', OM_DATETIME),
    ('loggingEndTime', OM_DATETIME),
    ('loggingCapacity', c_uint),
    ('reserved3', c_ubyte * int(11)),
    ('samplingRate', c_ubyte),
    ('lastChangeTime', c_uint),
    ('firmwareRevision', c_ubyte),
    ('timeZone', c_short),
    ('reserved4', c_ubyte * int(20)),
    ('annotation', c_ubyte * int(448)),
    ('reserved', c_ubyte * int(512)),
]

OM_READER_HEADER_PACKET = struct_anon_12# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1314

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1325
for _lib in _libs.values():
    if not _lib.has("OmReaderRawHeaderPacket", "cdecl"):
        continue
    OmReaderRawHeaderPacket = _lib.get("OmReaderRawHeaderPacket", "cdecl")
    OmReaderRawHeaderPacket.argtypes = [OmReaderHandle]
    OmReaderRawHeaderPacket.restype = POINTER(OM_READER_HEADER_PACKET)
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1351
class struct_anon_13(Structure):
    pass

struct_anon_13._pack_ = 1
struct_anon_13.__slots__ = [
    'packetHeader',
    'packetLength',
    'deviceFractional',
    'sessionId',
    'sequenceId',
    'timestamp',
    'light',
    'temperature',
    'events',
    'battery',
    'sampleRate',
    'numAxesBPS',
    'timestampOffset',
    'sampleCount',
    'rawSampleData',
    'checksum',
]
struct_anon_13._fields_ = [
    ('packetHeader', c_ushort),
    ('packetLength', c_ushort),
    ('deviceFractional', c_ushort),
    ('sessionId', c_uint),
    ('sequenceId', c_uint),
    ('timestamp', OM_DATETIME),
    ('light', c_ushort),
    ('temperature', c_ushort),
    ('events', c_ubyte),
    ('battery', c_ubyte),
    ('sampleRate', c_ubyte),
    ('numAxesBPS', c_ubyte),
    ('timestampOffset', c_short),
    ('sampleCount', c_ushort),
    ('rawSampleData', c_ubyte * int(480)),
    ('checksum', c_ushort),
]

OM_READER_DATA_PACKET = struct_anon_13# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1351

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1363
for _lib in _libs.values():
    if not _lib.has("OmReaderRawDataPacket", "cdecl"):
        continue
    OmReaderRawDataPacket = _lib.get("OmReaderRawDataPacket", "cdecl")
    OmReaderRawDataPacket.argtypes = [OmReaderHandle]
    OmReaderRawDataPacket.restype = POINTER(OM_READER_DATA_PACKET)
    break

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1372
for _lib in _libs.values():
    if not _lib.has("OmReaderClose", "cdecl"):
        continue
    OmReaderClose = _lib.get("OmReaderClose", "cdecl")
    OmReaderClose.argtypes = [OmReaderHandle]
    OmReaderClose.restype = None
    break

# <built-in>
try:
    __CHAR_BIT__ = 8
except:
    pass

# <built-in>
try:
    __SCHAR_MAX__ = 0x7f
except:
    pass

# <built-in>
try:
    __SHRT_MAX__ = 0x7fff
except:
    pass

# <built-in>
try:
    __INT_MAX__ = 0x7fffffff
except:
    pass

# <built-in>
try:
    __LONG_MAX__ = 0x7fffffff
except:
    pass

# <built-in>
try:
    __LONG_LONG_MAX__ = 0x7fffffffffffffff
except:
    pass

# <command-line>: 0
try:
    _REENTRANT = 1
except:
    pass

__const = c_int# <command-line>: 0

# <command-line>: 0
try:
    CTYPESGEN = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 10
def __STRINGIFY(x):
    return x

# C:/msys64/ucrt64/include/_mingw_mac.h: 11
def __MINGW64_STRINGIFY(x):
    return (__STRINGIFY (x))

# C:/msys64/ucrt64/include/_mingw_mac.h: 14
try:
    __MINGW64_VERSION_MAJOR = 12
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 15
try:
    __MINGW64_VERSION_MINOR = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 16
try:
    __MINGW64_VERSION_BUGFIX = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 24
try:
    __MINGW64_VERSION_RC = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 33
try:
    __MINGW64_VERSION_STATE = 'alpha'
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 39
try:
    __MINGW32_MAJOR_VERSION = 3
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 40
try:
    __MINGW32_MINOR_VERSION = 11
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 62
try:
    _M_AMD64 = 100
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 63
try:
    _M_X64 = 100
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 100
try:
    _ = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 104
try:
    __MINGW_USE_UNDERSCORE_PREFIX = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 106
# #undef _
try:
    del _
except NameError:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 121
def __MINGW_USYMBOL(sym):
    return sym

# C:/msys64/ucrt64/include/_mingw_mac.h: 195
try:
    __MINGW_HAVE_ANSI_C99_PRINTF = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 196
try:
    __MINGW_HAVE_WIDE_C99_PRINTF = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 197
try:
    __MINGW_HAVE_ANSI_C99_SCANF = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 198
try:
    __MINGW_HAVE_WIDE_C99_SCANF = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 220
try:
    __MINGW_GCC_VERSION = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 228
def __MINGW_GNUC_PREREQ(major, minor):
    return 0

# C:/msys64/ucrt64/include/_mingw_mac.h: 235
def __MINGW_MSC_PREREQ(major, minor):
    return 0

# C:/msys64/ucrt64/include/_mingw_mac.h: 250
try:
    __MINGW_SEC_WARN_STR = 'This function or variable may be unsafe, use _CRT_SECURE_NO_WARNINGS to disable deprecation'
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 253
try:
    __MINGW_MSVC2005_DEPREC_STR = 'This POSIX function is deprecated beginning in Visual C++ 2005, use _CRT_NONSTDC_NO_DEPRECATE to disable deprecation'
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 328
try:
    __MINGW_FORTIFY_LEVEL = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_mac.h: 381
try:
    __MINGW_FORTIFY_VA_ARG = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_secapi.h: 34
try:
    _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_secapi.h: 35
try:
    _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES_MEMORY = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_secapi.h: 36
try:
    _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_secapi.h: 37
try:
    _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw_secapi.h: 38
try:
    _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_MEMORY = 0
except:
    pass

__LONG32 = c_long# C:/msys64/ucrt64/include/_mingw.h: 24

# C:/msys64/ucrt64/include/_mingw.h: 70
try:
    USE___UUIDOF = 0
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 96
try:
    __CRT__NO_INLINE = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 106
def __UNUSED_PARAM(x):
    return x

__restrict_arr = c_int# C:/msys64/ucrt64/include/_mingw.h: 127

# C:/msys64/ucrt64/include/_mingw.h: 222
try:
    __MSVCRT_VERSION__ = 0xE00
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 232
try:
    _WIN32_WINNT = 0x603
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 654
try:
    MINGW_HAS_SECURE_API = 1
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 657
try:
    __STDC_SECURE_LIB__ = 200411
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 658
try:
    __GOT_SECURE_LIB__ = __STDC_SECURE_LIB__
except:
    pass

# C:/msys64/ucrt64/include/sdks/_mingw_ddk.h: 4
try:
    MINGW_HAS_DDK_H = 1
except:
    pass

# C:/msys64/ucrt64/include/vadefs.h: 13
try:
    _CRT_PACKING = 8
except:
    pass

# C:/msys64/ucrt64/include/vadefs.h: 42
def _ADDRESSOF(v):
    return pointer(v)

# C:/msys64/ucrt64/include/_mingw.h: 285
def __CRT_STRINGIZE(_Value):
    return _Value

# C:/msys64/ucrt64/include/_mingw.h: 286
def _CRT_STRINGIZE(_Value):
    return (__CRT_STRINGIZE (_Value))

# C:/msys64/ucrt64/include/_mingw.h: 348
try:
    _SECURECRT_FILL_BUFFER_PATTERN = 0xFD
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 401
try:
    _ARGMAX = 100
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 404
try:
    _TRUNCATE = (c_size_t (ord_if_char((-1)))).value
except:
    pass

# C:/msys64/ucrt64/include/_mingw.h: 408
def _CRT_UNUSED(x):
    return None

# C:/msys64/ucrt64/include/_mingw.h: 434
try:
    __USE_MINGW_ANSI_STDIO = 0
except:
    pass

# C:/msys64/ucrt64/include/corecrt.h: 13
# #undef _CRT_PACKING
try:
    del _CRT_PACKING
except NameError:
    pass

# C:/msys64/ucrt64/include/corecrt.h: 14
try:
    _CRT_PACKING = 8
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 20
try:
    PATH_MAX = 260
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 22
try:
    CHAR_BIT = 8
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 23
try:
    SCHAR_MIN = (-128)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 24
try:
    SCHAR_MAX = 127
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 25
try:
    UCHAR_MAX = 0xff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 31
try:
    CHAR_MIN = SCHAR_MIN
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 32
try:
    CHAR_MAX = SCHAR_MAX
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 35
try:
    MB_LEN_MAX = 5
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 36
try:
    SHRT_MIN = (-32768)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 37
try:
    SHRT_MAX = 32767
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 38
try:
    USHRT_MAX = 0xffff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 39
try:
    INT_MIN = ((-2147483647) - 1)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 40
try:
    INT_MAX = 2147483647
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 41
try:
    UINT_MAX = 0xffffffff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 42
try:
    LONG_MIN = ((-2147483647) - 1)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 43
try:
    LONG_MAX = 2147483647
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 44
try:
    ULONG_MAX = 0xffffffff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 45
try:
    LLONG_MAX = 9223372036854775807
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 46
try:
    LLONG_MIN = ((-9223372036854775807) - 1)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 47
try:
    ULLONG_MAX = 0xffffffffffffffff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 49
try:
    _I8_MIN = ((-127) - 1)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 50
try:
    _I8_MAX = 127
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 51
try:
    _UI8_MAX = 0xff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 53
try:
    _I16_MIN = ((-32767) - 1)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 54
try:
    _I16_MAX = 32767
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 55
try:
    _UI16_MAX = 0xffff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 57
try:
    _I32_MIN = ((-2147483647) - 1)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 58
try:
    _I32_MAX = 2147483647
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 59
try:
    _UI32_MAX = 0xffffffff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 70
try:
    _I64_MIN = ((-9223372036854775807) - 1)
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 71
try:
    _I64_MAX = 9223372036854775807
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 72
try:
    _UI64_MAX = 0xffffffffffffffff
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 76
try:
    SIZE_MAX = _UI64_MAX
except:
    pass

# C:/msys64/ucrt64/include/limits.h: 84
try:
    SSIZE_MAX = _I64_MAX
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 63
# #undef CHAR_BIT
try:
    del CHAR_BIT
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 64
try:
    CHAR_BIT = __CHAR_BIT__
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 72
# #undef SCHAR_MIN
try:
    del SCHAR_MIN
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 73
try:
    SCHAR_MIN = ((-SCHAR_MAX) - 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 74
# #undef SCHAR_MAX
try:
    del SCHAR_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 75
try:
    SCHAR_MAX = __SCHAR_MAX__
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 78
# #undef UCHAR_MAX
try:
    del UCHAR_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 82
try:
    UCHAR_MAX = ((SCHAR_MAX * 2) + 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 96
# #undef CHAR_MIN
try:
    del CHAR_MIN
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 97
try:
    CHAR_MIN = SCHAR_MIN
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 98
# #undef CHAR_MAX
try:
    del CHAR_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 99
try:
    CHAR_MAX = SCHAR_MAX
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 103
# #undef SHRT_MIN
try:
    del SHRT_MIN
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 104
try:
    SHRT_MIN = ((-SHRT_MAX) - 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 105
# #undef SHRT_MAX
try:
    del SHRT_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 106
try:
    SHRT_MAX = __SHRT_MAX__
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 109
# #undef USHRT_MAX
try:
    del USHRT_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 113
try:
    USHRT_MAX = ((SHRT_MAX * 2) + 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 117
# #undef INT_MIN
try:
    del INT_MIN
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 118
try:
    INT_MIN = ((-INT_MAX) - 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 119
# #undef INT_MAX
try:
    del INT_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 120
try:
    INT_MAX = __INT_MAX__
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 123
# #undef UINT_MAX
try:
    del UINT_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 124
try:
    UINT_MAX = ((INT_MAX * 2) + 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 128
# #undef LONG_MIN
try:
    del LONG_MIN
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 129
try:
    LONG_MIN = ((-LONG_MAX) - 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 130
# #undef LONG_MAX
try:
    del LONG_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 131
try:
    LONG_MAX = __LONG_MAX__
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 134
# #undef ULONG_MAX
try:
    del ULONG_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 135
try:
    ULONG_MAX = ((LONG_MAX * 2) + 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 139
# #undef LLONG_MIN
try:
    del LLONG_MIN
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 140
try:
    LLONG_MIN = ((-LLONG_MAX) - 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 141
# #undef LLONG_MAX
try:
    del LLONG_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 142
try:
    LLONG_MAX = __LONG_LONG_MAX__
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 145
# #undef ULLONG_MAX
try:
    del ULLONG_MAX
except NameError:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 146
try:
    ULLONG_MAX = ((LLONG_MAX * 2) + 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 152
try:
    LONG_LONG_MIN = ((-LONG_LONG_MAX) - 1)
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 154
try:
    LONG_LONG_MAX = __LONG_LONG_MAX__
except:
    pass

# C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/limits.h: 158
try:
    ULONG_LONG_MAX = ((LONG_LONG_MAX * 2) + 1)
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 44
try:
    EXIT_SUCCESS = 0
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 45
try:
    EXIT_FAILURE = 1
except:
    pass

onexit_t = _onexit_t# C:/msys64/ucrt64/include/stdlib.h: 53

# C:/msys64/ucrt64/include/stdlib.h: 80
def _PTR_LD(x):
    return cast(pointer((x.contents.ld)), POINTER(c_ubyte))

# C:/msys64/ucrt64/include/stdlib.h: 106
try:
    RAND_MAX = 0x7fff
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 109
try:
    MB_CUR_MAX = (___mb_cur_max_func ())
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 118
try:
    __mb_cur_max = (___mb_cur_max_func ())
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 124
def __max(a, b):
    return (a > b) and a or b

# C:/msys64/ucrt64/include/stdlib.h: 125
def __min(a, b):
    return (a < b) and a or b

# C:/msys64/ucrt64/include/stdlib.h: 127
try:
    _MAX_PATH = 260
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 128
try:
    _MAX_DRIVE = 3
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 129
try:
    _MAX_DIR = 256
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 130
try:
    _MAX_FNAME = 256
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 131
try:
    _MAX_EXT = 256
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 133
try:
    _OUT_TO_DEFAULT = 0
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 134
try:
    _OUT_TO_STDERR = 1
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 135
try:
    _OUT_TO_MSGBOX = 2
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 136
try:
    _REPORT_ERRMODE = 3
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 138
try:
    _WRITE_ABORT_MSG = 0x1
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 139
try:
    _CALL_REPORTFAULT = 0x2
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 141
try:
    _MAX_ENV = 32767
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 155
try:
    errno = ((_errno ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 160
try:
    _doserrno = ((__doserrno ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 170
try:
    _sys_nerr = ((__sys_nerr ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 171
try:
    _sys_errlist = (__sys_errlist ())
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 197
try:
    _fmode = ((__p__fmode ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 252
try:
    __argc = ((__p___argc ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 255
try:
    __argv = ((__p___argv ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 258
try:
    __wargv = ((__p___wargv ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 263
try:
    _environ = ((__p__environ ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 267
try:
    _wenviron = ((__p__wenviron ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 272
try:
    _pgmptr = ((__p__pgmptr ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 276
try:
    _wpgmptr = ((__p__wpgmptr ())[0])
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 377
def _countof(_Array):
    return (sizeof(_Array) / sizeof((_Array [0])))

# C:/msys64/ucrt64/include/stdlib.h: 613
try:
    _CVTBUFSIZE = (309 + 40)
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 707
try:
    sys_errlist = _sys_errlist
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 708
try:
    sys_nerr = _sys_nerr
except:
    pass

# C:/msys64/ucrt64/include/stdlib.h: 709
try:
    environ = _environ
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 18
try:
    _HEAP_MAXREQ = 0xFFFFFFFFFFFFFFE0
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 32
try:
    _HEAPEMPTY = (-1)
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 33
try:
    _HEAPOK = (-2)
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 34
try:
    _HEAPBADBEGIN = (-3)
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 35
try:
    _HEAPBADNODE = (-4)
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 36
try:
    _HEAPEND = (-5)
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 37
try:
    _HEAPBADPTR = (-6)
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 40
try:
    _FREEENTRY = 0
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 41
try:
    _USEDENTRY = 1
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 24
try:
    EPERM = 1
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 25
try:
    ENOENT = 2
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 26
try:
    ENOFILE = ENOENT
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 27
try:
    ESRCH = 3
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 28
try:
    EINTR = 4
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 29
try:
    EIO = 5
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 30
try:
    ENXIO = 6
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 31
try:
    E2BIG = 7
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 32
try:
    ENOEXEC = 8
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 33
try:
    EBADF = 9
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 34
try:
    ECHILD = 10
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 35
try:
    EAGAIN = 11
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 36
try:
    ENOMEM = 12
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 37
try:
    EACCES = 13
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 38
try:
    EFAULT = 14
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 39
try:
    EBUSY = 16
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 40
try:
    EEXIST = 17
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 41
try:
    EXDEV = 18
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 42
try:
    ENODEV = 19
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 43
try:
    ENOTDIR = 20
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 44
try:
    EISDIR = 21
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 45
try:
    ENFILE = 23
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 46
try:
    EMFILE = 24
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 47
try:
    ENOTTY = 25
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 48
try:
    EFBIG = 27
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 49
try:
    ENOSPC = 28
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 50
try:
    ESPIPE = 29
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 51
try:
    EROFS = 30
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 52
try:
    EMLINK = 31
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 53
try:
    EPIPE = 32
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 54
try:
    EDOM = 33
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 55
try:
    EDEADLK = 36
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 56
try:
    ENAMETOOLONG = 38
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 57
try:
    ENOLCK = 39
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 58
try:
    ENOSYS = 40
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 59
try:
    ENOTEMPTY = 41
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 64
try:
    EINVAL = 22
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 65
try:
    ERANGE = 34
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 66
try:
    EILSEQ = 42
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 67
try:
    STRUNCATE = 80
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 71
try:
    EDEADLOCK = EDEADLK
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 76
try:
    ENOTSUP = 129
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 82
try:
    EAFNOSUPPORT = 102
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 86
try:
    EADDRINUSE = 100
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 90
try:
    EADDRNOTAVAIL = 101
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 94
try:
    EISCONN = 113
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 98
try:
    ENOBUFS = 119
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 102
try:
    ECONNABORTED = 106
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 106
try:
    EALREADY = 103
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 110
try:
    ECONNREFUSED = 107
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 114
try:
    ECONNRESET = 108
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 118
try:
    EDESTADDRREQ = 109
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 122
try:
    EHOSTUNREACH = 110
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 126
try:
    EMSGSIZE = 115
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 130
try:
    ENETDOWN = 116
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 134
try:
    ENETRESET = 117
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 138
try:
    ENETUNREACH = 118
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 142
try:
    ENOPROTOOPT = 123
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 146
try:
    ENOTSOCK = 128
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 150
try:
    ENOTCONN = 126
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 154
try:
    ECANCELED = 105
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 158
try:
    EINPROGRESS = 112
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 162
try:
    EOPNOTSUPP = 130
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 166
try:
    EWOULDBLOCK = 140
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 170
try:
    EOWNERDEAD = 133
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 174
try:
    EPROTO = 134
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 178
try:
    EPROTONOSUPPORT = 135
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 182
try:
    EBADMSG = 104
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 186
try:
    EIDRM = 111
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 190
try:
    ENODATA = 120
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 194
try:
    ENOLINK = 121
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 198
try:
    ENOMSG = 122
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 202
try:
    ENOSR = 124
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 206
try:
    ENOSTR = 125
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 210
try:
    ENOTRECOVERABLE = 127
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 214
try:
    ETIME = 137
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 218
try:
    ETXTBSY = 139
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 223
try:
    ETIMEDOUT = 138
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 227
try:
    ELOOP = 114
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 231
try:
    EPROTOTYPE = 136
except:
    pass

# C:/msys64/ucrt64/include/errno.h: 235
try:
    EOVERFLOW = 132
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 87
try:
    _MAX_WAIT_MALLOC_CRT = 60000
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 114
try:
    _ALLOCA_S_THRESHOLD = 1024
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 115
try:
    _ALLOCA_S_STACK_MARKER = 0xCCCC
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 116
try:
    _ALLOCA_S_HEAP_MARKER = 0xDDDD
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 121
try:
    _ALLOCA_S_MARKER_SIZE = 16
except:
    pass

# C:/msys64/ucrt64/include/malloc.h: 166
try:
    alloca = _alloca
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 228
try:
    OM_VERSION = 108
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 434
try:
    OM_MEMORY_HEALTH_ERROR = 1
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 435
try:
    OM_MEMORY_HEALTH_WARNING = 8
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 656
try:
    OM_METADATA_SIZE = 448
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 735
def OmClearDataAndCommit(_deviceId):
    return (OmEraseDataAndCommit (_deviceId, OM_ERASE_QUICKFORMAT))

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 748
def OmCommit(_deviceId):
    return (OmEraseDataAndCommit (_deviceId, OM_ERASE_NONE))

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 756
try:
    OM_ACCEL_DEFAULT_RATE = 100
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 764
try:
    OM_ACCEL_DEFAULT_RANGE = 8
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 843
try:
    OM_MAX_PATH = 256
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1020
try:
    OM_TRUE = 1
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1021
try:
    OM_FALSE = 0
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1022
try:
    OM_OK = 0
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1023
try:
    OM_E_FAIL = (-1)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1024
try:
    OM_E_UNEXPECTED = (-2)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1025
try:
    OM_E_NOT_VALID_STATE = (-3)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1026
try:
    OM_E_OUT_OF_MEMORY = (-4)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1027
try:
    OM_E_INVALID_ARG = (-5)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1028
try:
    OM_E_POINTER = (-6)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1029
try:
    OM_E_NOT_IMPLEMENTED = (-7)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1030
try:
    OM_E_ABORT = (-8)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1031
try:
    OM_E_ACCESS_DENIED = (-9)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1032
try:
    OM_E_INVALID_DEVICE = (-10)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1033
try:
    OM_E_UNEXPECTED_RESPONSE = (-11)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1034
try:
    OM_E_LOCKED = (-12)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1035
def OM_SUCCEEDED(value):
    return (value >= 0)

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1036
def OM_FAILED(value):
    return (value < 0)

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1076
def OM_DATETIME_FROM_YMDHMS(year, month, day, hours, minutes, seconds):
    return ((((((((OM_DATETIME (ord_if_char((year % 100)))).value & 0x3f) << 26) | (((OM_DATETIME (ord_if_char(month))).value & 0x0f) << 22)) | (((OM_DATETIME (ord_if_char(day))).value & 0x1f) << 17)) | (((OM_DATETIME (ord_if_char(hours))).value & 0x1f) << 12)) | (((OM_DATETIME (ord_if_char(minutes))).value & 0x3f) << 6)) | ((OM_DATETIME (ord_if_char(seconds))).value & 0x3f))

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1084
def OM_DATETIME_YEAR(dateTime):
    return ((c_uint (ord_if_char((c_ubyte (ord_if_char(((dateTime >> 26) & 0x3f)))).value))).value + 2000)

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1085
def OM_DATETIME_MONTH(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 22) & 0x0f)))).value

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1086
def OM_DATETIME_DAY(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 17) & 0x1f)))).value

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1087
def OM_DATETIME_HOURS(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 12) & 0x1f)))).value

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1088
def OM_DATETIME_MINUTES(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 6) & 0x3f)))).value

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1089
def OM_DATETIME_SECONDS(dateTime):
    return (c_ubyte (ord_if_char((dateTime & 0x3f)))).value

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1090
try:
    OM_DATETIME_MIN_VALID = (OM_DATETIME_FROM_YMDHMS (2000, 1, 1, 0, 0, 0))
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1091
try:
    OM_DATETIME_MAX_VALID = (OM_DATETIME_FROM_YMDHMS (2063, 12, 31, 23, 59, 59))
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1092
try:
    OM_DATETIME_ZERO = 0
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1093
try:
    OM_DATETIME_INFINITE = (OM_DATETIME (ord_if_char((-1)))).value
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1096
try:
    OM_DATETIME_BUFFER_SIZE = 20
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1137
try:
    OM_MAX_SAMPLES = 120
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1144
try:
    OM_MAX_HEADER_SIZE = (2 * 512)
except:
    pass

# C:\\Users\\mikec\\OneDrive\\Desktop\\RIGHTSTEP\\OsteoSense\\ax6\\rs-ax6\\bindings\\rs-python\\c\\omapi.h: 1151
try:
    OM_MAX_DATA_SIZE = 512
except:
    pass

threadlocaleinfostruct = struct_threadlocaleinfostruct# C:/msys64/ucrt64/include/corecrt.h: 452

threadmbcinfostruct = struct_threadmbcinfostruct# C:/msys64/ucrt64/include/corecrt.h: 431

__lc_time_data = struct___lc_time_data# C:/msys64/ucrt64/include/corecrt.h: 434

localeinfo_struct = struct_localeinfo_struct# C:/msys64/ucrt64/include/corecrt.h: 439

tagLC_ID = struct_tagLC_ID# C:/msys64/ucrt64/include/corecrt.h: 447

_div_t = struct__div_t# C:/msys64/ucrt64/include/stdlib.h: 63

_ldiv_t = struct__ldiv_t# C:/msys64/ucrt64/include/stdlib.h: 68

_heapinfo = struct__heapinfo# C:/msys64/ucrt64/include/malloc.h: 50

# No inserted files

# No prefix-stripping

