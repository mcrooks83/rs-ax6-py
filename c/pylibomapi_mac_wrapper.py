r"""Wrapper for omapi.h

Generated with:
/Library/Frameworks/Python.framework/Versions/3.10/bin/ctypesgen -a -l libomapi.so omapi.h -o pylibomapi_wrapper.py

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

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

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
_libs["libomapi.so"] = load_library("libomapi.so")

# 1 libraries
# End libraries

# No modules

__int8_t = c_char# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 41

__uint8_t = c_ubyte# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 43

__int16_t = c_short# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 44

__uint16_t = c_ushort# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 45

__int32_t = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 46

__uint32_t = c_uint# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 47

__int64_t = c_longlong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 48

__uint64_t = c_ulonglong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 49

__darwin_intptr_t = c_long# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 51

__darwin_natural_t = c_uint# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 52

__darwin_ct_rune_t = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 72

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 81
class union_anon_1(Union):
    pass

union_anon_1.__slots__ = [
    '__mbstate8',
    '_mbstateL',
]
union_anon_1._fields_ = [
    ('__mbstate8', c_char * int(128)),
    ('_mbstateL', c_longlong),
]

__mbstate_t = union_anon_1# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 81

__darwin_mbstate_t = __mbstate_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 83

__darwin_ptrdiff_t = c_long# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 86

__darwin_size_t = c_ulong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 94

__darwin_va_list = POINTER(None)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 102

__darwin_wchar_t = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 106

__darwin_rune_t = __darwin_wchar_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 111

__darwin_wint_t = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 114

__darwin_clock_t = c_ulong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 119

__darwin_socklen_t = __uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 120

__darwin_ssize_t = c_long# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 121

__darwin_time_t = c_long# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 122

__darwin_blkcnt_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 55

__darwin_blksize_t = c_int32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 56

__darwin_dev_t = c_int32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 57

__darwin_fsblkcnt_t = c_uint# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 58

__darwin_fsfilcnt_t = c_uint# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 59

__darwin_gid_t = __uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 60

__darwin_id_t = __uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 61

__darwin_ino64_t = __uint64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 62

__darwin_ino_t = __darwin_ino64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 64

__darwin_mach_port_name_t = __darwin_natural_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 68

__darwin_mach_port_t = __darwin_mach_port_name_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 69

__darwin_mode_t = __uint16_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 70

__darwin_off_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 71

__darwin_pid_t = c_int32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 72

__darwin_sigset_t = __uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 73

__darwin_suseconds_t = c_int32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 74

__darwin_uid_t = __uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 75

__darwin_useconds_t = __uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 76

__darwin_uuid_t = c_ubyte * int(16)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 77

__darwin_uuid_string_t = c_char * int(37)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 78

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 57
class struct___darwin_pthread_handler_rec(Structure):
    pass

struct___darwin_pthread_handler_rec.__slots__ = [
    '__routine',
    '__arg',
    '__next',
]
struct___darwin_pthread_handler_rec._fields_ = [
    ('__routine', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('__arg', POINTER(None)),
    ('__next', POINTER(struct___darwin_pthread_handler_rec)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 63
class struct__opaque_pthread_attr_t(Structure):
    pass

struct__opaque_pthread_attr_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_attr_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(56)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 68
class struct__opaque_pthread_cond_t(Structure):
    pass

struct__opaque_pthread_cond_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_cond_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(40)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 73
class struct__opaque_pthread_condattr_t(Structure):
    pass

struct__opaque_pthread_condattr_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_condattr_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(8)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 78
class struct__opaque_pthread_mutex_t(Structure):
    pass

struct__opaque_pthread_mutex_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_mutex_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(56)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 83
class struct__opaque_pthread_mutexattr_t(Structure):
    pass

struct__opaque_pthread_mutexattr_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_mutexattr_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(8)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 88
class struct__opaque_pthread_once_t(Structure):
    pass

struct__opaque_pthread_once_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_once_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(8)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 93
class struct__opaque_pthread_rwlock_t(Structure):
    pass

struct__opaque_pthread_rwlock_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_rwlock_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(192)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 98
class struct__opaque_pthread_rwlockattr_t(Structure):
    pass

struct__opaque_pthread_rwlockattr_t.__slots__ = [
    '__sig',
    '__opaque',
]
struct__opaque_pthread_rwlockattr_t._fields_ = [
    ('__sig', c_long),
    ('__opaque', c_char * int(16)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 103
class struct__opaque_pthread_t(Structure):
    pass

struct__opaque_pthread_t.__slots__ = [
    '__sig',
    '__cleanup_stack',
    '__opaque',
]
struct__opaque_pthread_t._fields_ = [
    ('__sig', c_long),
    ('__cleanup_stack', POINTER(struct___darwin_pthread_handler_rec)),
    ('__opaque', c_char * int(8176)),
]

__darwin_pthread_attr_t = struct__opaque_pthread_attr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 109

__darwin_pthread_cond_t = struct__opaque_pthread_cond_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 110

__darwin_pthread_condattr_t = struct__opaque_pthread_condattr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 111

__darwin_pthread_key_t = c_ulong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 112

__darwin_pthread_mutex_t = struct__opaque_pthread_mutex_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 113

__darwin_pthread_mutexattr_t = struct__opaque_pthread_mutexattr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 114

__darwin_pthread_once_t = struct__opaque_pthread_once_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 115

__darwin_pthread_rwlock_t = struct__opaque_pthread_rwlock_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 116

__darwin_pthread_rwlockattr_t = struct__opaque_pthread_rwlockattr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 117

__darwin_pthread_t = POINTER(struct__opaque_pthread_t)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 118

__darwin_nl_item = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types.h: 40

__darwin_wctrans_t = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types.h: 41

__darwin_wctype_t = __uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types.h: 43

enum_anon_2 = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 83

P_ALL = 0# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 83

P_PID = (P_ALL + 1)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 83

P_PGID = (P_PID + 1)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 83

idtype_t = enum_anon_2# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 83

pid_t = __darwin_pid_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_pid_t.h: 31

id_t = __darwin_id_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_id_t.h: 31

sig_atomic_t = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/signal.h: 41

int8_t = c_char# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_int8_t.h: 30

int16_t = c_short# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_int16_t.h: 30

int32_t = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_int32_t.h: 30

int64_t = c_longlong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_int64_t.h: 30

u_int8_t = c_ubyte# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int8_t.h: 30

u_int16_t = c_ushort# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int16_t.h: 30

u_int32_t = c_uint# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int32_t.h: 30

u_int64_t = c_ulonglong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int64_t.h: 30

register_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 90

intptr_t = __darwin_intptr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_intptr_t.h: 32

uintptr_t = c_ulong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_uintptr_t.h: 34

user_addr_t = u_int64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 100

user_size_t = u_int64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 101

user_ssize_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 102

user_long_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 103

user_ulong_t = u_int64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 104

user_time_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 105

user_off_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 106

syscall_arg_t = u_int64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 114

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 48
class struct___darwin_i386_thread_state(Structure):
    pass

struct___darwin_i386_thread_state.__slots__ = [
    '__eax',
    '__ebx',
    '__ecx',
    '__edx',
    '__edi',
    '__esi',
    '__ebp',
    '__esp',
    '__ss',
    '__eflags',
    '__eip',
    '__cs',
    '__ds',
    '__es',
    '__fs',
    '__gs',
]
struct___darwin_i386_thread_state._fields_ = [
    ('__eax', c_uint),
    ('__ebx', c_uint),
    ('__ecx', c_uint),
    ('__edx', c_uint),
    ('__edi', c_uint),
    ('__esi', c_uint),
    ('__ebp', c_uint),
    ('__esp', c_uint),
    ('__ss', c_uint),
    ('__eflags', c_uint),
    ('__eip', c_uint),
    ('__cs', c_uint),
    ('__ds', c_uint),
    ('__es', c_uint),
    ('__fs', c_uint),
    ('__gs', c_uint),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 94
class struct___darwin_fp_control(Structure):
    pass

struct___darwin_fp_control.__slots__ = [
    '__invalid',
    '__denorm',
    '__zdiv',
    '__ovrfl',
    '__undfl',
    '__precis',
    'unnamed_1',
    '__pc',
    '__rc',
    'unnamed_2',
    'unnamed_3',
]
struct___darwin_fp_control._fields_ = [
    ('__invalid', c_ushort, 1),
    ('__denorm', c_ushort, 1),
    ('__zdiv', c_ushort, 1),
    ('__ovrfl', c_ushort, 1),
    ('__undfl', c_ushort, 1),
    ('__precis', c_ushort, 1),
    ('unnamed_1', c_ushort, 2),
    ('__pc', c_ushort, 2),
    ('__rc', c_ushort, 2),
    ('unnamed_2', c_ushort, 1),
    ('unnamed_3', c_ushort, 3),
]

__darwin_fp_control_t = struct___darwin_fp_control# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 119

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 152
class struct___darwin_fp_status(Structure):
    pass

struct___darwin_fp_status.__slots__ = [
    '__invalid',
    '__denorm',
    '__zdiv',
    '__ovrfl',
    '__undfl',
    '__precis',
    '__stkflt',
    '__errsumm',
    '__c0',
    '__c1',
    '__c2',
    '__tos',
    '__c3',
    '__busy',
]
struct___darwin_fp_status._fields_ = [
    ('__invalid', c_ushort, 1),
    ('__denorm', c_ushort, 1),
    ('__zdiv', c_ushort, 1),
    ('__ovrfl', c_ushort, 1),
    ('__undfl', c_ushort, 1),
    ('__precis', c_ushort, 1),
    ('__stkflt', c_ushort, 1),
    ('__errsumm', c_ushort, 1),
    ('__c0', c_ushort, 1),
    ('__c1', c_ushort, 1),
    ('__c2', c_ushort, 1),
    ('__tos', c_ushort, 3),
    ('__c3', c_ushort, 1),
    ('__busy', c_ushort, 1),
]

__darwin_fp_status_t = struct___darwin_fp_status# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 169

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 196
class struct___darwin_mmst_reg(Structure):
    pass

struct___darwin_mmst_reg.__slots__ = [
    '__mmst_reg',
    '__mmst_rsrv',
]
struct___darwin_mmst_reg._fields_ = [
    ('__mmst_reg', c_char * int(10)),
    ('__mmst_rsrv', c_char * int(6)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 215
class struct___darwin_xmm_reg(Structure):
    pass

struct___darwin_xmm_reg.__slots__ = [
    '__xmm_reg',
]
struct___darwin_xmm_reg._fields_ = [
    ('__xmm_reg', c_char * int(16)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 231
class struct___darwin_ymm_reg(Structure):
    pass

struct___darwin_ymm_reg.__slots__ = [
    '__ymm_reg',
]
struct___darwin_ymm_reg._fields_ = [
    ('__ymm_reg', c_char * int(32)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 247
class struct___darwin_zmm_reg(Structure):
    pass

struct___darwin_zmm_reg.__slots__ = [
    '__zmm_reg',
]
struct___darwin_zmm_reg._fields_ = [
    ('__zmm_reg', c_char * int(64)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 261
class struct___darwin_opmask_reg(Structure):
    pass

struct___darwin_opmask_reg.__slots__ = [
    '__opmask_reg',
]
struct___darwin_opmask_reg._fields_ = [
    ('__opmask_reg', c_char * int(8)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 283
class struct___darwin_i386_float_state(Structure):
    pass

struct___darwin_i386_float_state.__slots__ = [
    '__fpu_reserved',
    '__fpu_fcw',
    '__fpu_fsw',
    '__fpu_ftw',
    '__fpu_rsrv1',
    '__fpu_fop',
    '__fpu_ip',
    '__fpu_cs',
    '__fpu_rsrv2',
    '__fpu_dp',
    '__fpu_ds',
    '__fpu_rsrv3',
    '__fpu_mxcsr',
    '__fpu_mxcsrmask',
    '__fpu_stmm0',
    '__fpu_stmm1',
    '__fpu_stmm2',
    '__fpu_stmm3',
    '__fpu_stmm4',
    '__fpu_stmm5',
    '__fpu_stmm6',
    '__fpu_stmm7',
    '__fpu_xmm0',
    '__fpu_xmm1',
    '__fpu_xmm2',
    '__fpu_xmm3',
    '__fpu_xmm4',
    '__fpu_xmm5',
    '__fpu_xmm6',
    '__fpu_xmm7',
    '__fpu_rsrv4',
    '__fpu_reserved1',
]
struct___darwin_i386_float_state._fields_ = [
    ('__fpu_reserved', c_int * int(2)),
    ('__fpu_fcw', struct___darwin_fp_control),
    ('__fpu_fsw', struct___darwin_fp_status),
    ('__fpu_ftw', __uint8_t),
    ('__fpu_rsrv1', __uint8_t),
    ('__fpu_fop', __uint16_t),
    ('__fpu_ip', __uint32_t),
    ('__fpu_cs', __uint16_t),
    ('__fpu_rsrv2', __uint16_t),
    ('__fpu_dp', __uint32_t),
    ('__fpu_ds', __uint16_t),
    ('__fpu_rsrv3', __uint16_t),
    ('__fpu_mxcsr', __uint32_t),
    ('__fpu_mxcsrmask', __uint32_t),
    ('__fpu_stmm0', struct___darwin_mmst_reg),
    ('__fpu_stmm1', struct___darwin_mmst_reg),
    ('__fpu_stmm2', struct___darwin_mmst_reg),
    ('__fpu_stmm3', struct___darwin_mmst_reg),
    ('__fpu_stmm4', struct___darwin_mmst_reg),
    ('__fpu_stmm5', struct___darwin_mmst_reg),
    ('__fpu_stmm6', struct___darwin_mmst_reg),
    ('__fpu_stmm7', struct___darwin_mmst_reg),
    ('__fpu_xmm0', struct___darwin_xmm_reg),
    ('__fpu_xmm1', struct___darwin_xmm_reg),
    ('__fpu_xmm2', struct___darwin_xmm_reg),
    ('__fpu_xmm3', struct___darwin_xmm_reg),
    ('__fpu_xmm4', struct___darwin_xmm_reg),
    ('__fpu_xmm5', struct___darwin_xmm_reg),
    ('__fpu_xmm6', struct___darwin_xmm_reg),
    ('__fpu_xmm7', struct___darwin_xmm_reg),
    ('__fpu_rsrv4', c_char * int((14 * 16))),
    ('__fpu_reserved1', c_int),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 320
class struct___darwin_i386_avx_state(Structure):
    pass

struct___darwin_i386_avx_state.__slots__ = [
    '__fpu_reserved',
    '__fpu_fcw',
    '__fpu_fsw',
    '__fpu_ftw',
    '__fpu_rsrv1',
    '__fpu_fop',
    '__fpu_ip',
    '__fpu_cs',
    '__fpu_rsrv2',
    '__fpu_dp',
    '__fpu_ds',
    '__fpu_rsrv3',
    '__fpu_mxcsr',
    '__fpu_mxcsrmask',
    '__fpu_stmm0',
    '__fpu_stmm1',
    '__fpu_stmm2',
    '__fpu_stmm3',
    '__fpu_stmm4',
    '__fpu_stmm5',
    '__fpu_stmm6',
    '__fpu_stmm7',
    '__fpu_xmm0',
    '__fpu_xmm1',
    '__fpu_xmm2',
    '__fpu_xmm3',
    '__fpu_xmm4',
    '__fpu_xmm5',
    '__fpu_xmm6',
    '__fpu_xmm7',
    '__fpu_rsrv4',
    '__fpu_reserved1',
    '__avx_reserved1',
    '__fpu_ymmh0',
    '__fpu_ymmh1',
    '__fpu_ymmh2',
    '__fpu_ymmh3',
    '__fpu_ymmh4',
    '__fpu_ymmh5',
    '__fpu_ymmh6',
    '__fpu_ymmh7',
]
struct___darwin_i386_avx_state._fields_ = [
    ('__fpu_reserved', c_int * int(2)),
    ('__fpu_fcw', struct___darwin_fp_control),
    ('__fpu_fsw', struct___darwin_fp_status),
    ('__fpu_ftw', __uint8_t),
    ('__fpu_rsrv1', __uint8_t),
    ('__fpu_fop', __uint16_t),
    ('__fpu_ip', __uint32_t),
    ('__fpu_cs', __uint16_t),
    ('__fpu_rsrv2', __uint16_t),
    ('__fpu_dp', __uint32_t),
    ('__fpu_ds', __uint16_t),
    ('__fpu_rsrv3', __uint16_t),
    ('__fpu_mxcsr', __uint32_t),
    ('__fpu_mxcsrmask', __uint32_t),
    ('__fpu_stmm0', struct___darwin_mmst_reg),
    ('__fpu_stmm1', struct___darwin_mmst_reg),
    ('__fpu_stmm2', struct___darwin_mmst_reg),
    ('__fpu_stmm3', struct___darwin_mmst_reg),
    ('__fpu_stmm4', struct___darwin_mmst_reg),
    ('__fpu_stmm5', struct___darwin_mmst_reg),
    ('__fpu_stmm6', struct___darwin_mmst_reg),
    ('__fpu_stmm7', struct___darwin_mmst_reg),
    ('__fpu_xmm0', struct___darwin_xmm_reg),
    ('__fpu_xmm1', struct___darwin_xmm_reg),
    ('__fpu_xmm2', struct___darwin_xmm_reg),
    ('__fpu_xmm3', struct___darwin_xmm_reg),
    ('__fpu_xmm4', struct___darwin_xmm_reg),
    ('__fpu_xmm5', struct___darwin_xmm_reg),
    ('__fpu_xmm6', struct___darwin_xmm_reg),
    ('__fpu_xmm7', struct___darwin_xmm_reg),
    ('__fpu_rsrv4', c_char * int((14 * 16))),
    ('__fpu_reserved1', c_int),
    ('__avx_reserved1', c_char * int(64)),
    ('__fpu_ymmh0', struct___darwin_xmm_reg),
    ('__fpu_ymmh1', struct___darwin_xmm_reg),
    ('__fpu_ymmh2', struct___darwin_xmm_reg),
    ('__fpu_ymmh3', struct___darwin_xmm_reg),
    ('__fpu_ymmh4', struct___darwin_xmm_reg),
    ('__fpu_ymmh5', struct___darwin_xmm_reg),
    ('__fpu_ymmh6', struct___darwin_xmm_reg),
    ('__fpu_ymmh7', struct___darwin_xmm_reg),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 366
class struct___darwin_i386_avx512_state(Structure):
    pass

struct___darwin_i386_avx512_state.__slots__ = [
    '__fpu_reserved',
    '__fpu_fcw',
    '__fpu_fsw',
    '__fpu_ftw',
    '__fpu_rsrv1',
    '__fpu_fop',
    '__fpu_ip',
    '__fpu_cs',
    '__fpu_rsrv2',
    '__fpu_dp',
    '__fpu_ds',
    '__fpu_rsrv3',
    '__fpu_mxcsr',
    '__fpu_mxcsrmask',
    '__fpu_stmm0',
    '__fpu_stmm1',
    '__fpu_stmm2',
    '__fpu_stmm3',
    '__fpu_stmm4',
    '__fpu_stmm5',
    '__fpu_stmm6',
    '__fpu_stmm7',
    '__fpu_xmm0',
    '__fpu_xmm1',
    '__fpu_xmm2',
    '__fpu_xmm3',
    '__fpu_xmm4',
    '__fpu_xmm5',
    '__fpu_xmm6',
    '__fpu_xmm7',
    '__fpu_rsrv4',
    '__fpu_reserved1',
    '__avx_reserved1',
    '__fpu_ymmh0',
    '__fpu_ymmh1',
    '__fpu_ymmh2',
    '__fpu_ymmh3',
    '__fpu_ymmh4',
    '__fpu_ymmh5',
    '__fpu_ymmh6',
    '__fpu_ymmh7',
    '__fpu_k0',
    '__fpu_k1',
    '__fpu_k2',
    '__fpu_k3',
    '__fpu_k4',
    '__fpu_k5',
    '__fpu_k6',
    '__fpu_k7',
    '__fpu_zmmh0',
    '__fpu_zmmh1',
    '__fpu_zmmh2',
    '__fpu_zmmh3',
    '__fpu_zmmh4',
    '__fpu_zmmh5',
    '__fpu_zmmh6',
    '__fpu_zmmh7',
]
struct___darwin_i386_avx512_state._fields_ = [
    ('__fpu_reserved', c_int * int(2)),
    ('__fpu_fcw', struct___darwin_fp_control),
    ('__fpu_fsw', struct___darwin_fp_status),
    ('__fpu_ftw', __uint8_t),
    ('__fpu_rsrv1', __uint8_t),
    ('__fpu_fop', __uint16_t),
    ('__fpu_ip', __uint32_t),
    ('__fpu_cs', __uint16_t),
    ('__fpu_rsrv2', __uint16_t),
    ('__fpu_dp', __uint32_t),
    ('__fpu_ds', __uint16_t),
    ('__fpu_rsrv3', __uint16_t),
    ('__fpu_mxcsr', __uint32_t),
    ('__fpu_mxcsrmask', __uint32_t),
    ('__fpu_stmm0', struct___darwin_mmst_reg),
    ('__fpu_stmm1', struct___darwin_mmst_reg),
    ('__fpu_stmm2', struct___darwin_mmst_reg),
    ('__fpu_stmm3', struct___darwin_mmst_reg),
    ('__fpu_stmm4', struct___darwin_mmst_reg),
    ('__fpu_stmm5', struct___darwin_mmst_reg),
    ('__fpu_stmm6', struct___darwin_mmst_reg),
    ('__fpu_stmm7', struct___darwin_mmst_reg),
    ('__fpu_xmm0', struct___darwin_xmm_reg),
    ('__fpu_xmm1', struct___darwin_xmm_reg),
    ('__fpu_xmm2', struct___darwin_xmm_reg),
    ('__fpu_xmm3', struct___darwin_xmm_reg),
    ('__fpu_xmm4', struct___darwin_xmm_reg),
    ('__fpu_xmm5', struct___darwin_xmm_reg),
    ('__fpu_xmm6', struct___darwin_xmm_reg),
    ('__fpu_xmm7', struct___darwin_xmm_reg),
    ('__fpu_rsrv4', c_char * int((14 * 16))),
    ('__fpu_reserved1', c_int),
    ('__avx_reserved1', c_char * int(64)),
    ('__fpu_ymmh0', struct___darwin_xmm_reg),
    ('__fpu_ymmh1', struct___darwin_xmm_reg),
    ('__fpu_ymmh2', struct___darwin_xmm_reg),
    ('__fpu_ymmh3', struct___darwin_xmm_reg),
    ('__fpu_ymmh4', struct___darwin_xmm_reg),
    ('__fpu_ymmh5', struct___darwin_xmm_reg),
    ('__fpu_ymmh6', struct___darwin_xmm_reg),
    ('__fpu_ymmh7', struct___darwin_xmm_reg),
    ('__fpu_k0', struct___darwin_opmask_reg),
    ('__fpu_k1', struct___darwin_opmask_reg),
    ('__fpu_k2', struct___darwin_opmask_reg),
    ('__fpu_k3', struct___darwin_opmask_reg),
    ('__fpu_k4', struct___darwin_opmask_reg),
    ('__fpu_k5', struct___darwin_opmask_reg),
    ('__fpu_k6', struct___darwin_opmask_reg),
    ('__fpu_k7', struct___darwin_opmask_reg),
    ('__fpu_zmmh0', struct___darwin_ymm_reg),
    ('__fpu_zmmh1', struct___darwin_ymm_reg),
    ('__fpu_zmmh2', struct___darwin_ymm_reg),
    ('__fpu_zmmh3', struct___darwin_ymm_reg),
    ('__fpu_zmmh4', struct___darwin_ymm_reg),
    ('__fpu_zmmh5', struct___darwin_ymm_reg),
    ('__fpu_zmmh6', struct___darwin_ymm_reg),
    ('__fpu_zmmh7', struct___darwin_ymm_reg),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 577
class struct___darwin_i386_exception_state(Structure):
    pass

struct___darwin_i386_exception_state.__slots__ = [
    '__trapno',
    '__cpu',
    '__err',
    '__faultvaddr',
]
struct___darwin_i386_exception_state._fields_ = [
    ('__trapno', __uint16_t),
    ('__cpu', __uint16_t),
    ('__err', __uint32_t),
    ('__faultvaddr', __uint32_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 597
class struct___darwin_x86_debug_state32(Structure):
    pass

struct___darwin_x86_debug_state32.__slots__ = [
    '__dr0',
    '__dr1',
    '__dr2',
    '__dr3',
    '__dr4',
    '__dr5',
    '__dr6',
    '__dr7',
]
struct___darwin_x86_debug_state32._fields_ = [
    ('__dr0', c_uint),
    ('__dr1', c_uint),
    ('__dr2', c_uint),
    ('__dr3', c_uint),
    ('__dr4', c_uint),
    ('__dr5', c_uint),
    ('__dr6', c_uint),
    ('__dr7', c_uint),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 610
class struct___x86_instruction_state(Structure):
    pass

struct___x86_instruction_state.__slots__ = [
    '__insn_stream_valid_bytes',
    '__insn_offset',
    '__out_of_synch',
    '__insn_bytes',
    '__insn_cacheline',
]
struct___x86_instruction_state._fields_ = [
    ('__insn_stream_valid_bytes', c_int),
    ('__insn_offset', c_int),
    ('__out_of_synch', c_int),
    ('__insn_bytes', __uint8_t * int(((2448 - 64) - 4))),
    ('__insn_cacheline', __uint8_t * int(64)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 626
class struct___last_branch_record(Structure):
    pass

struct___last_branch_record.__slots__ = [
    '__from_ip',
    '__to_ip',
    '__mispredict',
    '__tsx_abort',
    '__in_tsx',
    '__cycle_count',
    '__reserved',
]
struct___last_branch_record._fields_ = [
    ('__from_ip', __uint64_t),
    ('__to_ip', __uint64_t),
    ('__mispredict', __uint32_t, 1),
    ('__tsx_abort', __uint32_t, 1),
    ('__in_tsx', __uint32_t, 1),
    ('__cycle_count', __uint32_t, 16),
    ('__reserved', __uint32_t, 13),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 638
class struct___last_branch_state(Structure):
    pass

struct___last_branch_state.__slots__ = [
    '__lbr_count',
    '__lbr_supported_tsx',
    '__lbr_supported_cycle_count',
    '__reserved',
    '__lbrs',
]
struct___last_branch_state._fields_ = [
    ('__lbr_count', c_int),
    ('__lbr_supported_tsx', __uint32_t, 1),
    ('__lbr_supported_cycle_count', __uint32_t, 1),
    ('__reserved', __uint32_t, 30),
    ('__lbrs', struct___last_branch_record * int(32)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 704
class struct___x86_pagein_state(Structure):
    pass

struct___x86_pagein_state.__slots__ = [
    '__pagein_error',
]
struct___x86_pagein_state._fields_ = [
    ('__pagein_error', c_int),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 715
class struct___darwin_x86_thread_state64(Structure):
    pass

struct___darwin_x86_thread_state64.__slots__ = [
    '__rax',
    '__rbx',
    '__rcx',
    '__rdx',
    '__rdi',
    '__rsi',
    '__rbp',
    '__rsp',
    '__r8',
    '__r9',
    '__r10',
    '__r11',
    '__r12',
    '__r13',
    '__r14',
    '__r15',
    '__rip',
    '__rflags',
    '__cs',
    '__fs',
    '__gs',
]
struct___darwin_x86_thread_state64._fields_ = [
    ('__rax', __uint64_t),
    ('__rbx', __uint64_t),
    ('__rcx', __uint64_t),
    ('__rdx', __uint64_t),
    ('__rdi', __uint64_t),
    ('__rsi', __uint64_t),
    ('__rbp', __uint64_t),
    ('__rsp', __uint64_t),
    ('__r8', __uint64_t),
    ('__r9', __uint64_t),
    ('__r10', __uint64_t),
    ('__r11', __uint64_t),
    ('__r12', __uint64_t),
    ('__r13', __uint64_t),
    ('__r14', __uint64_t),
    ('__r15', __uint64_t),
    ('__rip', __uint64_t),
    ('__rflags', __uint64_t),
    ('__cs', __uint64_t),
    ('__fs', __uint64_t),
    ('__gs', __uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 773
class struct___darwin_x86_thread_full_state64(Structure):
    pass

struct___darwin_x86_thread_full_state64.__slots__ = [
    '__ss64',
    '__ds',
    '__es',
    '__ss',
    '__gsbase',
]
struct___darwin_x86_thread_full_state64._fields_ = [
    ('__ss64', struct___darwin_x86_thread_state64),
    ('__ds', __uint64_t),
    ('__es', __uint64_t),
    ('__ss', __uint64_t),
    ('__gsbase', __uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 796
class struct___darwin_x86_float_state64(Structure):
    pass

struct___darwin_x86_float_state64.__slots__ = [
    '__fpu_reserved',
    '__fpu_fcw',
    '__fpu_fsw',
    '__fpu_ftw',
    '__fpu_rsrv1',
    '__fpu_fop',
    '__fpu_ip',
    '__fpu_cs',
    '__fpu_rsrv2',
    '__fpu_dp',
    '__fpu_ds',
    '__fpu_rsrv3',
    '__fpu_mxcsr',
    '__fpu_mxcsrmask',
    '__fpu_stmm0',
    '__fpu_stmm1',
    '__fpu_stmm2',
    '__fpu_stmm3',
    '__fpu_stmm4',
    '__fpu_stmm5',
    '__fpu_stmm6',
    '__fpu_stmm7',
    '__fpu_xmm0',
    '__fpu_xmm1',
    '__fpu_xmm2',
    '__fpu_xmm3',
    '__fpu_xmm4',
    '__fpu_xmm5',
    '__fpu_xmm6',
    '__fpu_xmm7',
    '__fpu_xmm8',
    '__fpu_xmm9',
    '__fpu_xmm10',
    '__fpu_xmm11',
    '__fpu_xmm12',
    '__fpu_xmm13',
    '__fpu_xmm14',
    '__fpu_xmm15',
    '__fpu_rsrv4',
    '__fpu_reserved1',
]
struct___darwin_x86_float_state64._fields_ = [
    ('__fpu_reserved', c_int * int(2)),
    ('__fpu_fcw', struct___darwin_fp_control),
    ('__fpu_fsw', struct___darwin_fp_status),
    ('__fpu_ftw', __uint8_t),
    ('__fpu_rsrv1', __uint8_t),
    ('__fpu_fop', __uint16_t),
    ('__fpu_ip', __uint32_t),
    ('__fpu_cs', __uint16_t),
    ('__fpu_rsrv2', __uint16_t),
    ('__fpu_dp', __uint32_t),
    ('__fpu_ds', __uint16_t),
    ('__fpu_rsrv3', __uint16_t),
    ('__fpu_mxcsr', __uint32_t),
    ('__fpu_mxcsrmask', __uint32_t),
    ('__fpu_stmm0', struct___darwin_mmst_reg),
    ('__fpu_stmm1', struct___darwin_mmst_reg),
    ('__fpu_stmm2', struct___darwin_mmst_reg),
    ('__fpu_stmm3', struct___darwin_mmst_reg),
    ('__fpu_stmm4', struct___darwin_mmst_reg),
    ('__fpu_stmm5', struct___darwin_mmst_reg),
    ('__fpu_stmm6', struct___darwin_mmst_reg),
    ('__fpu_stmm7', struct___darwin_mmst_reg),
    ('__fpu_xmm0', struct___darwin_xmm_reg),
    ('__fpu_xmm1', struct___darwin_xmm_reg),
    ('__fpu_xmm2', struct___darwin_xmm_reg),
    ('__fpu_xmm3', struct___darwin_xmm_reg),
    ('__fpu_xmm4', struct___darwin_xmm_reg),
    ('__fpu_xmm5', struct___darwin_xmm_reg),
    ('__fpu_xmm6', struct___darwin_xmm_reg),
    ('__fpu_xmm7', struct___darwin_xmm_reg),
    ('__fpu_xmm8', struct___darwin_xmm_reg),
    ('__fpu_xmm9', struct___darwin_xmm_reg),
    ('__fpu_xmm10', struct___darwin_xmm_reg),
    ('__fpu_xmm11', struct___darwin_xmm_reg),
    ('__fpu_xmm12', struct___darwin_xmm_reg),
    ('__fpu_xmm13', struct___darwin_xmm_reg),
    ('__fpu_xmm14', struct___darwin_xmm_reg),
    ('__fpu_xmm15', struct___darwin_xmm_reg),
    ('__fpu_rsrv4', c_char * int((6 * 16))),
    ('__fpu_reserved1', c_int),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 847
class struct___darwin_x86_avx_state64(Structure):
    pass

struct___darwin_x86_avx_state64.__slots__ = [
    '__fpu_reserved',
    '__fpu_fcw',
    '__fpu_fsw',
    '__fpu_ftw',
    '__fpu_rsrv1',
    '__fpu_fop',
    '__fpu_ip',
    '__fpu_cs',
    '__fpu_rsrv2',
    '__fpu_dp',
    '__fpu_ds',
    '__fpu_rsrv3',
    '__fpu_mxcsr',
    '__fpu_mxcsrmask',
    '__fpu_stmm0',
    '__fpu_stmm1',
    '__fpu_stmm2',
    '__fpu_stmm3',
    '__fpu_stmm4',
    '__fpu_stmm5',
    '__fpu_stmm6',
    '__fpu_stmm7',
    '__fpu_xmm0',
    '__fpu_xmm1',
    '__fpu_xmm2',
    '__fpu_xmm3',
    '__fpu_xmm4',
    '__fpu_xmm5',
    '__fpu_xmm6',
    '__fpu_xmm7',
    '__fpu_xmm8',
    '__fpu_xmm9',
    '__fpu_xmm10',
    '__fpu_xmm11',
    '__fpu_xmm12',
    '__fpu_xmm13',
    '__fpu_xmm14',
    '__fpu_xmm15',
    '__fpu_rsrv4',
    '__fpu_reserved1',
    '__avx_reserved1',
    '__fpu_ymmh0',
    '__fpu_ymmh1',
    '__fpu_ymmh2',
    '__fpu_ymmh3',
    '__fpu_ymmh4',
    '__fpu_ymmh5',
    '__fpu_ymmh6',
    '__fpu_ymmh7',
    '__fpu_ymmh8',
    '__fpu_ymmh9',
    '__fpu_ymmh10',
    '__fpu_ymmh11',
    '__fpu_ymmh12',
    '__fpu_ymmh13',
    '__fpu_ymmh14',
    '__fpu_ymmh15',
]
struct___darwin_x86_avx_state64._fields_ = [
    ('__fpu_reserved', c_int * int(2)),
    ('__fpu_fcw', struct___darwin_fp_control),
    ('__fpu_fsw', struct___darwin_fp_status),
    ('__fpu_ftw', __uint8_t),
    ('__fpu_rsrv1', __uint8_t),
    ('__fpu_fop', __uint16_t),
    ('__fpu_ip', __uint32_t),
    ('__fpu_cs', __uint16_t),
    ('__fpu_rsrv2', __uint16_t),
    ('__fpu_dp', __uint32_t),
    ('__fpu_ds', __uint16_t),
    ('__fpu_rsrv3', __uint16_t),
    ('__fpu_mxcsr', __uint32_t),
    ('__fpu_mxcsrmask', __uint32_t),
    ('__fpu_stmm0', struct___darwin_mmst_reg),
    ('__fpu_stmm1', struct___darwin_mmst_reg),
    ('__fpu_stmm2', struct___darwin_mmst_reg),
    ('__fpu_stmm3', struct___darwin_mmst_reg),
    ('__fpu_stmm4', struct___darwin_mmst_reg),
    ('__fpu_stmm5', struct___darwin_mmst_reg),
    ('__fpu_stmm6', struct___darwin_mmst_reg),
    ('__fpu_stmm7', struct___darwin_mmst_reg),
    ('__fpu_xmm0', struct___darwin_xmm_reg),
    ('__fpu_xmm1', struct___darwin_xmm_reg),
    ('__fpu_xmm2', struct___darwin_xmm_reg),
    ('__fpu_xmm3', struct___darwin_xmm_reg),
    ('__fpu_xmm4', struct___darwin_xmm_reg),
    ('__fpu_xmm5', struct___darwin_xmm_reg),
    ('__fpu_xmm6', struct___darwin_xmm_reg),
    ('__fpu_xmm7', struct___darwin_xmm_reg),
    ('__fpu_xmm8', struct___darwin_xmm_reg),
    ('__fpu_xmm9', struct___darwin_xmm_reg),
    ('__fpu_xmm10', struct___darwin_xmm_reg),
    ('__fpu_xmm11', struct___darwin_xmm_reg),
    ('__fpu_xmm12', struct___darwin_xmm_reg),
    ('__fpu_xmm13', struct___darwin_xmm_reg),
    ('__fpu_xmm14', struct___darwin_xmm_reg),
    ('__fpu_xmm15', struct___darwin_xmm_reg),
    ('__fpu_rsrv4', c_char * int((6 * 16))),
    ('__fpu_reserved1', c_int),
    ('__avx_reserved1', c_char * int(64)),
    ('__fpu_ymmh0', struct___darwin_xmm_reg),
    ('__fpu_ymmh1', struct___darwin_xmm_reg),
    ('__fpu_ymmh2', struct___darwin_xmm_reg),
    ('__fpu_ymmh3', struct___darwin_xmm_reg),
    ('__fpu_ymmh4', struct___darwin_xmm_reg),
    ('__fpu_ymmh5', struct___darwin_xmm_reg),
    ('__fpu_ymmh6', struct___darwin_xmm_reg),
    ('__fpu_ymmh7', struct___darwin_xmm_reg),
    ('__fpu_ymmh8', struct___darwin_xmm_reg),
    ('__fpu_ymmh9', struct___darwin_xmm_reg),
    ('__fpu_ymmh10', struct___darwin_xmm_reg),
    ('__fpu_ymmh11', struct___darwin_xmm_reg),
    ('__fpu_ymmh12', struct___darwin_xmm_reg),
    ('__fpu_ymmh13', struct___darwin_xmm_reg),
    ('__fpu_ymmh14', struct___darwin_xmm_reg),
    ('__fpu_ymmh15', struct___darwin_xmm_reg),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 915
class struct___darwin_x86_avx512_state64(Structure):
    pass

struct___darwin_x86_avx512_state64.__slots__ = [
    '__fpu_reserved',
    '__fpu_fcw',
    '__fpu_fsw',
    '__fpu_ftw',
    '__fpu_rsrv1',
    '__fpu_fop',
    '__fpu_ip',
    '__fpu_cs',
    '__fpu_rsrv2',
    '__fpu_dp',
    '__fpu_ds',
    '__fpu_rsrv3',
    '__fpu_mxcsr',
    '__fpu_mxcsrmask',
    '__fpu_stmm0',
    '__fpu_stmm1',
    '__fpu_stmm2',
    '__fpu_stmm3',
    '__fpu_stmm4',
    '__fpu_stmm5',
    '__fpu_stmm6',
    '__fpu_stmm7',
    '__fpu_xmm0',
    '__fpu_xmm1',
    '__fpu_xmm2',
    '__fpu_xmm3',
    '__fpu_xmm4',
    '__fpu_xmm5',
    '__fpu_xmm6',
    '__fpu_xmm7',
    '__fpu_xmm8',
    '__fpu_xmm9',
    '__fpu_xmm10',
    '__fpu_xmm11',
    '__fpu_xmm12',
    '__fpu_xmm13',
    '__fpu_xmm14',
    '__fpu_xmm15',
    '__fpu_rsrv4',
    '__fpu_reserved1',
    '__avx_reserved1',
    '__fpu_ymmh0',
    '__fpu_ymmh1',
    '__fpu_ymmh2',
    '__fpu_ymmh3',
    '__fpu_ymmh4',
    '__fpu_ymmh5',
    '__fpu_ymmh6',
    '__fpu_ymmh7',
    '__fpu_ymmh8',
    '__fpu_ymmh9',
    '__fpu_ymmh10',
    '__fpu_ymmh11',
    '__fpu_ymmh12',
    '__fpu_ymmh13',
    '__fpu_ymmh14',
    '__fpu_ymmh15',
    '__fpu_k0',
    '__fpu_k1',
    '__fpu_k2',
    '__fpu_k3',
    '__fpu_k4',
    '__fpu_k5',
    '__fpu_k6',
    '__fpu_k7',
    '__fpu_zmmh0',
    '__fpu_zmmh1',
    '__fpu_zmmh2',
    '__fpu_zmmh3',
    '__fpu_zmmh4',
    '__fpu_zmmh5',
    '__fpu_zmmh6',
    '__fpu_zmmh7',
    '__fpu_zmmh8',
    '__fpu_zmmh9',
    '__fpu_zmmh10',
    '__fpu_zmmh11',
    '__fpu_zmmh12',
    '__fpu_zmmh13',
    '__fpu_zmmh14',
    '__fpu_zmmh15',
    '__fpu_zmm16',
    '__fpu_zmm17',
    '__fpu_zmm18',
    '__fpu_zmm19',
    '__fpu_zmm20',
    '__fpu_zmm21',
    '__fpu_zmm22',
    '__fpu_zmm23',
    '__fpu_zmm24',
    '__fpu_zmm25',
    '__fpu_zmm26',
    '__fpu_zmm27',
    '__fpu_zmm28',
    '__fpu_zmm29',
    '__fpu_zmm30',
    '__fpu_zmm31',
]
struct___darwin_x86_avx512_state64._fields_ = [
    ('__fpu_reserved', c_int * int(2)),
    ('__fpu_fcw', struct___darwin_fp_control),
    ('__fpu_fsw', struct___darwin_fp_status),
    ('__fpu_ftw', __uint8_t),
    ('__fpu_rsrv1', __uint8_t),
    ('__fpu_fop', __uint16_t),
    ('__fpu_ip', __uint32_t),
    ('__fpu_cs', __uint16_t),
    ('__fpu_rsrv2', __uint16_t),
    ('__fpu_dp', __uint32_t),
    ('__fpu_ds', __uint16_t),
    ('__fpu_rsrv3', __uint16_t),
    ('__fpu_mxcsr', __uint32_t),
    ('__fpu_mxcsrmask', __uint32_t),
    ('__fpu_stmm0', struct___darwin_mmst_reg),
    ('__fpu_stmm1', struct___darwin_mmst_reg),
    ('__fpu_stmm2', struct___darwin_mmst_reg),
    ('__fpu_stmm3', struct___darwin_mmst_reg),
    ('__fpu_stmm4', struct___darwin_mmst_reg),
    ('__fpu_stmm5', struct___darwin_mmst_reg),
    ('__fpu_stmm6', struct___darwin_mmst_reg),
    ('__fpu_stmm7', struct___darwin_mmst_reg),
    ('__fpu_xmm0', struct___darwin_xmm_reg),
    ('__fpu_xmm1', struct___darwin_xmm_reg),
    ('__fpu_xmm2', struct___darwin_xmm_reg),
    ('__fpu_xmm3', struct___darwin_xmm_reg),
    ('__fpu_xmm4', struct___darwin_xmm_reg),
    ('__fpu_xmm5', struct___darwin_xmm_reg),
    ('__fpu_xmm6', struct___darwin_xmm_reg),
    ('__fpu_xmm7', struct___darwin_xmm_reg),
    ('__fpu_xmm8', struct___darwin_xmm_reg),
    ('__fpu_xmm9', struct___darwin_xmm_reg),
    ('__fpu_xmm10', struct___darwin_xmm_reg),
    ('__fpu_xmm11', struct___darwin_xmm_reg),
    ('__fpu_xmm12', struct___darwin_xmm_reg),
    ('__fpu_xmm13', struct___darwin_xmm_reg),
    ('__fpu_xmm14', struct___darwin_xmm_reg),
    ('__fpu_xmm15', struct___darwin_xmm_reg),
    ('__fpu_rsrv4', c_char * int((6 * 16))),
    ('__fpu_reserved1', c_int),
    ('__avx_reserved1', c_char * int(64)),
    ('__fpu_ymmh0', struct___darwin_xmm_reg),
    ('__fpu_ymmh1', struct___darwin_xmm_reg),
    ('__fpu_ymmh2', struct___darwin_xmm_reg),
    ('__fpu_ymmh3', struct___darwin_xmm_reg),
    ('__fpu_ymmh4', struct___darwin_xmm_reg),
    ('__fpu_ymmh5', struct___darwin_xmm_reg),
    ('__fpu_ymmh6', struct___darwin_xmm_reg),
    ('__fpu_ymmh7', struct___darwin_xmm_reg),
    ('__fpu_ymmh8', struct___darwin_xmm_reg),
    ('__fpu_ymmh9', struct___darwin_xmm_reg),
    ('__fpu_ymmh10', struct___darwin_xmm_reg),
    ('__fpu_ymmh11', struct___darwin_xmm_reg),
    ('__fpu_ymmh12', struct___darwin_xmm_reg),
    ('__fpu_ymmh13', struct___darwin_xmm_reg),
    ('__fpu_ymmh14', struct___darwin_xmm_reg),
    ('__fpu_ymmh15', struct___darwin_xmm_reg),
    ('__fpu_k0', struct___darwin_opmask_reg),
    ('__fpu_k1', struct___darwin_opmask_reg),
    ('__fpu_k2', struct___darwin_opmask_reg),
    ('__fpu_k3', struct___darwin_opmask_reg),
    ('__fpu_k4', struct___darwin_opmask_reg),
    ('__fpu_k5', struct___darwin_opmask_reg),
    ('__fpu_k6', struct___darwin_opmask_reg),
    ('__fpu_k7', struct___darwin_opmask_reg),
    ('__fpu_zmmh0', struct___darwin_ymm_reg),
    ('__fpu_zmmh1', struct___darwin_ymm_reg),
    ('__fpu_zmmh2', struct___darwin_ymm_reg),
    ('__fpu_zmmh3', struct___darwin_ymm_reg),
    ('__fpu_zmmh4', struct___darwin_ymm_reg),
    ('__fpu_zmmh5', struct___darwin_ymm_reg),
    ('__fpu_zmmh6', struct___darwin_ymm_reg),
    ('__fpu_zmmh7', struct___darwin_ymm_reg),
    ('__fpu_zmmh8', struct___darwin_ymm_reg),
    ('__fpu_zmmh9', struct___darwin_ymm_reg),
    ('__fpu_zmmh10', struct___darwin_ymm_reg),
    ('__fpu_zmmh11', struct___darwin_ymm_reg),
    ('__fpu_zmmh12', struct___darwin_ymm_reg),
    ('__fpu_zmmh13', struct___darwin_ymm_reg),
    ('__fpu_zmmh14', struct___darwin_ymm_reg),
    ('__fpu_zmmh15', struct___darwin_ymm_reg),
    ('__fpu_zmm16', struct___darwin_zmm_reg),
    ('__fpu_zmm17', struct___darwin_zmm_reg),
    ('__fpu_zmm18', struct___darwin_zmm_reg),
    ('__fpu_zmm19', struct___darwin_zmm_reg),
    ('__fpu_zmm20', struct___darwin_zmm_reg),
    ('__fpu_zmm21', struct___darwin_zmm_reg),
    ('__fpu_zmm22', struct___darwin_zmm_reg),
    ('__fpu_zmm23', struct___darwin_zmm_reg),
    ('__fpu_zmm24', struct___darwin_zmm_reg),
    ('__fpu_zmm25', struct___darwin_zmm_reg),
    ('__fpu_zmm26', struct___darwin_zmm_reg),
    ('__fpu_zmm27', struct___darwin_zmm_reg),
    ('__fpu_zmm28', struct___darwin_zmm_reg),
    ('__fpu_zmm29', struct___darwin_zmm_reg),
    ('__fpu_zmm30', struct___darwin_zmm_reg),
    ('__fpu_zmm31', struct___darwin_zmm_reg),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1254
class struct___darwin_x86_exception_state64(Structure):
    pass

struct___darwin_x86_exception_state64.__slots__ = [
    '__trapno',
    '__cpu',
    '__err',
    '__faultvaddr',
]
struct___darwin_x86_exception_state64._fields_ = [
    ('__trapno', __uint16_t),
    ('__cpu', __uint16_t),
    ('__err', __uint32_t),
    ('__faultvaddr', __uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1274
class struct___darwin_x86_debug_state64(Structure):
    pass

struct___darwin_x86_debug_state64.__slots__ = [
    '__dr0',
    '__dr1',
    '__dr2',
    '__dr3',
    '__dr4',
    '__dr5',
    '__dr6',
    '__dr7',
]
struct___darwin_x86_debug_state64._fields_ = [
    ('__dr0', __uint64_t),
    ('__dr1', __uint64_t),
    ('__dr2', __uint64_t),
    ('__dr3', __uint64_t),
    ('__dr4', __uint64_t),
    ('__dr5', __uint64_t),
    ('__dr6', __uint64_t),
    ('__dr7', __uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1302
class struct___darwin_x86_cpmu_state64(Structure):
    pass

struct___darwin_x86_cpmu_state64.__slots__ = [
    '__ctrs',
]
struct___darwin_x86_cpmu_state64._fields_ = [
    ('__ctrs', __uint64_t * int(16)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 41
class struct___darwin_mcontext32(Structure):
    pass

struct___darwin_mcontext32.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext32._fields_ = [
    ('__es', struct___darwin_i386_exception_state),
    ('__ss', struct___darwin_i386_thread_state),
    ('__fs', struct___darwin_i386_float_state),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 49
class struct___darwin_mcontext_avx32(Structure):
    pass

struct___darwin_mcontext_avx32.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext_avx32._fields_ = [
    ('__es', struct___darwin_i386_exception_state),
    ('__ss', struct___darwin_i386_thread_state),
    ('__fs', struct___darwin_i386_avx_state),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 58
class struct___darwin_mcontext_avx512_32(Structure):
    pass

struct___darwin_mcontext_avx512_32.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext_avx512_32._fields_ = [
    ('__es', struct___darwin_i386_exception_state),
    ('__ss', struct___darwin_i386_thread_state),
    ('__fs', struct___darwin_i386_avx512_state),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 99
class struct___darwin_mcontext64(Structure):
    pass

struct___darwin_mcontext64.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext64._fields_ = [
    ('__es', struct___darwin_x86_exception_state64),
    ('__ss', struct___darwin_x86_thread_state64),
    ('__fs', struct___darwin_x86_float_state64),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 107
class struct___darwin_mcontext64_full(Structure):
    pass

struct___darwin_mcontext64_full.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext64_full._fields_ = [
    ('__es', struct___darwin_x86_exception_state64),
    ('__ss', struct___darwin_x86_thread_full_state64),
    ('__fs', struct___darwin_x86_float_state64),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 115
class struct___darwin_mcontext_avx64(Structure):
    pass

struct___darwin_mcontext_avx64.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext_avx64._fields_ = [
    ('__es', struct___darwin_x86_exception_state64),
    ('__ss', struct___darwin_x86_thread_state64),
    ('__fs', struct___darwin_x86_avx_state64),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 123
class struct___darwin_mcontext_avx64_full(Structure):
    pass

struct___darwin_mcontext_avx64_full.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext_avx64_full._fields_ = [
    ('__es', struct___darwin_x86_exception_state64),
    ('__ss', struct___darwin_x86_thread_full_state64),
    ('__fs', struct___darwin_x86_avx_state64),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 132
class struct___darwin_mcontext_avx512_64(Structure):
    pass

struct___darwin_mcontext_avx512_64.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext_avx512_64._fields_ = [
    ('__es', struct___darwin_x86_exception_state64),
    ('__ss', struct___darwin_x86_thread_state64),
    ('__fs', struct___darwin_x86_avx512_state64),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 140
class struct___darwin_mcontext_avx512_64_full(Structure):
    pass

struct___darwin_mcontext_avx512_64_full.__slots__ = [
    '__es',
    '__ss',
    '__fs',
]
struct___darwin_mcontext_avx512_64_full._fields_ = [
    ('__es', struct___darwin_x86_exception_state64),
    ('__ss', struct___darwin_x86_thread_full_state64),
    ('__fs', struct___darwin_x86_avx512_state64),
]

mcontext_t = POINTER(struct___darwin_mcontext64)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 206

pthread_attr_t = __darwin_pthread_attr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_attr_t.h: 31

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigaltstack.h: 42
class struct___darwin_sigaltstack(Structure):
    pass

struct___darwin_sigaltstack.__slots__ = [
    'ss_sp',
    'ss_size',
    'ss_flags',
]
struct___darwin_sigaltstack._fields_ = [
    ('ss_sp', POINTER(None)),
    ('ss_size', __darwin_size_t),
    ('ss_flags', c_int),
]

stack_t = struct___darwin_sigaltstack# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigaltstack.h: 48

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_ucontext.h: 43
class struct___darwin_ucontext(Structure):
    pass

struct___darwin_ucontext.__slots__ = [
    'uc_onstack',
    'uc_sigmask',
    'uc_stack',
    'uc_link',
    'uc_mcsize',
    'uc_mcontext',
]
struct___darwin_ucontext._fields_ = [
    ('uc_onstack', c_int),
    ('uc_sigmask', __darwin_sigset_t),
    ('uc_stack', struct___darwin_sigaltstack),
    ('uc_link', POINTER(struct___darwin_ucontext)),
    ('uc_mcsize', __darwin_size_t),
    ('uc_mcontext', POINTER(struct___darwin_mcontext64)),
]

ucontext_t = struct___darwin_ucontext# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_ucontext.h: 57

sigset_t = __darwin_sigset_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigset_t.h: 31

size_t = __darwin_size_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h: 31

uid_t = __darwin_uid_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_uid_t.h: 31

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 158
class union_sigval(Union):
    pass

union_sigval.__slots__ = [
    'sival_int',
    'sival_ptr',
]
union_sigval._fields_ = [
    ('sival_int', c_int),
    ('sival_ptr', POINTER(None)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 168
class struct_sigevent(Structure):
    pass

struct_sigevent.__slots__ = [
    'sigev_notify',
    'sigev_signo',
    'sigev_value',
    'sigev_notify_function',
    'sigev_notify_attributes',
]
struct_sigevent._fields_ = [
    ('sigev_notify', c_int),
    ('sigev_signo', c_int),
    ('sigev_value', union_sigval),
    ('sigev_notify_function', CFUNCTYPE(UNCHECKED(None), union_sigval)),
    ('sigev_notify_attributes', POINTER(pthread_attr_t)),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 188
class struct___siginfo(Structure):
    pass

struct___siginfo.__slots__ = [
    'si_signo',
    'si_errno',
    'si_code',
    'si_pid',
    'si_uid',
    'si_status',
    'si_addr',
    'si_value',
    'si_band',
    '__pad',
]
struct___siginfo._fields_ = [
    ('si_signo', c_int),
    ('si_errno', c_int),
    ('si_code', c_int),
    ('si_pid', pid_t),
    ('si_uid', uid_t),
    ('si_status', c_int),
    ('si_addr', POINTER(None)),
    ('si_value', union_sigval),
    ('si_band', c_long),
    ('__pad', c_ulong * int(7)),
]

siginfo_t = struct___siginfo# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 188

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 269
class union___sigaction_u(Union):
    pass

union___sigaction_u.__slots__ = [
    '__sa_handler',
    '__sa_sigaction',
]
union___sigaction_u._fields_ = [
    ('__sa_handler', CFUNCTYPE(UNCHECKED(None), c_int)),
    ('__sa_sigaction', CFUNCTYPE(UNCHECKED(None), c_int, POINTER(struct___siginfo), POINTER(None))),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 276
class struct___sigaction(Structure):
    pass

struct___sigaction.__slots__ = [
    '__sigaction_u',
    'sa_tramp',
    'sa_mask',
    'sa_flags',
]
struct___sigaction._fields_ = [
    ('__sigaction_u', union___sigaction_u),
    ('sa_tramp', CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, c_int, POINTER(siginfo_t), POINTER(None))),
    ('sa_mask', sigset_t),
    ('sa_flags', c_int),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 286
class struct_sigaction(Structure):
    pass

struct_sigaction.__slots__ = [
    '__sigaction_u',
    'sa_mask',
    'sa_flags',
]
struct_sigaction._fields_ = [
    ('__sigaction_u', union___sigaction_u),
    ('sa_mask', sigset_t),
    ('sa_flags', c_int),
]

sig_t = CFUNCTYPE(UNCHECKED(None), c_int)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 331

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 348
class struct_sigvec(Structure):
    pass

struct_sigvec.__slots__ = [
    'sv_handler',
    'sv_mask',
    'sv_flags',
]
struct_sigvec._fields_ = [
    ('sv_handler', CFUNCTYPE(UNCHECKED(None), c_int)),
    ('sv_mask', c_int),
    ('sv_flags', c_int),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 367
class struct_sigstack(Structure):
    pass

struct_sigstack.__slots__ = [
    'ss_sp',
    'ss_onstack',
]
struct_sigstack._fields_ = [
    ('ss_sp', String),
    ('ss_onstack', c_int),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 390
if _libs["libomapi.so"].has("signal", "cdecl"):
    signal = _libs["libomapi.so"].get("signal", "cdecl")
    signal.argtypes = [c_int, CFUNCTYPE(UNCHECKED(None), c_int)]
    signal.restype = POINTER(CFUNCTYPE(UNCHECKED(None), c_int))

uint8_t = c_ubyte# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uint8_t.h: 31

uint16_t = c_ushort# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uint16_t.h: 31

uint32_t = c_uint# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uint32_t.h: 31

uint64_t = c_ulonglong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uint64_t.h: 31

int_least8_t = c_int8# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 29

int_least16_t = c_int16# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 30

int_least32_t = c_int32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 31

int_least64_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 32

uint_least8_t = uint8_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 33

uint_least16_t = uint16_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 34

uint_least32_t = uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 35

uint_least64_t = uint64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 36

int_fast8_t = c_int8# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 40

int_fast16_t = c_int16# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 41

int_fast32_t = c_int32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 42

int_fast64_t = c_int64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 43

uint_fast8_t = uint8_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 44

uint_fast16_t = uint16_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 45

uint_fast32_t = uint32_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 46

uint_fast64_t = uint64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 47

intmax_t = c_long# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_intmax_t.h: 32

uintmax_t = c_ulong# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types/_uintmax_t.h: 32

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_timeval.h: 34
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __darwin_time_t),
    ('tv_usec', __darwin_suseconds_t),
]

rlim_t = __uint64_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 89

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 152
class struct_rusage(Structure):
    pass

struct_rusage.__slots__ = [
    'ru_utime',
    'ru_stime',
    'ru_maxrss',
    'ru_ixrss',
    'ru_idrss',
    'ru_isrss',
    'ru_minflt',
    'ru_majflt',
    'ru_nswap',
    'ru_inblock',
    'ru_oublock',
    'ru_msgsnd',
    'ru_msgrcv',
    'ru_nsignals',
    'ru_nvcsw',
    'ru_nivcsw',
]
struct_rusage._fields_ = [
    ('ru_utime', struct_timeval),
    ('ru_stime', struct_timeval),
    ('ru_maxrss', c_long),
    ('ru_ixrss', c_long),
    ('ru_idrss', c_long),
    ('ru_isrss', c_long),
    ('ru_minflt', c_long),
    ('ru_majflt', c_long),
    ('ru_nswap', c_long),
    ('ru_inblock', c_long),
    ('ru_oublock', c_long),
    ('ru_msgsnd', c_long),
    ('ru_msgrcv', c_long),
    ('ru_nsignals', c_long),
    ('ru_nvcsw', c_long),
    ('ru_nivcsw', c_long),
]

rusage_info_t = POINTER(None)# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 200

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 202
class struct_rusage_info_v0(Structure):
    pass

struct_rusage_info_v0.__slots__ = [
    'ri_uuid',
    'ri_user_time',
    'ri_system_time',
    'ri_pkg_idle_wkups',
    'ri_interrupt_wkups',
    'ri_pageins',
    'ri_wired_size',
    'ri_resident_size',
    'ri_phys_footprint',
    'ri_proc_start_abstime',
    'ri_proc_exit_abstime',
]
struct_rusage_info_v0._fields_ = [
    ('ri_uuid', uint8_t * int(16)),
    ('ri_user_time', uint64_t),
    ('ri_system_time', uint64_t),
    ('ri_pkg_idle_wkups', uint64_t),
    ('ri_interrupt_wkups', uint64_t),
    ('ri_pageins', uint64_t),
    ('ri_wired_size', uint64_t),
    ('ri_resident_size', uint64_t),
    ('ri_phys_footprint', uint64_t),
    ('ri_proc_start_abstime', uint64_t),
    ('ri_proc_exit_abstime', uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 216
class struct_rusage_info_v1(Structure):
    pass

struct_rusage_info_v1.__slots__ = [
    'ri_uuid',
    'ri_user_time',
    'ri_system_time',
    'ri_pkg_idle_wkups',
    'ri_interrupt_wkups',
    'ri_pageins',
    'ri_wired_size',
    'ri_resident_size',
    'ri_phys_footprint',
    'ri_proc_start_abstime',
    'ri_proc_exit_abstime',
    'ri_child_user_time',
    'ri_child_system_time',
    'ri_child_pkg_idle_wkups',
    'ri_child_interrupt_wkups',
    'ri_child_pageins',
    'ri_child_elapsed_abstime',
]
struct_rusage_info_v1._fields_ = [
    ('ri_uuid', uint8_t * int(16)),
    ('ri_user_time', uint64_t),
    ('ri_system_time', uint64_t),
    ('ri_pkg_idle_wkups', uint64_t),
    ('ri_interrupt_wkups', uint64_t),
    ('ri_pageins', uint64_t),
    ('ri_wired_size', uint64_t),
    ('ri_resident_size', uint64_t),
    ('ri_phys_footprint', uint64_t),
    ('ri_proc_start_abstime', uint64_t),
    ('ri_proc_exit_abstime', uint64_t),
    ('ri_child_user_time', uint64_t),
    ('ri_child_system_time', uint64_t),
    ('ri_child_pkg_idle_wkups', uint64_t),
    ('ri_child_interrupt_wkups', uint64_t),
    ('ri_child_pageins', uint64_t),
    ('ri_child_elapsed_abstime', uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 236
class struct_rusage_info_v2(Structure):
    pass

struct_rusage_info_v2.__slots__ = [
    'ri_uuid',
    'ri_user_time',
    'ri_system_time',
    'ri_pkg_idle_wkups',
    'ri_interrupt_wkups',
    'ri_pageins',
    'ri_wired_size',
    'ri_resident_size',
    'ri_phys_footprint',
    'ri_proc_start_abstime',
    'ri_proc_exit_abstime',
    'ri_child_user_time',
    'ri_child_system_time',
    'ri_child_pkg_idle_wkups',
    'ri_child_interrupt_wkups',
    'ri_child_pageins',
    'ri_child_elapsed_abstime',
    'ri_diskio_bytesread',
    'ri_diskio_byteswritten',
]
struct_rusage_info_v2._fields_ = [
    ('ri_uuid', uint8_t * int(16)),
    ('ri_user_time', uint64_t),
    ('ri_system_time', uint64_t),
    ('ri_pkg_idle_wkups', uint64_t),
    ('ri_interrupt_wkups', uint64_t),
    ('ri_pageins', uint64_t),
    ('ri_wired_size', uint64_t),
    ('ri_resident_size', uint64_t),
    ('ri_phys_footprint', uint64_t),
    ('ri_proc_start_abstime', uint64_t),
    ('ri_proc_exit_abstime', uint64_t),
    ('ri_child_user_time', uint64_t),
    ('ri_child_system_time', uint64_t),
    ('ri_child_pkg_idle_wkups', uint64_t),
    ('ri_child_interrupt_wkups', uint64_t),
    ('ri_child_pageins', uint64_t),
    ('ri_child_elapsed_abstime', uint64_t),
    ('ri_diskio_bytesread', uint64_t),
    ('ri_diskio_byteswritten', uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 258
class struct_rusage_info_v3(Structure):
    pass

struct_rusage_info_v3.__slots__ = [
    'ri_uuid',
    'ri_user_time',
    'ri_system_time',
    'ri_pkg_idle_wkups',
    'ri_interrupt_wkups',
    'ri_pageins',
    'ri_wired_size',
    'ri_resident_size',
    'ri_phys_footprint',
    'ri_proc_start_abstime',
    'ri_proc_exit_abstime',
    'ri_child_user_time',
    'ri_child_system_time',
    'ri_child_pkg_idle_wkups',
    'ri_child_interrupt_wkups',
    'ri_child_pageins',
    'ri_child_elapsed_abstime',
    'ri_diskio_bytesread',
    'ri_diskio_byteswritten',
    'ri_cpu_time_qos_default',
    'ri_cpu_time_qos_maintenance',
    'ri_cpu_time_qos_background',
    'ri_cpu_time_qos_utility',
    'ri_cpu_time_qos_legacy',
    'ri_cpu_time_qos_user_initiated',
    'ri_cpu_time_qos_user_interactive',
    'ri_billed_system_time',
    'ri_serviced_system_time',
]
struct_rusage_info_v3._fields_ = [
    ('ri_uuid', uint8_t * int(16)),
    ('ri_user_time', uint64_t),
    ('ri_system_time', uint64_t),
    ('ri_pkg_idle_wkups', uint64_t),
    ('ri_interrupt_wkups', uint64_t),
    ('ri_pageins', uint64_t),
    ('ri_wired_size', uint64_t),
    ('ri_resident_size', uint64_t),
    ('ri_phys_footprint', uint64_t),
    ('ri_proc_start_abstime', uint64_t),
    ('ri_proc_exit_abstime', uint64_t),
    ('ri_child_user_time', uint64_t),
    ('ri_child_system_time', uint64_t),
    ('ri_child_pkg_idle_wkups', uint64_t),
    ('ri_child_interrupt_wkups', uint64_t),
    ('ri_child_pageins', uint64_t),
    ('ri_child_elapsed_abstime', uint64_t),
    ('ri_diskio_bytesread', uint64_t),
    ('ri_diskio_byteswritten', uint64_t),
    ('ri_cpu_time_qos_default', uint64_t),
    ('ri_cpu_time_qos_maintenance', uint64_t),
    ('ri_cpu_time_qos_background', uint64_t),
    ('ri_cpu_time_qos_utility', uint64_t),
    ('ri_cpu_time_qos_legacy', uint64_t),
    ('ri_cpu_time_qos_user_initiated', uint64_t),
    ('ri_cpu_time_qos_user_interactive', uint64_t),
    ('ri_billed_system_time', uint64_t),
    ('ri_serviced_system_time', uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 289
class struct_rusage_info_v4(Structure):
    pass

struct_rusage_info_v4.__slots__ = [
    'ri_uuid',
    'ri_user_time',
    'ri_system_time',
    'ri_pkg_idle_wkups',
    'ri_interrupt_wkups',
    'ri_pageins',
    'ri_wired_size',
    'ri_resident_size',
    'ri_phys_footprint',
    'ri_proc_start_abstime',
    'ri_proc_exit_abstime',
    'ri_child_user_time',
    'ri_child_system_time',
    'ri_child_pkg_idle_wkups',
    'ri_child_interrupt_wkups',
    'ri_child_pageins',
    'ri_child_elapsed_abstime',
    'ri_diskio_bytesread',
    'ri_diskio_byteswritten',
    'ri_cpu_time_qos_default',
    'ri_cpu_time_qos_maintenance',
    'ri_cpu_time_qos_background',
    'ri_cpu_time_qos_utility',
    'ri_cpu_time_qos_legacy',
    'ri_cpu_time_qos_user_initiated',
    'ri_cpu_time_qos_user_interactive',
    'ri_billed_system_time',
    'ri_serviced_system_time',
    'ri_logical_writes',
    'ri_lifetime_max_phys_footprint',
    'ri_instructions',
    'ri_cycles',
    'ri_billed_energy',
    'ri_serviced_energy',
    'ri_interval_max_phys_footprint',
    'ri_runnable_time',
]
struct_rusage_info_v4._fields_ = [
    ('ri_uuid', uint8_t * int(16)),
    ('ri_user_time', uint64_t),
    ('ri_system_time', uint64_t),
    ('ri_pkg_idle_wkups', uint64_t),
    ('ri_interrupt_wkups', uint64_t),
    ('ri_pageins', uint64_t),
    ('ri_wired_size', uint64_t),
    ('ri_resident_size', uint64_t),
    ('ri_phys_footprint', uint64_t),
    ('ri_proc_start_abstime', uint64_t),
    ('ri_proc_exit_abstime', uint64_t),
    ('ri_child_user_time', uint64_t),
    ('ri_child_system_time', uint64_t),
    ('ri_child_pkg_idle_wkups', uint64_t),
    ('ri_child_interrupt_wkups', uint64_t),
    ('ri_child_pageins', uint64_t),
    ('ri_child_elapsed_abstime', uint64_t),
    ('ri_diskio_bytesread', uint64_t),
    ('ri_diskio_byteswritten', uint64_t),
    ('ri_cpu_time_qos_default', uint64_t),
    ('ri_cpu_time_qos_maintenance', uint64_t),
    ('ri_cpu_time_qos_background', uint64_t),
    ('ri_cpu_time_qos_utility', uint64_t),
    ('ri_cpu_time_qos_legacy', uint64_t),
    ('ri_cpu_time_qos_user_initiated', uint64_t),
    ('ri_cpu_time_qos_user_interactive', uint64_t),
    ('ri_billed_system_time', uint64_t),
    ('ri_serviced_system_time', uint64_t),
    ('ri_logical_writes', uint64_t),
    ('ri_lifetime_max_phys_footprint', uint64_t),
    ('ri_instructions', uint64_t),
    ('ri_cycles', uint64_t),
    ('ri_billed_energy', uint64_t),
    ('ri_serviced_energy', uint64_t),
    ('ri_interval_max_phys_footprint', uint64_t),
    ('ri_runnable_time', uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 328
class struct_rusage_info_v5(Structure):
    pass

struct_rusage_info_v5.__slots__ = [
    'ri_uuid',
    'ri_user_time',
    'ri_system_time',
    'ri_pkg_idle_wkups',
    'ri_interrupt_wkups',
    'ri_pageins',
    'ri_wired_size',
    'ri_resident_size',
    'ri_phys_footprint',
    'ri_proc_start_abstime',
    'ri_proc_exit_abstime',
    'ri_child_user_time',
    'ri_child_system_time',
    'ri_child_pkg_idle_wkups',
    'ri_child_interrupt_wkups',
    'ri_child_pageins',
    'ri_child_elapsed_abstime',
    'ri_diskio_bytesread',
    'ri_diskio_byteswritten',
    'ri_cpu_time_qos_default',
    'ri_cpu_time_qos_maintenance',
    'ri_cpu_time_qos_background',
    'ri_cpu_time_qos_utility',
    'ri_cpu_time_qos_legacy',
    'ri_cpu_time_qos_user_initiated',
    'ri_cpu_time_qos_user_interactive',
    'ri_billed_system_time',
    'ri_serviced_system_time',
    'ri_logical_writes',
    'ri_lifetime_max_phys_footprint',
    'ri_instructions',
    'ri_cycles',
    'ri_billed_energy',
    'ri_serviced_energy',
    'ri_interval_max_phys_footprint',
    'ri_runnable_time',
    'ri_flags',
]
struct_rusage_info_v5._fields_ = [
    ('ri_uuid', uint8_t * int(16)),
    ('ri_user_time', uint64_t),
    ('ri_system_time', uint64_t),
    ('ri_pkg_idle_wkups', uint64_t),
    ('ri_interrupt_wkups', uint64_t),
    ('ri_pageins', uint64_t),
    ('ri_wired_size', uint64_t),
    ('ri_resident_size', uint64_t),
    ('ri_phys_footprint', uint64_t),
    ('ri_proc_start_abstime', uint64_t),
    ('ri_proc_exit_abstime', uint64_t),
    ('ri_child_user_time', uint64_t),
    ('ri_child_system_time', uint64_t),
    ('ri_child_pkg_idle_wkups', uint64_t),
    ('ri_child_interrupt_wkups', uint64_t),
    ('ri_child_pageins', uint64_t),
    ('ri_child_elapsed_abstime', uint64_t),
    ('ri_diskio_bytesread', uint64_t),
    ('ri_diskio_byteswritten', uint64_t),
    ('ri_cpu_time_qos_default', uint64_t),
    ('ri_cpu_time_qos_maintenance', uint64_t),
    ('ri_cpu_time_qos_background', uint64_t),
    ('ri_cpu_time_qos_utility', uint64_t),
    ('ri_cpu_time_qos_legacy', uint64_t),
    ('ri_cpu_time_qos_user_initiated', uint64_t),
    ('ri_cpu_time_qos_user_interactive', uint64_t),
    ('ri_billed_system_time', uint64_t),
    ('ri_serviced_system_time', uint64_t),
    ('ri_logical_writes', uint64_t),
    ('ri_lifetime_max_phys_footprint', uint64_t),
    ('ri_instructions', uint64_t),
    ('ri_cycles', uint64_t),
    ('ri_billed_energy', uint64_t),
    ('ri_serviced_energy', uint64_t),
    ('ri_interval_max_phys_footprint', uint64_t),
    ('ri_runnable_time', uint64_t),
    ('ri_flags', uint64_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 368
class struct_rusage_info_v6(Structure):
    pass

struct_rusage_info_v6.__slots__ = [
    'ri_uuid',
    'ri_user_time',
    'ri_system_time',
    'ri_pkg_idle_wkups',
    'ri_interrupt_wkups',
    'ri_pageins',
    'ri_wired_size',
    'ri_resident_size',
    'ri_phys_footprint',
    'ri_proc_start_abstime',
    'ri_proc_exit_abstime',
    'ri_child_user_time',
    'ri_child_system_time',
    'ri_child_pkg_idle_wkups',
    'ri_child_interrupt_wkups',
    'ri_child_pageins',
    'ri_child_elapsed_abstime',
    'ri_diskio_bytesread',
    'ri_diskio_byteswritten',
    'ri_cpu_time_qos_default',
    'ri_cpu_time_qos_maintenance',
    'ri_cpu_time_qos_background',
    'ri_cpu_time_qos_utility',
    'ri_cpu_time_qos_legacy',
    'ri_cpu_time_qos_user_initiated',
    'ri_cpu_time_qos_user_interactive',
    'ri_billed_system_time',
    'ri_serviced_system_time',
    'ri_logical_writes',
    'ri_lifetime_max_phys_footprint',
    'ri_instructions',
    'ri_cycles',
    'ri_billed_energy',
    'ri_serviced_energy',
    'ri_interval_max_phys_footprint',
    'ri_runnable_time',
    'ri_flags',
    'ri_user_ptime',
    'ri_system_ptime',
    'ri_pinstructions',
    'ri_pcycles',
    'ri_energy_nj',
    'ri_penergy_nj',
    'ri_reserved',
]
struct_rusage_info_v6._fields_ = [
    ('ri_uuid', uint8_t * int(16)),
    ('ri_user_time', uint64_t),
    ('ri_system_time', uint64_t),
    ('ri_pkg_idle_wkups', uint64_t),
    ('ri_interrupt_wkups', uint64_t),
    ('ri_pageins', uint64_t),
    ('ri_wired_size', uint64_t),
    ('ri_resident_size', uint64_t),
    ('ri_phys_footprint', uint64_t),
    ('ri_proc_start_abstime', uint64_t),
    ('ri_proc_exit_abstime', uint64_t),
    ('ri_child_user_time', uint64_t),
    ('ri_child_system_time', uint64_t),
    ('ri_child_pkg_idle_wkups', uint64_t),
    ('ri_child_interrupt_wkups', uint64_t),
    ('ri_child_pageins', uint64_t),
    ('ri_child_elapsed_abstime', uint64_t),
    ('ri_diskio_bytesread', uint64_t),
    ('ri_diskio_byteswritten', uint64_t),
    ('ri_cpu_time_qos_default', uint64_t),
    ('ri_cpu_time_qos_maintenance', uint64_t),
    ('ri_cpu_time_qos_background', uint64_t),
    ('ri_cpu_time_qos_utility', uint64_t),
    ('ri_cpu_time_qos_legacy', uint64_t),
    ('ri_cpu_time_qos_user_initiated', uint64_t),
    ('ri_cpu_time_qos_user_interactive', uint64_t),
    ('ri_billed_system_time', uint64_t),
    ('ri_serviced_system_time', uint64_t),
    ('ri_logical_writes', uint64_t),
    ('ri_lifetime_max_phys_footprint', uint64_t),
    ('ri_instructions', uint64_t),
    ('ri_cycles', uint64_t),
    ('ri_billed_energy', uint64_t),
    ('ri_serviced_energy', uint64_t),
    ('ri_interval_max_phys_footprint', uint64_t),
    ('ri_runnable_time', uint64_t),
    ('ri_flags', uint64_t),
    ('ri_user_ptime', uint64_t),
    ('ri_system_ptime', uint64_t),
    ('ri_pinstructions', uint64_t),
    ('ri_pcycles', uint64_t),
    ('ri_energy_nj', uint64_t),
    ('ri_penergy_nj', uint64_t),
    ('ri_reserved', uint64_t * int(14)),
]

rusage_info_current = struct_rusage_info_v6# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 415

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 459
class struct_rlimit(Structure):
    pass

struct_rlimit.__slots__ = [
    'rlim_cur',
    'rlim_max',
]
struct_rlimit._fields_ = [
    ('rlim_cur', rlim_t),
    ('rlim_max', rlim_t),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 494
class struct_proc_rlimit_control_wakeupmon(Structure):
    pass

struct_proc_rlimit_control_wakeupmon.__slots__ = [
    'wm_flags',
    'wm_rate',
]
struct_proc_rlimit_control_wakeupmon._fields_ = [
    ('wm_flags', uint32_t),
    ('wm_rate', c_int32),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 563
if _libs["libomapi.so"].has("getpriority", "cdecl"):
    getpriority = _libs["libomapi.so"].get("getpriority", "cdecl")
    getpriority.argtypes = [c_int, id_t]
    getpriority.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 565
if _libs["libomapi.so"].has("getiopolicy_np", "cdecl"):
    getiopolicy_np = _libs["libomapi.so"].get("getiopolicy_np", "cdecl")
    getiopolicy_np.argtypes = [c_int, c_int]
    getiopolicy_np.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 567
if _libs["libomapi.so"].has("getrlimit", "cdecl"):
    getrlimit = _libs["libomapi.so"].get("getrlimit", "cdecl")
    getrlimit.argtypes = [c_int, POINTER(struct_rlimit)]
    getrlimit.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 568
if _libs["libomapi.so"].has("getrusage", "cdecl"):
    getrusage = _libs["libomapi.so"].get("getrusage", "cdecl")
    getrusage.argtypes = [c_int, POINTER(struct_rusage)]
    getrusage.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 569
if _libs["libomapi.so"].has("setpriority", "cdecl"):
    setpriority = _libs["libomapi.so"].get("setpriority", "cdecl")
    setpriority.argtypes = [c_int, id_t, c_int]
    setpriority.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 571
if _libs["libomapi.so"].has("setiopolicy_np", "cdecl"):
    setiopolicy_np = _libs["libomapi.so"].get("setiopolicy_np", "cdecl")
    setiopolicy_np.argtypes = [c_int, c_int, c_int]
    setiopolicy_np.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 573
if _libs["libomapi.so"].has("setrlimit", "cdecl"):
    setrlimit = _libs["libomapi.so"].get("setrlimit", "cdecl")
    setrlimit.argtypes = [c_int, POINTER(struct_rlimit)]
    setrlimit.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 199
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'w_Termsig',
    'w_Coredump',
    'w_Retcode',
    'w_Filler',
]
struct_anon_3._fields_ = [
    ('w_Termsig', c_uint, 7),
    ('w_Coredump', c_uint, 1),
    ('w_Retcode', c_uint, 8),
    ('w_Filler', c_uint, 16),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 218
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'w_Stopval',
    'w_Stopsig',
    'w_Filler',
]
struct_anon_4._fields_ = [
    ('w_Stopval', c_uint, 8),
    ('w_Stopsig', c_uint, 8),
    ('w_Filler', c_uint, 16),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 194
class union_wait(Union):
    pass

union_wait.__slots__ = [
    'w_status',
    'w_T',
    'w_S',
]
union_wait._fields_ = [
    ('w_status', c_int),
    ('w_T', struct_anon_3),
    ('w_S', struct_anon_4),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 248
if _libs["libomapi.so"].has("wait", "cdecl"):
    wait = _libs["libomapi.so"].get("wait", "cdecl")
    wait.argtypes = [POINTER(c_int)]
    wait.restype = pid_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 249
if _libs["libomapi.so"].has("waitpid", "cdecl"):
    waitpid = _libs["libomapi.so"].get("waitpid", "cdecl")
    waitpid.argtypes = [pid_t, POINTER(c_int), c_int]
    waitpid.restype = pid_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 251
if _libs["libomapi.so"].has("waitid", "cdecl"):
    waitid = _libs["libomapi.so"].get("waitid", "cdecl")
    waitid.argtypes = [idtype_t, id_t, POINTER(siginfo_t), c_int]
    waitid.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 254
if _libs["libomapi.so"].has("wait3", "cdecl"):
    wait3 = _libs["libomapi.so"].get("wait3", "cdecl")
    wait3.argtypes = [POINTER(c_int), c_int, POINTER(struct_rusage)]
    wait3.restype = pid_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 255
if _libs["libomapi.so"].has("wait4", "cdecl"):
    wait4 = _libs["libomapi.so"].get("wait4", "cdecl")
    wait4.argtypes = [pid_t, POINTER(c_int), c_int, POINTER(struct_rusage)]
    wait4.restype = pid_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/alloca.h: 32
for _lib in _libs.values():
    if not _lib.has("alloca", "cdecl"):
        continue
    alloca = _lib.get("alloca", "cdecl")
    alloca.argtypes = [c_size_t]
    alloca.restype = POINTER(c_ubyte)
    alloca.errcheck = lambda v,*a : cast(v, c_void_p)
    break

ct_rune_t = __darwin_ct_rune_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_ct_rune_t.h: 32

rune_t = __darwin_rune_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_rune_t.h: 31

wchar_t = __darwin_wchar_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_wchar_t.h: 34

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 86
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'quot',
    'rem',
]
struct_anon_5._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]

div_t = struct_anon_5# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 86

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 91
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'quot',
    'rem',
]
struct_anon_6._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]

ldiv_t = struct_anon_6# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 91

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 97
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'quot',
    'rem',
]
struct_anon_7._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]

lldiv_t = struct_anon_7# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 97

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 118
try:
    __mb_cur_max = (c_int).in_dll(_libs["libomapi.so"], "__mb_cur_max")
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h: 40
if _libs["libomapi.so"].has("malloc", "cdecl"):
    malloc = _libs["libomapi.so"].get("malloc", "cdecl")
    malloc.argtypes = [c_size_t]
    malloc.restype = POINTER(c_ubyte)
    malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h: 41
if _libs["libomapi.so"].has("calloc", "cdecl"):
    calloc = _libs["libomapi.so"].get("calloc", "cdecl")
    calloc.argtypes = [c_size_t, c_size_t]
    calloc.restype = POINTER(c_ubyte)
    calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h: 42
if _libs["libomapi.so"].has("free", "cdecl"):
    free = _libs["libomapi.so"].get("free", "cdecl")
    free.argtypes = [POINTER(None)]
    free.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h: 43
if _libs["libomapi.so"].has("realloc", "cdecl"):
    realloc = _libs["libomapi.so"].get("realloc", "cdecl")
    realloc.argtypes = [POINTER(None), c_size_t]
    realloc.restype = POINTER(c_ubyte)
    realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h: 45
if _libs["libomapi.so"].has("valloc", "cdecl"):
    valloc = _libs["libomapi.so"].get("valloc", "cdecl")
    valloc.argtypes = [c_size_t]
    valloc.restype = POINTER(c_ubyte)
    valloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h: 50
if _libs["libomapi.so"].has("aligned_alloc", "cdecl"):
    aligned_alloc = _libs["libomapi.so"].get("aligned_alloc", "cdecl")
    aligned_alloc.argtypes = [c_size_t, c_size_t]
    aligned_alloc.restype = POINTER(c_ubyte)
    aligned_alloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h: 52
if _libs["libomapi.so"].has("posix_memalign", "cdecl"):
    posix_memalign = _libs["libomapi.so"].get("posix_memalign", "cdecl")
    posix_memalign.argtypes = [POINTER(POINTER(None)), c_size_t, c_size_t]
    posix_memalign.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 131
if _libs["libomapi.so"].has("abort", "cdecl"):
    abort = _libs["libomapi.so"].get("abort", "cdecl")
    abort.argtypes = []
    abort.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 132
if _libs["libomapi.so"].has("abs", "cdecl"):
    abs = _libs["libomapi.so"].get("abs", "cdecl")
    abs.argtypes = [c_int]
    abs.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 133
if _libs["libomapi.so"].has("atexit", "cdecl"):
    atexit = _libs["libomapi.so"].get("atexit", "cdecl")
    atexit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    atexit.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 134
if _libs["libomapi.so"].has("atof", "cdecl"):
    atof = _libs["libomapi.so"].get("atof", "cdecl")
    atof.argtypes = [String]
    atof.restype = c_double

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 135
if _libs["libomapi.so"].has("atoi", "cdecl"):
    atoi = _libs["libomapi.so"].get("atoi", "cdecl")
    atoi.argtypes = [String]
    atoi.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 136
if _libs["libomapi.so"].has("atol", "cdecl"):
    atol = _libs["libomapi.so"].get("atol", "cdecl")
    atol.argtypes = [String]
    atol.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 139
if _libs["libomapi.so"].has("atoll", "cdecl"):
    atoll = _libs["libomapi.so"].get("atoll", "cdecl")
    atoll.argtypes = [String]
    atoll.restype = c_longlong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 141
if _libs["libomapi.so"].has("bsearch", "cdecl"):
    bsearch = _libs["libomapi.so"].get("bsearch", "cdecl")
    bsearch.argtypes = [POINTER(None), POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    bsearch.restype = POINTER(c_ubyte)
    bsearch.errcheck = lambda v,*a : cast(v, c_void_p)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 144
if _libs["libomapi.so"].has("div", "cdecl"):
    div = _libs["libomapi.so"].get("div", "cdecl")
    div.argtypes = [c_int, c_int]
    div.restype = div_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 145
if _libs["libomapi.so"].has("exit", "cdecl"):
    exit = _libs["libomapi.so"].get("exit", "cdecl")
    exit.argtypes = [c_int]
    exit.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 147
if _libs["libomapi.so"].has("getenv", "cdecl"):
    getenv = _libs["libomapi.so"].get("getenv", "cdecl")
    getenv.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getenv.restype = ReturnString
    else:
        getenv.restype = String
        getenv.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 148
if _libs["libomapi.so"].has("labs", "cdecl"):
    labs = _libs["libomapi.so"].get("labs", "cdecl")
    labs.argtypes = [c_long]
    labs.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 149
if _libs["libomapi.so"].has("ldiv", "cdecl"):
    ldiv = _libs["libomapi.so"].get("ldiv", "cdecl")
    ldiv.argtypes = [c_long, c_long]
    ldiv.restype = ldiv_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 152
if _libs["libomapi.so"].has("llabs", "cdecl"):
    llabs = _libs["libomapi.so"].get("llabs", "cdecl")
    llabs.argtypes = [c_longlong]
    llabs.restype = c_longlong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 153
if _libs["libomapi.so"].has("lldiv", "cdecl"):
    lldiv = _libs["libomapi.so"].get("lldiv", "cdecl")
    lldiv.argtypes = [c_longlong, c_longlong]
    lldiv.restype = lldiv_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 156
if _libs["libomapi.so"].has("mblen", "cdecl"):
    mblen = _libs["libomapi.so"].get("mblen", "cdecl")
    mblen.argtypes = [String, c_size_t]
    mblen.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 157
if _libs["libomapi.so"].has("mbstowcs", "cdecl"):
    mbstowcs = _libs["libomapi.so"].get("mbstowcs", "cdecl")
    mbstowcs.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbstowcs.restype = c_size_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 158
if _libs["libomapi.so"].has("mbtowc", "cdecl"):
    mbtowc = _libs["libomapi.so"].get("mbtowc", "cdecl")
    mbtowc.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbtowc.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 160
if _libs["libomapi.so"].has("qsort", "cdecl"):
    qsort = _libs["libomapi.so"].get("qsort", "cdecl")
    qsort.argtypes = [POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    qsort.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 162
if _libs["libomapi.so"].has("rand", "cdecl"):
    rand = _libs["libomapi.so"].get("rand", "cdecl")
    rand.argtypes = []
    rand.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 164
if _libs["libomapi.so"].has("srand", "cdecl"):
    srand = _libs["libomapi.so"].get("srand", "cdecl")
    srand.argtypes = [c_uint]
    srand.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 165
if _libs["libomapi.so"].has("strtod", "cdecl"):
    strtod = _libs["libomapi.so"].get("strtod", "cdecl")
    strtod.argtypes = [String, POINTER(POINTER(c_char))]
    strtod.restype = c_double

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 166
if _libs["libomapi.so"].has("strtof", "cdecl"):
    strtof = _libs["libomapi.so"].get("strtof", "cdecl")
    strtof.argtypes = [String, POINTER(POINTER(c_char))]
    strtof.restype = c_float

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 167
if _libs["libomapi.so"].has("strtol", "cdecl"):
    strtol = _libs["libomapi.so"].get("strtol", "cdecl")
    strtol.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtol.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 169
if _libs["libomapi.so"].has("strtold", "cdecl"):
    strtold = _libs["libomapi.so"].get("strtold", "cdecl")
    strtold.argtypes = [String, POINTER(POINTER(c_char))]
    strtold.restype = c_longdouble

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 172
if _libs["libomapi.so"].has("strtoll", "cdecl"):
    strtoll = _libs["libomapi.so"].get("strtoll", "cdecl")
    strtoll.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoll.restype = c_longlong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 175
if _libs["libomapi.so"].has("strtoul", "cdecl"):
    strtoul = _libs["libomapi.so"].get("strtoul", "cdecl")
    strtoul.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoul.restype = c_ulong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 178
if _libs["libomapi.so"].has("strtoull", "cdecl"):
    strtoull = _libs["libomapi.so"].get("strtoull", "cdecl")
    strtoull.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoull.restype = c_ulonglong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 184
if _libs["libomapi.so"].has("system", "cdecl"):
    system = _libs["libomapi.so"].get("system", "cdecl")
    system.argtypes = [String]
    system.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 187
if _libs["libomapi.so"].has("wcstombs", "cdecl"):
    wcstombs = _libs["libomapi.so"].get("wcstombs", "cdecl")
    wcstombs.argtypes = [String, POINTER(c_wchar), c_size_t]
    wcstombs.restype = c_size_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 188
if _libs["libomapi.so"].has("wctomb", "cdecl"):
    wctomb = _libs["libomapi.so"].get("wctomb", "cdecl")
    wctomb.argtypes = [String, c_wchar]
    wctomb.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 191
if _libs["libomapi.so"].has("_Exit", "cdecl"):
    _Exit = _libs["libomapi.so"].get("_Exit", "cdecl")
    _Exit.argtypes = [c_int]
    _Exit.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 192
if _libs["libomapi.so"].has("a64l", "cdecl"):
    a64l = _libs["libomapi.so"].get("a64l", "cdecl")
    a64l.argtypes = [String]
    a64l.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 193
if _libs["libomapi.so"].has("drand48", "cdecl"):
    drand48 = _libs["libomapi.so"].get("drand48", "cdecl")
    drand48.argtypes = []
    drand48.restype = c_double

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 194
if _libs["libomapi.so"].has("ecvt", "cdecl"):
    ecvt = _libs["libomapi.so"].get("ecvt", "cdecl")
    ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecvt.restype = ReturnString
    else:
        ecvt.restype = String
        ecvt.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 195
if _libs["libomapi.so"].has("erand48", "cdecl"):
    erand48 = _libs["libomapi.so"].get("erand48", "cdecl")
    erand48.argtypes = [c_ushort * int(3)]
    erand48.restype = c_double

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 196
if _libs["libomapi.so"].has("fcvt", "cdecl"):
    fcvt = _libs["libomapi.so"].get("fcvt", "cdecl")
    fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        fcvt.restype = ReturnString
    else:
        fcvt.restype = String
        fcvt.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 197
if _libs["libomapi.so"].has("gcvt", "cdecl"):
    gcvt = _libs["libomapi.so"].get("gcvt", "cdecl")
    gcvt.argtypes = [c_double, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        gcvt.restype = ReturnString
    else:
        gcvt.restype = String
        gcvt.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 198
if _libs["libomapi.so"].has("getsubopt", "cdecl"):
    getsubopt = _libs["libomapi.so"].get("getsubopt", "cdecl")
    getsubopt.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    getsubopt.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 199
if _libs["libomapi.so"].has("grantpt", "cdecl"):
    grantpt = _libs["libomapi.so"].get("grantpt", "cdecl")
    grantpt.argtypes = [c_int]
    grantpt.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 201
if _libs["libomapi.so"].has("initstate", "cdecl"):
    initstate = _libs["libomapi.so"].get("initstate", "cdecl")
    initstate.argtypes = [c_uint, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        initstate.restype = ReturnString
    else:
        initstate.restype = String
        initstate.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 205
if _libs["libomapi.so"].has("jrand48", "cdecl"):
    jrand48 = _libs["libomapi.so"].get("jrand48", "cdecl")
    jrand48.argtypes = [c_ushort * int(3)]
    jrand48.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 206
if _libs["libomapi.so"].has("l64a", "cdecl"):
    l64a = _libs["libomapi.so"].get("l64a", "cdecl")
    l64a.argtypes = [c_long]
    if sizeof(c_int) == sizeof(c_void_p):
        l64a.restype = ReturnString
    else:
        l64a.restype = String
        l64a.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 207
if _libs["libomapi.so"].has("lcong48", "cdecl"):
    lcong48 = _libs["libomapi.so"].get("lcong48", "cdecl")
    lcong48.argtypes = [c_ushort * int(7)]
    lcong48.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 208
if _libs["libomapi.so"].has("lrand48", "cdecl"):
    lrand48 = _libs["libomapi.so"].get("lrand48", "cdecl")
    lrand48.argtypes = []
    lrand48.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 212
if _libs["libomapi.so"].has("mktemp", "cdecl"):
    mktemp = _libs["libomapi.so"].get("mktemp", "cdecl")
    mktemp.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mktemp.restype = ReturnString
    else:
        mktemp.restype = String
        mktemp.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 213
if _libs["libomapi.so"].has("mkstemp", "cdecl"):
    mkstemp = _libs["libomapi.so"].get("mkstemp", "cdecl")
    mkstemp.argtypes = [String]
    mkstemp.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 214
if _libs["libomapi.so"].has("mrand48", "cdecl"):
    mrand48 = _libs["libomapi.so"].get("mrand48", "cdecl")
    mrand48.argtypes = []
    mrand48.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 215
if _libs["libomapi.so"].has("nrand48", "cdecl"):
    nrand48 = _libs["libomapi.so"].get("nrand48", "cdecl")
    nrand48.argtypes = [c_ushort * int(3)]
    nrand48.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 216
if _libs["libomapi.so"].has("posix_openpt", "cdecl"):
    posix_openpt = _libs["libomapi.so"].get("posix_openpt", "cdecl")
    posix_openpt.argtypes = [c_int]
    posix_openpt.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 217
if _libs["libomapi.so"].has("ptsname", "cdecl"):
    ptsname = _libs["libomapi.so"].get("ptsname", "cdecl")
    ptsname.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ptsname.restype = ReturnString
    else:
        ptsname.restype = String
        ptsname.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 223
if _libs["libomapi.so"].has("putenv", "cdecl"):
    putenv = _libs["libomapi.so"].get("putenv", "cdecl")
    putenv.argtypes = [String]
    putenv.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 224
if _libs["libomapi.so"].has("random", "cdecl"):
    random = _libs["libomapi.so"].get("random", "cdecl")
    random.argtypes = []
    random.restype = c_long

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 225
if _libs["libomapi.so"].has("rand_r", "cdecl"):
    rand_r = _libs["libomapi.so"].get("rand_r", "cdecl")
    rand_r.argtypes = [POINTER(c_uint)]
    rand_r.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 227
if _libs["libomapi.so"].has("realpath", "cdecl"):
    realpath = _libs["libomapi.so"].get("realpath", "cdecl")
    realpath.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        realpath.restype = ReturnString
    else:
        realpath.restype = String
        realpath.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 232
if _libs["libomapi.so"].has("seed48", "cdecl"):
    seed48 = _libs["libomapi.so"].get("seed48", "cdecl")
    seed48.argtypes = [c_ushort * int(3)]
    seed48.restype = POINTER(c_ushort)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 233
if _libs["libomapi.so"].has("setenv", "cdecl"):
    setenv = _libs["libomapi.so"].get("setenv", "cdecl")
    setenv.argtypes = [String, String, c_int]
    setenv.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 235
if _libs["libomapi.so"].has("setkey", "cdecl"):
    setkey = _libs["libomapi.so"].get("setkey", "cdecl")
    setkey.argtypes = [String]
    setkey.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 239
if _libs["libomapi.so"].has("setstate", "cdecl"):
    setstate = _libs["libomapi.so"].get("setstate", "cdecl")
    setstate.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        setstate.restype = ReturnString
    else:
        setstate.restype = String
        setstate.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 240
if _libs["libomapi.so"].has("srand48", "cdecl"):
    srand48 = _libs["libomapi.so"].get("srand48", "cdecl")
    srand48.argtypes = [c_long]
    srand48.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 242
if _libs["libomapi.so"].has("srandom", "cdecl"):
    srandom = _libs["libomapi.so"].get("srandom", "cdecl")
    srandom.argtypes = [c_uint]
    srandom.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 246
if _libs["libomapi.so"].has("unlockpt", "cdecl"):
    unlockpt = _libs["libomapi.so"].get("unlockpt", "cdecl")
    unlockpt.argtypes = [c_int]
    unlockpt.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 248
if _libs["libomapi.so"].has("unsetenv", "cdecl"):
    unsetenv = _libs["libomapi.so"].get("unsetenv", "cdecl")
    unsetenv.argtypes = [String]
    unsetenv.restype = c_int

dev_t = __darwin_dev_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_dev_t.h: 31

mode_t = __darwin_mode_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_mode_t.h: 31

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 260
if _libs["libomapi.so"].has("arc4random", "cdecl"):
    arc4random = _libs["libomapi.so"].get("arc4random", "cdecl")
    arc4random.argtypes = []
    arc4random.restype = uint32_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 261
if _libs["libomapi.so"].has("arc4random_addrandom", "cdecl"):
    arc4random_addrandom = _libs["libomapi.so"].get("arc4random_addrandom", "cdecl")
    arc4random_addrandom.argtypes = [POINTER(c_ubyte), c_int]
    arc4random_addrandom.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 266
if _libs["libomapi.so"].has("arc4random_buf", "cdecl"):
    arc4random_buf = _libs["libomapi.so"].get("arc4random_buf", "cdecl")
    arc4random_buf.argtypes = [POINTER(None), c_size_t]
    arc4random_buf.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 267
if _libs["libomapi.so"].has("arc4random_stir", "cdecl"):
    arc4random_stir = _libs["libomapi.so"].get("arc4random_stir", "cdecl")
    arc4random_stir.argtypes = []
    arc4random_stir.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 269
if _libs["libomapi.so"].has("arc4random_uniform", "cdecl"):
    arc4random_uniform = _libs["libomapi.so"].get("arc4random_uniform", "cdecl")
    arc4random_uniform.argtypes = [uint32_t]
    arc4random_uniform.restype = uint32_t

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 286
if _libs["libomapi.so"].has("cgetcap", "cdecl"):
    cgetcap = _libs["libomapi.so"].get("cgetcap", "cdecl")
    cgetcap.argtypes = [String, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        cgetcap.restype = ReturnString
    else:
        cgetcap.restype = String
        cgetcap.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 287
if _libs["libomapi.so"].has("cgetclose", "cdecl"):
    cgetclose = _libs["libomapi.so"].get("cgetclose", "cdecl")
    cgetclose.argtypes = []
    cgetclose.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 288
if _libs["libomapi.so"].has("cgetent", "cdecl"):
    cgetent = _libs["libomapi.so"].get("cgetent", "cdecl")
    cgetent.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), String]
    cgetent.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 289
if _libs["libomapi.so"].has("cgetfirst", "cdecl"):
    cgetfirst = _libs["libomapi.so"].get("cgetfirst", "cdecl")
    cgetfirst.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    cgetfirst.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 290
if _libs["libomapi.so"].has("cgetmatch", "cdecl"):
    cgetmatch = _libs["libomapi.so"].get("cgetmatch", "cdecl")
    cgetmatch.argtypes = [String, String]
    cgetmatch.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 291
if _libs["libomapi.so"].has("cgetnext", "cdecl"):
    cgetnext = _libs["libomapi.so"].get("cgetnext", "cdecl")
    cgetnext.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    cgetnext.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 292
if _libs["libomapi.so"].has("cgetnum", "cdecl"):
    cgetnum = _libs["libomapi.so"].get("cgetnum", "cdecl")
    cgetnum.argtypes = [String, String, POINTER(c_long)]
    cgetnum.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 293
if _libs["libomapi.so"].has("cgetset", "cdecl"):
    cgetset = _libs["libomapi.so"].get("cgetset", "cdecl")
    cgetset.argtypes = [String]
    cgetset.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 294
if _libs["libomapi.so"].has("cgetstr", "cdecl"):
    cgetstr = _libs["libomapi.so"].get("cgetstr", "cdecl")
    cgetstr.argtypes = [String, String, POINTER(POINTER(c_char))]
    cgetstr.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 295
if _libs["libomapi.so"].has("cgetustr", "cdecl"):
    cgetustr = _libs["libomapi.so"].get("cgetustr", "cdecl")
    cgetustr.argtypes = [String, String, POINTER(POINTER(c_char))]
    cgetustr.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 297
if _libs["libomapi.so"].has("daemon", "cdecl"):
    daemon = _libs["libomapi.so"].get("daemon", "cdecl")
    daemon.argtypes = [c_int, c_int]
    daemon.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 298
if _libs["libomapi.so"].has("devname", "cdecl"):
    devname = _libs["libomapi.so"].get("devname", "cdecl")
    devname.argtypes = [dev_t, mode_t]
    if sizeof(c_int) == sizeof(c_void_p):
        devname.restype = ReturnString
    else:
        devname.restype = String
        devname.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 299
if _libs["libomapi.so"].has("devname_r", "cdecl"):
    devname_r = _libs["libomapi.so"].get("devname_r", "cdecl")
    devname_r.argtypes = [dev_t, mode_t, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        devname_r.restype = ReturnString
    else:
        devname_r.restype = String
        devname_r.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 300
if _libs["libomapi.so"].has("getbsize", "cdecl"):
    getbsize = _libs["libomapi.so"].get("getbsize", "cdecl")
    getbsize.argtypes = [POINTER(c_int), POINTER(c_long)]
    if sizeof(c_int) == sizeof(c_void_p):
        getbsize.restype = ReturnString
    else:
        getbsize.restype = String
        getbsize.errcheck = ReturnString

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 301
if _libs["libomapi.so"].has("getloadavg", "cdecl"):
    getloadavg = _libs["libomapi.so"].get("getloadavg", "cdecl")
    getloadavg.argtypes = [POINTER(c_double), c_int]
    getloadavg.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 303
if _libs["libomapi.so"].has("getprogname", "cdecl"):
    getprogname = _libs["libomapi.so"].get("getprogname", "cdecl")
    getprogname.argtypes = []
    getprogname.restype = c_char_p

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 304
if _libs["libomapi.so"].has("setprogname", "cdecl"):
    setprogname = _libs["libomapi.so"].get("setprogname", "cdecl")
    setprogname.argtypes = [String]
    setprogname.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 314
if _libs["libomapi.so"].has("heapsort", "cdecl"):
    heapsort = _libs["libomapi.so"].get("heapsort", "cdecl")
    heapsort.argtypes = [POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    heapsort.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 321
if _libs["libomapi.so"].has("mergesort", "cdecl"):
    mergesort = _libs["libomapi.so"].get("mergesort", "cdecl")
    mergesort.argtypes = [POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    mergesort.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 328
if _libs["libomapi.so"].has("psort", "cdecl"):
    psort = _libs["libomapi.so"].get("psort", "cdecl")
    psort.argtypes = [POINTER(None), c_size_t, c_size_t, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    psort.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 336
if _libs["libomapi.so"].has("psort_r", "cdecl"):
    psort_r = _libs["libomapi.so"].get("psort_r", "cdecl")
    psort_r.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), POINTER(None))]
    psort_r.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 344
if _libs["libomapi.so"].has("qsort_r", "cdecl"):
    qsort_r = _libs["libomapi.so"].get("qsort_r", "cdecl")
    qsort_r.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), POINTER(None))]
    qsort_r.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 346
if _libs["libomapi.so"].has("radixsort", "cdecl"):
    radixsort = _libs["libomapi.so"].get("radixsort", "cdecl")
    radixsort.argtypes = [POINTER(POINTER(c_ubyte)), c_int, POINTER(c_ubyte), c_uint]
    radixsort.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 348
if _libs["libomapi.so"].has("rpmatch", "cdecl"):
    rpmatch = _libs["libomapi.so"].get("rpmatch", "cdecl")
    rpmatch.argtypes = [String]
    rpmatch.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 350
if _libs["libomapi.so"].has("sradixsort", "cdecl"):
    sradixsort = _libs["libomapi.so"].get("sradixsort", "cdecl")
    sradixsort.argtypes = [POINTER(POINTER(c_ubyte)), c_int, POINTER(c_ubyte), c_uint]
    sradixsort.restype = c_int

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 352
if _libs["libomapi.so"].has("sranddev", "cdecl"):
    sranddev = _libs["libomapi.so"].get("sranddev", "cdecl")
    sranddev.argtypes = []
    sranddev.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 353
if _libs["libomapi.so"].has("srandomdev", "cdecl"):
    srandomdev = _libs["libomapi.so"].get("srandomdev", "cdecl")
    srandomdev.argtypes = []
    srandomdev.restype = None

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 354
if _libs["libomapi.so"].has("reallocf", "cdecl"):
    reallocf = _libs["libomapi.so"].get("reallocf", "cdecl")
    reallocf.argtypes = [POINTER(None), c_size_t]
    reallocf.restype = POINTER(c_ubyte)
    reallocf.errcheck = lambda v,*a : cast(v, c_void_p)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 356
if _libs["libomapi.so"].has("strtonum", "cdecl"):
    strtonum = _libs["libomapi.so"].get("strtonum", "cdecl")
    strtonum.argtypes = [String, c_longlong, c_longlong, POINTER(POINTER(c_char))]
    strtonum.restype = c_longlong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 360
if _libs["libomapi.so"].has("strtoq", "cdecl"):
    strtoq = _libs["libomapi.so"].get("strtoq", "cdecl")
    strtoq.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoq.restype = c_longlong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 362
if _libs["libomapi.so"].has("strtouq", "cdecl"):
    strtouq = _libs["libomapi.so"].get("strtouq", "cdecl")
    strtouq.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtouq.restype = c_ulonglong

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 364
try:
    suboptarg = (String).in_dll(_libs["libomapi.so"], "suboptarg")
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 242
if _libs["libomapi.so"].has("OmStartup", "cdecl"):
    OmStartup = _libs["libomapi.so"].get("OmStartup", "cdecl")
    OmStartup.argtypes = [c_int]
    OmStartup.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 253
if _libs["libomapi.so"].has("OmShutdown", "cdecl"):
    OmShutdown = _libs["libomapi.so"].get("OmShutdown", "cdecl")
    OmShutdown.argtypes = []
    OmShutdown.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 263
if _libs["libomapi.so"].has("OmSetLogStream", "cdecl"):
    OmSetLogStream = _libs["libomapi.so"].get("OmSetLogStream", "cdecl")
    OmSetLogStream.argtypes = [c_int]
    OmSetLogStream.restype = c_int

OmLogCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 273

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 283
if _libs["libomapi.so"].has("OmSetLogCallback", "cdecl"):
    OmSetLogCallback = _libs["libomapi.so"].get("OmSetLogCallback", "cdecl")
    OmSetLogCallback.argtypes = [OmLogCallback, POINTER(None)]
    OmSetLogCallback.restype = c_int

enum_anon_8 = c_int# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 294

OM_DEVICE_REMOVED = 0# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 294

OM_DEVICE_CONNECTED = (OM_DEVICE_REMOVED + 1)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 294

OM_DEVICE_STATUS = enum_anon_8# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 294

OmDeviceCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, OM_DEVICE_STATUS)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 303

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 313
if _libs["libomapi.so"].has("OmSetDeviceCallback", "cdecl"):
    OmSetDeviceCallback = _libs["libomapi.so"].get("OmSetDeviceCallback", "cdecl")
    OmSetDeviceCallback.argtypes = [OmDeviceCallback, POINTER(None)]
    OmSetDeviceCallback.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 325
if _libs["libomapi.so"].has("OmGetDeviceIds", "cdecl"):
    OmGetDeviceIds = _libs["libomapi.so"].get("OmGetDeviceIds", "cdecl")
    OmGetDeviceIds.argtypes = [POINTER(c_int), c_int]
    OmGetDeviceIds.restype = c_int

OM_DATETIME = c_ulong# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 335

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 370
if _libs["libomapi.so"].has("OmGetVersion", "cdecl"):
    OmGetVersion = _libs["libomapi.so"].get("OmGetVersion", "cdecl")
    OmGetVersion.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    OmGetVersion.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 379
if _libs["libomapi.so"].has("OmGetDeviceSerial", "cdecl"):
    OmGetDeviceSerial = _libs["libomapi.so"].get("OmGetDeviceSerial", "cdecl")
    OmGetDeviceSerial.argtypes = [c_int, String]
    OmGetDeviceSerial.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 389
if _libs["libomapi.so"].has("OmGetDevicePort", "cdecl"):
    OmGetDevicePort = _libs["libomapi.so"].get("OmGetDevicePort", "cdecl")
    OmGetDevicePort.argtypes = [c_int, String]
    OmGetDevicePort.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 399
if _libs["libomapi.so"].has("OmGetDevicePath", "cdecl"):
    OmGetDevicePath = _libs["libomapi.so"].get("OmGetDevicePath", "cdecl")
    OmGetDevicePath.argtypes = [c_int, String]
    OmGetDevicePath.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 408
if _libs["libomapi.so"].has("OmGetBatteryLevel", "cdecl"):
    OmGetBatteryLevel = _libs["libomapi.so"].get("OmGetBatteryLevel", "cdecl")
    OmGetBatteryLevel.argtypes = [c_int]
    OmGetBatteryLevel.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 419
if _libs["libomapi.so"].has("OmSelfTest", "cdecl"):
    OmSelfTest = _libs["libomapi.so"].get("OmSelfTest", "cdecl")
    OmSelfTest.argtypes = [c_int]
    OmSelfTest.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 432
if _libs["libomapi.so"].has("OmGetMemoryHealth", "cdecl"):
    OmGetMemoryHealth = _libs["libomapi.so"].get("OmGetMemoryHealth", "cdecl")
    OmGetMemoryHealth.argtypes = [c_int]
    OmGetMemoryHealth.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 446
if _libs["libomapi.so"].has("OmGetBatteryHealth", "cdecl"):
    OmGetBatteryHealth = _libs["libomapi.so"].get("OmGetBatteryHealth", "cdecl")
    OmGetBatteryHealth.argtypes = [c_int]
    OmGetBatteryHealth.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 458
if _libs["libomapi.so"].has("OmGetAccelerometer", "cdecl"):
    OmGetAccelerometer = _libs["libomapi.so"].get("OmGetAccelerometer", "cdecl")
    OmGetAccelerometer.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    OmGetAccelerometer.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 467
if _libs["libomapi.so"].has("OmGetTime", "cdecl"):
    OmGetTime = _libs["libomapi.so"].get("OmGetTime", "cdecl")
    OmGetTime.argtypes = [c_int, POINTER(OM_DATETIME)]
    OmGetTime.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 476
if _libs["libomapi.so"].has("OmSetTime", "cdecl"):
    OmSetTime = _libs["libomapi.so"].get("OmSetTime", "cdecl")
    OmSetTime.argtypes = [c_int, OM_DATETIME]
    OmSetTime.restype = c_int

enum_anon_9 = c_int# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_AUTO = (-1)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_OFF = 0# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_BLUE = 1# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_GREEN = 2# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_CYAN = 3# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_RED = 4# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_MAGENTA = 5# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_YELLOW = 6# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_WHITE = 7# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

OM_LED_STATE = enum_anon_9# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 498

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 508
if _libs["libomapi.so"].has("OmSetLed", "cdecl"):
    OmSetLed = _libs["libomapi.so"].get("OmSetLed", "cdecl")
    OmSetLed.argtypes = [c_int, OM_LED_STATE]
    OmSetLed.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 518
if _libs["libomapi.so"].has("OmIsLocked", "cdecl"):
    OmIsLocked = _libs["libomapi.so"].get("OmIsLocked", "cdecl")
    OmIsLocked.argtypes = [c_int, POINTER(c_int)]
    OmIsLocked.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 529
if _libs["libomapi.so"].has("OmSetLock", "cdecl"):
    OmSetLock = _libs["libomapi.so"].get("OmSetLock", "cdecl")
    OmSetLock.argtypes = [c_int, c_ushort]
    OmSetLock.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 540
if _libs["libomapi.so"].has("OmUnlock", "cdecl"):
    OmUnlock = _libs["libomapi.so"].get("OmUnlock", "cdecl")
    OmUnlock.argtypes = [c_int, c_ushort]
    OmUnlock.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 550
if _libs["libomapi.so"].has("OmSetEcc", "cdecl"):
    OmSetEcc = _libs["libomapi.so"].get("OmSetEcc", "cdecl")
    OmSetEcc.argtypes = [c_int, c_int]
    OmSetEcc.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 559
if _libs["libomapi.so"].has("OmGetEcc", "cdecl"):
    OmGetEcc = _libs["libomapi.so"].get("OmGetEcc", "cdecl")
    OmGetEcc.argtypes = [c_int]
    OmGetEcc.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 578
if _libs["libomapi.so"].has("OmCommand", "cdecl"):
    OmCommand = _libs["libomapi.so"].get("OmCommand", "cdecl")
    OmCommand.argtypes = [c_int, String, String, c_size_t, String, c_uint, POINTER(POINTER(c_char)), c_int]
    OmCommand.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 611
if _libs["libomapi.so"].has("OmGetDelays", "cdecl"):
    OmGetDelays = _libs["libomapi.so"].get("OmGetDelays", "cdecl")
    OmGetDelays.argtypes = [c_int, POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmGetDelays.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 629
if _libs["libomapi.so"].has("OmSetDelays", "cdecl"):
    OmSetDelays = _libs["libomapi.so"].get("OmSetDelays", "cdecl")
    OmSetDelays.argtypes = [c_int, OM_DATETIME, OM_DATETIME]
    OmSetDelays.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 638
if _libs["libomapi.so"].has("OmGetSessionId", "cdecl"):
    OmGetSessionId = _libs["libomapi.so"].get("OmGetSessionId", "cdecl")
    OmGetSessionId.argtypes = [c_int, POINTER(c_uint)]
    OmGetSessionId.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 649
if _libs["libomapi.so"].has("OmSetSessionId", "cdecl"):
    OmSetSessionId = _libs["libomapi.so"].get("OmSetSessionId", "cdecl")
    OmSetSessionId.argtypes = [c_int, c_uint]
    OmSetSessionId.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 666
if _libs["libomapi.so"].has("OmGetMetadata", "cdecl"):
    OmGetMetadata = _libs["libomapi.so"].get("OmGetMetadata", "cdecl")
    OmGetMetadata.argtypes = [c_int, String]
    OmGetMetadata.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 679
if _libs["libomapi.so"].has("OmSetMetadata", "cdecl"):
    OmSetMetadata = _libs["libomapi.so"].get("OmSetMetadata", "cdecl")
    OmSetMetadata.argtypes = [c_int, String, c_int]
    OmSetMetadata.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 688
if _libs["libomapi.so"].has("OmGetLastConfigTime", "cdecl"):
    OmGetLastConfigTime = _libs["libomapi.so"].get("OmGetLastConfigTime", "cdecl")
    OmGetLastConfigTime.argtypes = [c_int, POINTER(OM_DATETIME)]
    OmGetLastConfigTime.restype = c_int

enum_anon_10 = c_int# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 702

OM_ERASE_NONE = 0# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 702

OM_ERASE_DELETE = 1# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 702

OM_ERASE_QUICKFORMAT = 2# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 702

OM_ERASE_WIPE = 3# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 702

OM_ERASE_LEVEL = enum_anon_10# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 702

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 723
if _libs["libomapi.so"].has("OmEraseDataAndCommit", "cdecl"):
    OmEraseDataAndCommit = _libs["libomapi.so"].get("OmEraseDataAndCommit", "cdecl")
    OmEraseDataAndCommit.argtypes = [c_int, OM_ERASE_LEVEL]
    OmEraseDataAndCommit.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 776
if _libs["libomapi.so"].has("OmGetAccelConfig", "cdecl"):
    OmGetAccelConfig = _libs["libomapi.so"].get("OmGetAccelConfig", "cdecl")
    OmGetAccelConfig.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    OmGetAccelConfig.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 789
if _libs["libomapi.so"].has("OmSetAccelConfig", "cdecl"):
    OmSetAccelConfig = _libs["libomapi.so"].get("OmSetAccelConfig", "cdecl")
    OmSetAccelConfig.argtypes = [c_int, c_int, c_int]
    OmSetAccelConfig.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 800
if _libs["libomapi.so"].has("OmGetMaxSamples", "cdecl"):
    OmGetMaxSamples = _libs["libomapi.so"].get("OmGetMaxSamples", "cdecl")
    OmGetMaxSamples.argtypes = [c_int, POINTER(c_int)]
    OmGetMaxSamples.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 812
if _libs["libomapi.so"].has("OmSetMaxSamples", "cdecl"):
    OmSetMaxSamples = _libs["libomapi.so"].get("OmSetMaxSamples", "cdecl")
    OmSetMaxSamples.argtypes = [c_int, c_int]
    OmSetMaxSamples.restype = c_int

enum_anon_11 = c_int# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 857

OM_DOWNLOAD_NONE = 0# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 857

OM_DOWNLOAD_ERROR = (OM_DOWNLOAD_NONE + 1)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 857

OM_DOWNLOAD_PROGRESS = (OM_DOWNLOAD_ERROR + 1)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 857

OM_DOWNLOAD_COMPLETE = (OM_DOWNLOAD_PROGRESS + 1)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 857

OM_DOWNLOAD_CANCELLED = (OM_DOWNLOAD_COMPLETE + 1)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 857

OM_DOWNLOAD_STATUS = enum_anon_11# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 857

OmDownloadCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, OM_DOWNLOAD_STATUS, c_int)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 866

OmDownloadChunkCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, POINTER(None), c_int, c_int)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 876

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 885
if _libs["libomapi.so"].has("OmSetDownloadCallback", "cdecl"):
    OmSetDownloadCallback = _libs["libomapi.so"].get("OmSetDownloadCallback", "cdecl")
    OmSetDownloadCallback.argtypes = [OmDownloadCallback, POINTER(None)]
    OmSetDownloadCallback.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 895
if _libs["libomapi.so"].has("OmSetDownloadChunkCallback", "cdecl"):
    OmSetDownloadChunkCallback = _libs["libomapi.so"].get("OmSetDownloadChunkCallback", "cdecl")
    OmSetDownloadChunkCallback.argtypes = [OmDownloadChunkCallback, POINTER(None)]
    OmSetDownloadChunkCallback.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 904
if _libs["libomapi.so"].has("OmGetDataFileSize", "cdecl"):
    OmGetDataFileSize = _libs["libomapi.so"].get("OmGetDataFileSize", "cdecl")
    OmGetDataFileSize.argtypes = [c_int]
    OmGetDataFileSize.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 914
if _libs["libomapi.so"].has("OmGetDataFilename", "cdecl"):
    OmGetDataFilename = _libs["libomapi.so"].get("OmGetDataFilename", "cdecl")
    OmGetDataFilename.argtypes = [c_int, String]
    OmGetDataFilename.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 927
if _libs["libomapi.so"].has("OmGetDataRange", "cdecl"):
    OmGetDataRange = _libs["libomapi.so"].get("OmGetDataRange", "cdecl")
    OmGetDataRange.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmGetDataRange.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 943
if _libs["libomapi.so"].has("OmBeginDownloading", "cdecl"):
    OmBeginDownloading = _libs["libomapi.so"].get("OmBeginDownloading", "cdecl")
    OmBeginDownloading.argtypes = [c_int, c_int, c_int, String]
    OmBeginDownloading.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 961
if _libs["libomapi.so"].has("OmBeginDownloadingReference", "cdecl"):
    OmBeginDownloadingReference = _libs["libomapi.so"].get("OmBeginDownloadingReference", "cdecl")
    OmBeginDownloadingReference.argtypes = [c_int, c_int, c_int, String, POINTER(None)]
    OmBeginDownloadingReference.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 976
if _libs["libomapi.so"].has("OmQueryDownload", "cdecl"):
    OmQueryDownload = _libs["libomapi.so"].get("OmQueryDownload", "cdecl")
    OmQueryDownload.argtypes = [c_int, POINTER(OM_DOWNLOAD_STATUS), POINTER(c_int)]
    OmQueryDownload.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 991
if _libs["libomapi.so"].has("OmWaitForDownload", "cdecl"):
    OmWaitForDownload = _libs["libomapi.so"].get("OmWaitForDownload", "cdecl")
    OmWaitForDownload.argtypes = [c_int, POINTER(OM_DOWNLOAD_STATUS), POINTER(c_int)]
    OmWaitForDownload.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1001
if _libs["libomapi.so"].has("OmCancelDownload", "cdecl"):
    OmCancelDownload = _libs["libomapi.so"].get("OmCancelDownload", "cdecl")
    OmCancelDownload.argtypes = [c_int]
    OmCancelDownload.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1044
if _libs["libomapi.so"].has("OmErrorString", "cdecl"):
    OmErrorString = _libs["libomapi.so"].get("OmErrorString", "cdecl")
    OmErrorString.argtypes = [c_int]
    OmErrorString.restype = c_char_p

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1099
if _libs["libomapi.so"].has("OmDateTimeFromString", "cdecl"):
    OmDateTimeFromString = _libs["libomapi.so"].get("OmDateTimeFromString", "cdecl")
    OmDateTimeFromString.argtypes = [String]
    OmDateTimeFromString.restype = OM_DATETIME

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1103
if _libs["libomapi.so"].has("OmDateTimeToString", "cdecl"):
    OmDateTimeToString = _libs["libomapi.so"].get("OmDateTimeToString", "cdecl")
    OmDateTimeToString.argtypes = [OM_DATETIME, String]
    if sizeof(c_int) == sizeof(c_void_p):
        OmDateTimeToString.restype = ReturnString
    else:
        OmDateTimeToString.restype = String
        OmDateTimeToString.errcheck = ReturnString

OmReaderHandle = POINTER(None)# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1130

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1161
if _libs["libomapi.so"].has("OmReaderOpen", "cdecl"):
    OmReaderOpen = _libs["libomapi.so"].get("OmReaderOpen", "cdecl")
    OmReaderOpen.argtypes = [String]
    OmReaderOpen.restype = OmReaderHandle

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1174
if _libs["libomapi.so"].has("OmReaderDataRange", "cdecl"):
    OmReaderDataRange = _libs["libomapi.so"].get("OmReaderDataRange", "cdecl")
    OmReaderDataRange.argtypes = [OmReaderHandle, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmReaderDataRange.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1184
if _libs["libomapi.so"].has("OmReaderMetadata", "cdecl"):
    OmReaderMetadata = _libs["libomapi.so"].get("OmReaderMetadata", "cdecl")
    OmReaderMetadata.argtypes = [OmReaderHandle, POINTER(c_int), POINTER(c_uint)]
    OmReaderMetadata.restype = c_char_p

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1192
if _libs["libomapi.so"].has("OmReaderDataBlockPosition", "cdecl"):
    OmReaderDataBlockPosition = _libs["libomapi.so"].get("OmReaderDataBlockPosition", "cdecl")
    OmReaderDataBlockPosition.argtypes = [OmReaderHandle]
    OmReaderDataBlockPosition.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1201
if _libs["libomapi.so"].has("OmReaderDataBlockSeek", "cdecl"):
    OmReaderDataBlockSeek = _libs["libomapi.so"].get("OmReaderDataBlockSeek", "cdecl")
    OmReaderDataBlockSeek.argtypes = [OmReaderHandle, c_int]
    OmReaderDataBlockSeek.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1213
if _libs["libomapi.so"].has("OmReaderNextBlock", "cdecl"):
    OmReaderNextBlock = _libs["libomapi.so"].get("OmReaderNextBlock", "cdecl")
    OmReaderNextBlock.argtypes = [OmReaderHandle]
    OmReaderNextBlock.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1225
if _libs["libomapi.so"].has("OmReaderBuffer", "cdecl"):
    OmReaderBuffer = _libs["libomapi.so"].get("OmReaderBuffer", "cdecl")
    OmReaderBuffer.argtypes = [OmReaderHandle]
    OmReaderBuffer.restype = POINTER(c_short)

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1240
if _libs["libomapi.so"].has("OmReaderTimestamp", "cdecl"):
    OmReaderTimestamp = _libs["libomapi.so"].get("OmReaderTimestamp", "cdecl")
    OmReaderTimestamp.argtypes = [OmReaderHandle, c_int, POINTER(c_ushort)]
    OmReaderTimestamp.restype = OM_DATETIME

enum_anon_12 = c_int# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_DEVICEID = 3# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_SESSIONID = 4# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_SEQUENCEID = 5# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_LIGHT = 7# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_TEMPERATURE = 8# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_EVENTS = 9# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_BATTERY = 10# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_SAMPLERATE = 11# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_LIGHT_LOG10LUXTIMES10POWER3 = 107# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_TEMPERATURE_MC = 108# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_BATTERY_MV = 110# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_BATTERY_PERCENT = 210# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_AXES = 12# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_SCALE_ACCEL = 13# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_SCALE_GYRO = 14# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_SCALE_MAG = 15# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_ACCEL_AXIS = 16# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_GYRO_AXIS = 17# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_VALUE_MAG_AXIS = 18# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

OM_READER_VALUE_TYPE = enum_anon_12# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1275

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1287
if _libs["libomapi.so"].has("OmReaderGetValue", "cdecl"):
    OmReaderGetValue = _libs["libomapi.so"].get("OmReaderGetValue", "cdecl")
    OmReaderGetValue.argtypes = [OmReaderHandle, OM_READER_VALUE_TYPE]
    OmReaderGetValue.restype = c_int

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1314
class struct_anon_13(Structure):
    pass

struct_anon_13._pack_ = 1
struct_anon_13.__slots__ = [
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
struct_anon_13._fields_ = [
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

OM_READER_HEADER_PACKET = struct_anon_13# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1314

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1325
if _libs["libomapi.so"].has("OmReaderRawHeaderPacket", "cdecl"):
    OmReaderRawHeaderPacket = _libs["libomapi.so"].get("OmReaderRawHeaderPacket", "cdecl")
    OmReaderRawHeaderPacket.argtypes = [OmReaderHandle]
    OmReaderRawHeaderPacket.restype = POINTER(OM_READER_HEADER_PACKET)

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1351
class struct_anon_14(Structure):
    pass

struct_anon_14._pack_ = 1
struct_anon_14.__slots__ = [
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
struct_anon_14._fields_ = [
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

OM_READER_DATA_PACKET = struct_anon_14# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1351

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1363
if _libs["libomapi.so"].has("OmReaderRawDataPacket", "cdecl"):
    OmReaderRawDataPacket = _libs["libomapi.so"].get("OmReaderRawDataPacket", "cdecl")
    OmReaderRawDataPacket.argtypes = [OmReaderHandle]
    OmReaderRawDataPacket.restype = POINTER(OM_READER_DATA_PACKET)

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1372
if _libs["libomapi.so"].has("OmReaderClose", "cdecl"):
    OmReaderClose = _libs["libomapi.so"].get("OmReaderClose", "cdecl")
    OmReaderClose.argtypes = [OmReaderHandle]
    OmReaderClose.restype = None

# <built-in>
try:
    __WCHAR_MAX__ = 2147483647
except:
    pass

# <built-in>
try:
    __ENVIRONMENT_MAC_OS_X_VERSION_MIN_REQUIRED__ = 120000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/Availability.h: 132
try:
    __API_TO_BE_DEPRECATED = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/Availability.h: 136
try:
    __API_TO_BE_DEPRECATED_MACOS = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/Availability.h: 140
try:
    __API_TO_BE_DEPRECATED_IOS = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/Availability.h: 144
try:
    __API_TO_BE_DEPRECATED_TVOS = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/Availability.h: 148
try:
    __API_TO_BE_DEPRECATED_WATCHOS = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/Availability.h: 156
try:
    __API_TO_BE_DEPRECATED_MACCATALYST = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/Availability.h: 160
try:
    __API_TO_BE_DEPRECATED_DRIVERKIT = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 27
try:
    __MAC_10_0 = 1000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 28
try:
    __MAC_10_1 = 1010
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 29
try:
    __MAC_10_2 = 1020
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 30
try:
    __MAC_10_3 = 1030
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 31
try:
    __MAC_10_4 = 1040
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 32
try:
    __MAC_10_5 = 1050
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 33
try:
    __MAC_10_6 = 1060
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 34
try:
    __MAC_10_7 = 1070
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 35
try:
    __MAC_10_8 = 1080
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 36
try:
    __MAC_10_9 = 1090
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 37
try:
    __MAC_10_10 = 101000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 38
try:
    __MAC_10_10_2 = 101002
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 39
try:
    __MAC_10_10_3 = 101003
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 40
try:
    __MAC_10_11 = 101100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 41
try:
    __MAC_10_11_2 = 101102
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 42
try:
    __MAC_10_11_3 = 101103
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 43
try:
    __MAC_10_11_4 = 101104
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 44
try:
    __MAC_10_12 = 101200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 45
try:
    __MAC_10_12_1 = 101201
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 46
try:
    __MAC_10_12_2 = 101202
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 47
try:
    __MAC_10_12_4 = 101204
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 48
try:
    __MAC_10_13 = 101300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 49
try:
    __MAC_10_13_1 = 101301
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 50
try:
    __MAC_10_13_2 = 101302
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 51
try:
    __MAC_10_13_4 = 101304
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 52
try:
    __MAC_10_14 = 101400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 53
try:
    __MAC_10_14_1 = 101401
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 54
try:
    __MAC_10_14_4 = 101404
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 55
try:
    __MAC_10_14_6 = 101406
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 56
try:
    __MAC_10_15 = 101500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 57
try:
    __MAC_10_15_1 = 101501
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 58
try:
    __MAC_10_15_4 = 101504
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 59
try:
    __MAC_10_16 = 101600
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 60
try:
    __MAC_11_0 = 110000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 61
try:
    __MAC_11_1 = 110100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 62
try:
    __MAC_11_3 = 110300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 63
try:
    __MAC_11_4 = 110400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 64
try:
    __MAC_11_5 = 110500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 65
try:
    __MAC_11_6 = 110600
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 66
try:
    __MAC_12_0 = 120000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 67
try:
    __MAC_12_1 = 120100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 68
try:
    __MAC_12_2 = 120200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 69
try:
    __MAC_12_3 = 120300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 70
try:
    __MAC_13_0 = 130000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 71
try:
    __MAC_13_1 = 130100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 74
try:
    __IPHONE_2_0 = 20000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 75
try:
    __IPHONE_2_1 = 20100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 76
try:
    __IPHONE_2_2 = 20200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 77
try:
    __IPHONE_3_0 = 30000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 78
try:
    __IPHONE_3_1 = 30100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 79
try:
    __IPHONE_3_2 = 30200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 80
try:
    __IPHONE_4_0 = 40000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 81
try:
    __IPHONE_4_1 = 40100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 82
try:
    __IPHONE_4_2 = 40200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 83
try:
    __IPHONE_4_3 = 40300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 84
try:
    __IPHONE_5_0 = 50000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 85
try:
    __IPHONE_5_1 = 50100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 86
try:
    __IPHONE_6_0 = 60000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 87
try:
    __IPHONE_6_1 = 60100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 88
try:
    __IPHONE_7_0 = 70000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 89
try:
    __IPHONE_7_1 = 70100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 90
try:
    __IPHONE_8_0 = 80000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 91
try:
    __IPHONE_8_1 = 80100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 92
try:
    __IPHONE_8_2 = 80200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 93
try:
    __IPHONE_8_3 = 80300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 94
try:
    __IPHONE_8_4 = 80400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 95
try:
    __IPHONE_9_0 = 90000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 96
try:
    __IPHONE_9_1 = 90100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 97
try:
    __IPHONE_9_2 = 90200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 98
try:
    __IPHONE_9_3 = 90300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 99
try:
    __IPHONE_10_0 = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 100
try:
    __IPHONE_10_1 = 100100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 101
try:
    __IPHONE_10_2 = 100200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 102
try:
    __IPHONE_10_3 = 100300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 103
try:
    __IPHONE_11_0 = 110000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 104
try:
    __IPHONE_11_1 = 110100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 105
try:
    __IPHONE_11_2 = 110200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 106
try:
    __IPHONE_11_3 = 110300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 107
try:
    __IPHONE_11_4 = 110400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 108
try:
    __IPHONE_12_0 = 120000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 109
try:
    __IPHONE_12_1 = 120100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 110
try:
    __IPHONE_12_2 = 120200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 111
try:
    __IPHONE_12_3 = 120300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 112
try:
    __IPHONE_12_4 = 120400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 113
try:
    __IPHONE_13_0 = 130000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 114
try:
    __IPHONE_13_1 = 130100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 115
try:
    __IPHONE_13_2 = 130200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 116
try:
    __IPHONE_13_3 = 130300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 117
try:
    __IPHONE_13_4 = 130400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 118
try:
    __IPHONE_13_5 = 130500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 119
try:
    __IPHONE_13_6 = 130600
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 120
try:
    __IPHONE_13_7 = 130700
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 121
try:
    __IPHONE_14_0 = 140000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 122
try:
    __IPHONE_14_1 = 140100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 123
try:
    __IPHONE_14_2 = 140200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 124
try:
    __IPHONE_14_3 = 140300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 125
try:
    __IPHONE_14_5 = 140500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 126
try:
    __IPHONE_14_6 = 140600
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 127
try:
    __IPHONE_14_7 = 140700
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 128
try:
    __IPHONE_14_8 = 140800
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 129
try:
    __IPHONE_15_0 = 150000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 130
try:
    __IPHONE_15_1 = 150100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 131
try:
    __IPHONE_15_2 = 150200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 132
try:
    __IPHONE_15_3 = 150300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 133
try:
    __IPHONE_15_4 = 150400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 134
try:
    __IPHONE_16_0 = 160000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 135
try:
    __IPHONE_16_1 = 160100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 136
try:
    __IPHONE_16_2 = 160200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 139
try:
    __TVOS_9_0 = 90000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 140
try:
    __TVOS_9_1 = 90100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 141
try:
    __TVOS_9_2 = 90200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 142
try:
    __TVOS_10_0 = 100000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 143
try:
    __TVOS_10_0_1 = 100001
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 144
try:
    __TVOS_10_1 = 100100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 145
try:
    __TVOS_10_2 = 100200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 146
try:
    __TVOS_11_0 = 110000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 147
try:
    __TVOS_11_1 = 110100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 148
try:
    __TVOS_11_2 = 110200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 149
try:
    __TVOS_11_3 = 110300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 150
try:
    __TVOS_11_4 = 110400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 151
try:
    __TVOS_12_0 = 120000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 152
try:
    __TVOS_12_1 = 120100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 153
try:
    __TVOS_12_2 = 120200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 154
try:
    __TVOS_12_3 = 120300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 155
try:
    __TVOS_12_4 = 120400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 156
try:
    __TVOS_13_0 = 130000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 157
try:
    __TVOS_13_2 = 130200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 158
try:
    __TVOS_13_3 = 130300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 159
try:
    __TVOS_13_4 = 130400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 160
try:
    __TVOS_14_0 = 140000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 161
try:
    __TVOS_14_1 = 140100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 162
try:
    __TVOS_14_2 = 140200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 163
try:
    __TVOS_14_3 = 140300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 164
try:
    __TVOS_14_5 = 140500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 165
try:
    __TVOS_14_6 = 140600
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 166
try:
    __TVOS_14_7 = 140700
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 167
try:
    __TVOS_15_0 = 150000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 168
try:
    __TVOS_15_1 = 150100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 169
try:
    __TVOS_15_2 = 150200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 170
try:
    __TVOS_15_3 = 150300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 171
try:
    __TVOS_15_4 = 150400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 172
try:
    __TVOS_16_0 = 160000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 173
try:
    __TVOS_16_1 = 160100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 174
try:
    __TVOS_16_2 = 160200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 176
try:
    __WATCHOS_1_0 = 10000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 177
try:
    __WATCHOS_2_0 = 20000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 178
try:
    __WATCHOS_2_1 = 20100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 179
try:
    __WATCHOS_2_2 = 20200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 180
try:
    __WATCHOS_3_0 = 30000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 181
try:
    __WATCHOS_3_1 = 30100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 182
try:
    __WATCHOS_3_1_1 = 30101
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 183
try:
    __WATCHOS_3_2 = 30200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 184
try:
    __WATCHOS_4_0 = 40000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 185
try:
    __WATCHOS_4_1 = 40100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 186
try:
    __WATCHOS_4_2 = 40200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 187
try:
    __WATCHOS_4_3 = 40300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 188
try:
    __WATCHOS_5_0 = 50000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 189
try:
    __WATCHOS_5_1 = 50100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 190
try:
    __WATCHOS_5_2 = 50200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 191
try:
    __WATCHOS_5_3 = 50300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 192
try:
    __WATCHOS_6_0 = 60000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 193
try:
    __WATCHOS_6_1 = 60100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 194
try:
    __WATCHOS_6_2 = 60200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 195
try:
    __WATCHOS_7_0 = 70000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 196
try:
    __WATCHOS_7_1 = 70100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 197
try:
    __WATCHOS_7_2 = 70200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 198
try:
    __WATCHOS_7_3 = 70300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 199
try:
    __WATCHOS_7_4 = 70400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 200
try:
    __WATCHOS_7_5 = 70500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 201
try:
    __WATCHOS_7_6 = 70600
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 202
try:
    __WATCHOS_8_0 = 80000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 203
try:
    __WATCHOS_8_1 = 80100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 204
try:
    __WATCHOS_8_3 = 80300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 205
try:
    __WATCHOS_8_4 = 80400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 206
try:
    __WATCHOS_8_5 = 80500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 207
try:
    __WATCHOS_9_0 = 90000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 208
try:
    __WATCHOS_9_1 = 90100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 209
try:
    __WATCHOS_9_2 = 90200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 217
try:
    MAC_OS_X_VERSION_10_0 = 1000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 218
try:
    MAC_OS_X_VERSION_10_1 = 1010
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 219
try:
    MAC_OS_X_VERSION_10_2 = 1020
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 220
try:
    MAC_OS_X_VERSION_10_3 = 1030
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 221
try:
    MAC_OS_X_VERSION_10_4 = 1040
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 222
try:
    MAC_OS_X_VERSION_10_5 = 1050
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 223
try:
    MAC_OS_X_VERSION_10_6 = 1060
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 224
try:
    MAC_OS_X_VERSION_10_7 = 1070
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 225
try:
    MAC_OS_X_VERSION_10_8 = 1080
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 226
try:
    MAC_OS_X_VERSION_10_9 = 1090
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 227
try:
    MAC_OS_X_VERSION_10_10 = 101000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 228
try:
    MAC_OS_X_VERSION_10_10_2 = 101002
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 229
try:
    MAC_OS_X_VERSION_10_10_3 = 101003
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 230
try:
    MAC_OS_X_VERSION_10_11 = 101100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 231
try:
    MAC_OS_X_VERSION_10_11_2 = 101102
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 232
try:
    MAC_OS_X_VERSION_10_11_3 = 101103
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 233
try:
    MAC_OS_X_VERSION_10_11_4 = 101104
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 234
try:
    MAC_OS_X_VERSION_10_12 = 101200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 235
try:
    MAC_OS_X_VERSION_10_12_1 = 101201
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 236
try:
    MAC_OS_X_VERSION_10_12_2 = 101202
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 237
try:
    MAC_OS_X_VERSION_10_12_4 = 101204
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 238
try:
    MAC_OS_X_VERSION_10_13 = 101300
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 239
try:
    MAC_OS_X_VERSION_10_13_1 = 101301
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 240
try:
    MAC_OS_X_VERSION_10_13_2 = 101302
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 241
try:
    MAC_OS_X_VERSION_10_13_4 = 101304
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 242
try:
    MAC_OS_X_VERSION_10_14 = 101400
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 243
try:
    MAC_OS_X_VERSION_10_14_1 = 101401
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 244
try:
    MAC_OS_X_VERSION_10_14_4 = 101404
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 245
try:
    MAC_OS_X_VERSION_10_14_6 = 101406
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 246
try:
    MAC_OS_X_VERSION_10_15 = 101500
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 247
try:
    MAC_OS_X_VERSION_10_15_1 = 101501
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 248
try:
    MAC_OS_X_VERSION_10_16 = 101600
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 249
try:
    MAC_OS_VERSION_11_0 = 110000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 250
try:
    MAC_OS_VERSION_12_0 = 120000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 251
try:
    MAC_OS_VERSION_13_0 = 130000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 255
try:
    __DRIVERKIT_19_0 = 190000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 256
try:
    __DRIVERKIT_20_0 = 200000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h: 257
try:
    __DRIVERKIT_21_0 = 210000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h: 40
try:
    __MAC_OS_X_VERSION_MIN_REQUIRED = __ENVIRONMENT_MAC_OS_X_VERSION_MIN_REQUIRED__
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h: 93
try:
    __MAC_OS_X_VERSION_MAX_ALLOWED = __MAC_13_1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h: 148
try:
    __ENABLE_LEGACY_MAC_AVAILABILITY = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h: 4480
def __API_RANGE_STRINGIFY(x):
    return (__API_RANGE_STRINGIFY2 (x))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h: 4481
def __API_RANGE_STRINGIFY2(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 112
def __P(protos):
    return protos

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 114
def __STRING(x):
    return x

__const = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 116

__signed = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 117

__volatile = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 118

__restrict = c_int# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 254

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 513
try:
    __DARWIN_ONLY_64_BIT_INO_T = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 514
try:
    __DARWIN_ONLY_UNIX_CONFORMANCE = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 515
try:
    __DARWIN_ONLY_VERS_1050 = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 545
try:
    __DARWIN_UNIX03 = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 581
try:
    __DARWIN_64_BIT_INO_T = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 592
try:
    __DARWIN_VERS_1050 = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 597
try:
    __DARWIN_NON_CANCELABLE = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 614
try:
    __DARWIN_SUF_64_BIT_INO_T = '$INODE64'
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 624
try:
    __DARWIN_SUF_1050 = '$1050'
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 643
try:
    __DARWIN_SUF_EXTSN = '$DARWIN_EXTSN'
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 393
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_0(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 399
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_1(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 405
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_2(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 411
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_3(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 417
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_4(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 423
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_5(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 429
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_6(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 435
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_7(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 441
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_8(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 447
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_9(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 453
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_10(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 459
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_10_2(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 465
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_10_3(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 471
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_11(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 477
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_11_2(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 483
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_11_3(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 489
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_11_4(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 495
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_12(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 501
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_12_1(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 507
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_12_2(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 513
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_12_4(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 519
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_13(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 525
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_13_1(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 531
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_13_2(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 537
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_13_4(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 543
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_14(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 549
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_14_1(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 555
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_14_4(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 561
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_14_5(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 567
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_14_6(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 573
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_15(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 579
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_15_1(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 585
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_15_4(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 591
def __DARWIN_ALIAS_STARTING_MAC___MAC_10_16(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 597
def __DARWIN_ALIAS_STARTING_MAC___MAC_11_0(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 603
def __DARWIN_ALIAS_STARTING_MAC___MAC_11_1(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 609
def __DARWIN_ALIAS_STARTING_MAC___MAC_11_3(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h: 615
def __DARWIN_ALIAS_STARTING_MAC___MAC_12_0(x):
    return x

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 742
try:
    __DARWIN_C_ANSI = 0o10000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 743
try:
    __DARWIN_C_FULL = 900000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 750
try:
    __DARWIN_C_LEVEL = __DARWIN_C_FULL
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 758
try:
    __STDC_WANT_LIB_EXT1__ = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 769
try:
    __DARWIN_NO_LONG_LONG = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 781
try:
    _DARWIN_FEATURE_64_BIT_INODE = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 807
try:
    _DARWIN_FEATURE_ONLY_UNIX_CONFORMANCE = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 815
try:
    _DARWIN_FEATURE_UNIX_CONFORMANCE = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 857
try:
    __has_ptrcheck = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 877
def __unsafe_forge_bidi_indexable(T, P, S):
    return (T (P))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 878
def __unsafe_forge_single(T, P):
    return (T (P))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 879
def __terminated_by_to_indexable(P):
    return P

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 880
def __unsafe_terminated_by_to_indexable(P):
    return P

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 881
def __null_terminated_to_indexable(P):
    return P

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h: 882
def __unsafe_null_terminated_to_indexable(P):
    return P

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 52
try:
    __DARWIN_NULL = cast(0, POINTER(None))
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 36
try:
    __PTHREAD_SIZE__ = 8176
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 37
try:
    __PTHREAD_ATTR_SIZE__ = 56
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 38
try:
    __PTHREAD_MUTEXATTR_SIZE__ = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 39
try:
    __PTHREAD_MUTEX_SIZE__ = 56
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 40
try:
    __PTHREAD_CONDATTR_SIZE__ = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 41
try:
    __PTHREAD_COND_SIZE__ = 40
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 42
try:
    __PTHREAD_ONCE_SIZE__ = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 43
try:
    __PTHREAD_RWLOCK_SIZE__ = 192
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 44
try:
    __PTHREAD_RWLOCKATTR_SIZE__ = 16
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types.h: 49
try:
    __DARWIN_WCHAR_MAX = __WCHAR_MAX__
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types.h: 55
try:
    __DARWIN_WCHAR_MIN = ((-0x7fffffff) - 1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types.h: 59
try:
    __DARWIN_WEOF = (__darwin_wint_t (ord_if_char((-1)))).value
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_types.h: 65
try:
    _FORTIFY_SOURCE = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 76
try:
    __DARWIN_NSIG = 32
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 79
try:
    NSIG = __DARWIN_NSIG
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/signal.h: 34
try:
    _I386_SIGNAL_H_ = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 84
try:
    SIGHUP = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 85
try:
    SIGINT = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 86
try:
    SIGQUIT = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 87
try:
    SIGILL = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 88
try:
    SIGTRAP = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 89
try:
    SIGABRT = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 93
try:
    SIGIOT = SIGABRT
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 94
try:
    SIGEMT = 7
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 96
try:
    SIGFPE = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 97
try:
    SIGKILL = 9
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 98
try:
    SIGBUS = 10
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 99
try:
    SIGSEGV = 11
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 100
try:
    SIGSYS = 12
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 101
try:
    SIGPIPE = 13
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 102
try:
    SIGALRM = 14
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 103
try:
    SIGTERM = 15
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 104
try:
    SIGURG = 16
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 105
try:
    SIGSTOP = 17
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 106
try:
    SIGTSTP = 18
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 107
try:
    SIGCONT = 19
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 108
try:
    SIGCHLD = 20
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 109
try:
    SIGTTIN = 21
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 110
try:
    SIGTTOU = 22
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 112
try:
    SIGIO = 23
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 114
try:
    SIGXCPU = 24
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 115
try:
    SIGXFSZ = 25
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 116
try:
    SIGVTALRM = 26
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 117
try:
    SIGPROF = 27
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 119
try:
    SIGWINCH = 28
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 120
try:
    SIGINFO = 29
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 122
try:
    SIGUSR1 = 30
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 123
try:
    SIGUSR2 = 31
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 131
try:
    SIG_DFL = cast(0, POINTER(CFUNCTYPE(UNCHECKED(None), c_int)))
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 132
try:
    SIG_IGN = cast(1, POINTER(CFUNCTYPE(UNCHECKED(None), c_int)))
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 133
try:
    SIG_HOLD = cast(5, POINTER(CFUNCTYPE(UNCHECKED(None), c_int)))
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 134
try:
    SIG_ERR = cast((-1), POINTER(CFUNCTYPE(UNCHECKED(None), c_int)))
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 107
try:
    USER_ADDR_NULL = (user_addr_t (ord_if_char(0))).value
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/types.h: 108
def CAST_USER_ADDR_T(a_ptr):
    return (user_addr_t (ord_if_char((uintptr_t (ord_if_char(a_ptr))).value))).value

_STRUCT_X86_THREAD_STATE32 = struct___darwin_i386_thread_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 47

_STRUCT_FP_CONTROL = struct___darwin_fp_control# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 93

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 105
try:
    FP_PREC_24B = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 106
try:
    FP_PREC_53B = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 107
try:
    FP_PREC_64B = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 111
try:
    FP_RND_NEAR = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 112
try:
    FP_RND_DOWN = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 113
try:
    FP_RND_UP = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 114
try:
    FP_CHOP = 3
except:
    pass

_STRUCT_FP_STATUS = struct___darwin_fp_status# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 151

_STRUCT_MMST_REG = struct___darwin_mmst_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 195

_STRUCT_XMM_REG = struct___darwin_xmm_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 214

_STRUCT_YMM_REG = struct___darwin_ymm_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 230

_STRUCT_ZMM_REG = struct___darwin_zmm_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 246

_STRUCT_OPMASK_REG = struct___darwin_opmask_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 260

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 278
try:
    FP_STATE_BYTES = 512
except:
    pass

_STRUCT_X86_FLOAT_STATE32 = struct___darwin_i386_float_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 282

_STRUCT_X86_AVX_STATE32 = struct___darwin_i386_avx_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 319

_STRUCT_X86_AVX512_STATE32 = struct___darwin_i386_avx512_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 365

_STRUCT_X86_EXCEPTION_STATE32 = struct___darwin_i386_exception_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 576

_STRUCT_X86_DEBUG_STATE32 = struct___darwin_x86_debug_state32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 596

_STRUCT_X86_INSTRUCTION_STATE = struct___x86_instruction_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 609

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 619
try:
    _X86_INSTRUCTION_STATE_MAX_INSN_BYTES = ((2448 - 64) - 4)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 621
try:
    _X86_INSTRUCTION_STATE_CACHELINE_SIZE = 64
except:
    pass

_STRUCT_LAST_BRANCH_RECORD = struct___last_branch_record# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 625

_STRUCT_LAST_BRANCH_STATE = struct___last_branch_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 637

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 644
try:
    __LASTBRANCH_MAX = 32
except:
    pass

_STRUCT_X86_PAGEIN_STATE = struct___x86_pagein_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 703

_STRUCT_X86_THREAD_STATE64 = struct___darwin_x86_thread_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 714

_STRUCT_X86_THREAD_FULL_STATE64 = struct___darwin_x86_thread_full_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 772

_STRUCT_X86_FLOAT_STATE64 = struct___darwin_x86_float_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 795

_STRUCT_X86_AVX_STATE64 = struct___darwin_x86_avx_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 846

_STRUCT_X86_AVX512_STATE64 = struct___darwin_x86_avx512_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 914

_STRUCT_X86_EXCEPTION_STATE64 = struct___darwin_x86_exception_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1253

_STRUCT_X86_DEBUG_STATE64 = struct___darwin_x86_debug_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1273

_STRUCT_X86_CPMU_STATE64 = struct___darwin_x86_cpmu_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1301

_STRUCT_MCONTEXT32 = struct___darwin_mcontext32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 40

_STRUCT_MCONTEXT_AVX32 = struct___darwin_mcontext_avx32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 48

_STRUCT_MCONTEXT_AVX512_32 = struct___darwin_mcontext_avx512_32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 57

_STRUCT_MCONTEXT64 = struct___darwin_mcontext64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 98

_STRUCT_MCONTEXT64_FULL = struct___darwin_mcontext64_full# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 106

_STRUCT_MCONTEXT_AVX64 = struct___darwin_mcontext_avx64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 114

_STRUCT_MCONTEXT_AVX64_FULL = struct___darwin_mcontext_avx64_full# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 122

_STRUCT_MCONTEXT_AVX512_64 = struct___darwin_mcontext_avx512_64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 131

_STRUCT_MCONTEXT_AVX512_64_FULL = struct___darwin_mcontext_avx512_64_full# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 139

_STRUCT_SIGALTSTACK = struct___darwin_sigaltstack# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigaltstack.h: 35

_STRUCT_UCONTEXT = struct___darwin_ucontext# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_ucontext.h: 33

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 164
try:
    SIGEV_NONE = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 165
try:
    SIGEV_SIGNAL = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 166
try:
    SIGEV_THREAD = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 206
try:
    ILL_NOOP = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 208
try:
    ILL_ILLOPC = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 209
try:
    ILL_ILLTRP = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 210
try:
    ILL_PRVOPC = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 211
try:
    ILL_ILLOPN = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 212
try:
    ILL_ILLADR = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 213
try:
    ILL_PRVREG = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 214
try:
    ILL_COPROC = 7
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 215
try:
    ILL_BADSTK = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 219
try:
    FPE_NOOP = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 221
try:
    FPE_FLTDIV = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 222
try:
    FPE_FLTOVF = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 223
try:
    FPE_FLTUND = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 224
try:
    FPE_FLTRES = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 225
try:
    FPE_FLTINV = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 226
try:
    FPE_FLTSUB = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 227
try:
    FPE_INTDIV = 7
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 228
try:
    FPE_INTOVF = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 232
try:
    SEGV_NOOP = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 234
try:
    SEGV_MAPERR = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 235
try:
    SEGV_ACCERR = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 239
try:
    BUS_NOOP = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 241
try:
    BUS_ADRALN = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 242
try:
    BUS_ADRERR = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 243
try:
    BUS_OBJERR = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 246
try:
    TRAP_BRKPT = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 247
try:
    TRAP_TRACE = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 251
try:
    CLD_NOOP = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 253
try:
    CLD_EXITED = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 254
try:
    CLD_KILLED = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 255
try:
    CLD_DUMPED = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 256
try:
    CLD_TRAPPED = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 257
try:
    CLD_STOPPED = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 258
try:
    CLD_CONTINUED = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 261
try:
    POLL_IN = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 262
try:
    POLL_OUT = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 263
try:
    POLL_MSG = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 264
try:
    POLL_ERR = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 265
try:
    POLL_PRI = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 266
try:
    POLL_HUP = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 298
try:
    SA_ONSTACK = 0x0001
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 299
try:
    SA_RESTART = 0x0002
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 300
try:
    SA_RESETHAND = 0x0004
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 301
try:
    SA_NOCLDSTOP = 0x0008
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 302
try:
    SA_NODEFER = 0x0010
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 303
try:
    SA_NOCLDWAIT = 0x0020
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 304
try:
    SA_SIGINFO = 0x0040
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 306
try:
    SA_USERTRAMP = 0x0100
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 308
try:
    SA_64REGSET = 0x0200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 314
try:
    SA_USERSPACE_MASK = ((((((SA_ONSTACK | SA_RESTART) | SA_RESETHAND) | SA_NOCLDSTOP) | SA_NODEFER) | SA_NOCLDWAIT) | SA_SIGINFO)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 319
try:
    SIG_BLOCK = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 320
try:
    SIG_UNBLOCK = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 321
try:
    SIG_SETMASK = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 324
try:
    SI_USER = 0x10001
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 325
try:
    SI_QUEUE = 0x10002
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 326
try:
    SI_TIMER = 0x10003
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 327
try:
    SI_ASYNCIO = 0x10004
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 328
try:
    SI_MESGQ = 0x10005
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 338
try:
    SS_ONSTACK = 0x0001
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 339
try:
    SS_DISABLE = 0x0004
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 340
try:
    MINSIGSTKSZ = 32768
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 341
try:
    SIGSTKSZ = 131072
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 354
try:
    SV_ONSTACK = SA_ONSTACK
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 355
try:
    SV_INTERRUPT = SA_RESTART
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 356
try:
    SV_RESETHAND = SA_RESETHAND
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 357
try:
    SV_NODEFER = SA_NODEFER
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 358
try:
    SV_NOCLDSTOP = SA_NOCLDSTOP
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 359
try:
    SV_SIGINFO = SA_SIGINFO
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 377
def sigmask(m):
    return (1 << (m - 1))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 380
try:
    BADSIG = SIG_ERR
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 10
try:
    __WORDSIZE = 64
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 62
def INT8_C(v):
    return v

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 63
def INT16_C(v):
    return v

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 64
def INT32_C(v):
    return v

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 67
def UINT8_C(v):
    return v

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 68
def UINT16_C(v):
    return v

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 91
try:
    INT8_MAX = 127
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 92
try:
    INT16_MAX = 32767
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 93
try:
    INT32_MAX = 2147483647
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 94
try:
    INT64_MAX = 9223372036854775807
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 96
try:
    INT8_MIN = (-128)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 97
try:
    INT16_MIN = (-32768)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 104
try:
    INT32_MIN = ((-INT32_MAX) - 1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 105
try:
    INT64_MIN = ((-INT64_MAX) - 1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 107
try:
    UINT8_MAX = 255
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 108
try:
    UINT16_MAX = 65535
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 109
try:
    UINT32_MAX = 4294967295
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 110
try:
    UINT64_MAX = 18446744073709551615
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 113
try:
    INT_LEAST8_MIN = INT8_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 114
try:
    INT_LEAST16_MIN = INT16_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 115
try:
    INT_LEAST32_MIN = INT32_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 116
try:
    INT_LEAST64_MIN = INT64_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 118
try:
    INT_LEAST8_MAX = INT8_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 119
try:
    INT_LEAST16_MAX = INT16_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 120
try:
    INT_LEAST32_MAX = INT32_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 121
try:
    INT_LEAST64_MAX = INT64_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 123
try:
    UINT_LEAST8_MAX = UINT8_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 124
try:
    UINT_LEAST16_MAX = UINT16_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 125
try:
    UINT_LEAST32_MAX = UINT32_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 126
try:
    UINT_LEAST64_MAX = UINT64_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 129
try:
    INT_FAST8_MIN = INT8_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 130
try:
    INT_FAST16_MIN = INT16_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 131
try:
    INT_FAST32_MIN = INT32_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 132
try:
    INT_FAST64_MIN = INT64_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 134
try:
    INT_FAST8_MAX = INT8_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 135
try:
    INT_FAST16_MAX = INT16_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 136
try:
    INT_FAST32_MAX = INT32_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 137
try:
    INT_FAST64_MAX = INT64_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 139
try:
    UINT_FAST8_MAX = UINT8_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 140
try:
    UINT_FAST16_MAX = UINT16_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 141
try:
    UINT_FAST32_MAX = UINT32_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 142
try:
    UINT_FAST64_MAX = UINT64_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 147
try:
    INTPTR_MAX = 9223372036854775807
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 151
try:
    INTPTR_MIN = ((-INTPTR_MAX) - 1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 154
try:
    UINTPTR_MAX = 18446744073709551615
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 173
try:
    SIZE_MAX = UINTPTR_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 176
try:
    RSIZE_MAX = (SIZE_MAX >> 1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 181
try:
    WCHAR_MAX = __WCHAR_MAX__
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 195
try:
    WCHAR_MIN = ((-WCHAR_MAX) - 1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 199
try:
    WINT_MIN = INT32_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 200
try:
    WINT_MAX = INT32_MAX
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 202
try:
    SIG_ATOMIC_MIN = INT32_MIN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdint.h: 203
try:
    SIG_ATOMIC_MAX = INT32_MAX
except:
    pass

_STRUCT_TIMEVAL = struct_timeval# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_timeval.h: 29

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 100
try:
    PRIO_PROCESS = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 101
try:
    PRIO_PGRP = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 102
try:
    PRIO_USER = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 105
try:
    PRIO_DARWIN_THREAD = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 106
try:
    PRIO_DARWIN_PROCESS = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 112
try:
    PRIO_MIN = (-20)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 113
try:
    PRIO_MAX = 20
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 120
try:
    PRIO_DARWIN_BG = 0x1000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 126
try:
    PRIO_DARWIN_NONUI = 0x1001
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 140
try:
    RUSAGE_SELF = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 141
try:
    RUSAGE_CHILDREN = (-1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 186
try:
    RUSAGE_INFO_V0 = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 187
try:
    RUSAGE_INFO_V1 = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 188
try:
    RUSAGE_INFO_V2 = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 189
try:
    RUSAGE_INFO_V3 = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 190
try:
    RUSAGE_INFO_V4 = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 191
try:
    RUSAGE_INFO_V5 = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 192
try:
    RUSAGE_INFO_V6 = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 193
try:
    RUSAGE_INFO_CURRENT = RUSAGE_INFO_V6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 198
try:
    RU_PROC_RUNS_RESLIDE = 0x00000001
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 430
try:
    RLIM_INFINITY = (((__uint64_t (ord_if_char(1))).value << 63) - 1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 431
try:
    RLIM_SAVED_MAX = RLIM_INFINITY
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 432
try:
    RLIM_SAVED_CUR = RLIM_INFINITY
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 438
try:
    RLIMIT_CPU = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 439
try:
    RLIMIT_FSIZE = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 440
try:
    RLIMIT_DATA = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 441
try:
    RLIMIT_STACK = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 442
try:
    RLIMIT_CORE = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 443
try:
    RLIMIT_AS = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 445
try:
    RLIMIT_RSS = RLIMIT_AS
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 446
try:
    RLIMIT_MEMLOCK = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 447
try:
    RLIMIT_NPROC = 7
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 449
try:
    RLIMIT_NOFILE = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 451
try:
    RLIM_NLIMITS = 9
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 453
try:
    _RLIMIT_POSIX_FLAG = 0x1000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 470
try:
    RLIMIT_WAKEUPS_MONITOR = 0x1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 471
try:
    RLIMIT_CPU_USAGE_MONITOR = 0x2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 472
try:
    RLIMIT_THREAD_CPULIMITS = 0x3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 473
try:
    RLIMIT_FOOTPRINT_INTERVAL = 0x4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 478
try:
    WAKEMON_ENABLE = 0x01
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 479
try:
    WAKEMON_DISABLE = 0x02
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 480
try:
    WAKEMON_GET_PARAMS = 0x04
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 481
try:
    WAKEMON_SET_DEFAULTS = 0x08
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 482
try:
    WAKEMON_MAKE_FATAL = 0x10
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 487
try:
    CPUMON_MAKE_FATAL = 0x1000
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 492
try:
    FOOTPRINT_INTERVAL_RESET = 0x1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 502
try:
    IOPOL_TYPE_DISK = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 503
try:
    IOPOL_TYPE_VFS_ATIME_UPDATES = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 504
try:
    IOPOL_TYPE_VFS_MATERIALIZE_DATALESS_FILES = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 505
try:
    IOPOL_TYPE_VFS_STATFS_NO_DATA_VOLUME = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 506
try:
    IOPOL_TYPE_VFS_TRIGGER_RESOLVE = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 507
try:
    IOPOL_TYPE_VFS_IGNORE_CONTENT_PROTECTION = 6
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 508
try:
    IOPOL_TYPE_VFS_IGNORE_PERMISSIONS = 7
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 509
try:
    IOPOL_TYPE_VFS_SKIP_MTIME_UPDATE = 8
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 510
try:
    IOPOL_TYPE_VFS_ALLOW_LOW_SPACE_WRITES = 9
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 511
try:
    IOPOL_TYPE_VFS_DISALLOW_RW_FOR_O_EVTONLY = 10
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 514
try:
    IOPOL_SCOPE_PROCESS = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 515
try:
    IOPOL_SCOPE_THREAD = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 516
try:
    IOPOL_SCOPE_DARWIN_BG = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 519
try:
    IOPOL_DEFAULT = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 520
try:
    IOPOL_IMPORTANT = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 521
try:
    IOPOL_PASSIVE = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 522
try:
    IOPOL_THROTTLE = 3
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 523
try:
    IOPOL_UTILITY = 4
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 524
try:
    IOPOL_STANDARD = 5
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 527
try:
    IOPOL_APPLICATION = IOPOL_STANDARD
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 528
try:
    IOPOL_NORMAL = IOPOL_IMPORTANT
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 531
try:
    IOPOL_ATIME_UPDATES_DEFAULT = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 532
try:
    IOPOL_ATIME_UPDATES_OFF = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 534
try:
    IOPOL_MATERIALIZE_DATALESS_FILES_DEFAULT = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 535
try:
    IOPOL_MATERIALIZE_DATALESS_FILES_OFF = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 536
try:
    IOPOL_MATERIALIZE_DATALESS_FILES_ON = 2
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 538
try:
    IOPOL_VFS_STATFS_NO_DATA_VOLUME_DEFAULT = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 539
try:
    IOPOL_VFS_STATFS_FORCE_NO_DATA_VOLUME = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 541
try:
    IOPOL_VFS_TRIGGER_RESOLVE_DEFAULT = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 542
try:
    IOPOL_VFS_TRIGGER_RESOLVE_OFF = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 544
try:
    IOPOL_VFS_CONTENT_PROTECTION_DEFAULT = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 545
try:
    IOPOL_VFS_CONTENT_PROTECTION_IGNORE = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 547
try:
    IOPOL_VFS_IGNORE_PERMISSIONS_OFF = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 548
try:
    IOPOL_VFS_IGNORE_PERMISSIONS_ON = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 550
try:
    IOPOL_VFS_SKIP_MTIME_UPDATE_OFF = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 551
try:
    IOPOL_VFS_SKIP_MTIME_UPDATE_ON = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 553
try:
    IOPOL_VFS_ALLOW_LOW_SPACE_WRITES_OFF = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 554
try:
    IOPOL_VFS_ALLOW_LOW_SPACE_WRITES_ON = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 556
try:
    IOPOL_VFS_DISALLOW_RW_FOR_O_EVTONLY_DEFAULT = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 557
try:
    IOPOL_VFS_DISALLOW_RW_FOR_O_EVTONLY_ON = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 121
try:
    WNOHANG = 0x00000001
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 122
try:
    WUNTRACED = 0x00000002
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 131
def _W_INT(w):
    return (cast(pointer(w), POINTER(c_int))[0])

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 132
try:
    WCOREFLAG = 0o200
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 136
def _WSTATUS(x):
    return ((_W_INT (x)) & 0o177)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 137
try:
    _WSTOPPED = 0o177
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 144
def WEXITSTATUS(x):
    return (((_W_INT (x)) >> 8) & 0x000000ff)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 149
def WSTOPSIG(x):
    return ((_W_INT (x)) >> 8)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 150
def WIFCONTINUED(x):
    return (((_WSTATUS (x)) == _WSTOPPED) and ((WSTOPSIG (x)) == 0x13))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 151
def WIFSTOPPED(x):
    return (((_WSTATUS (x)) == _WSTOPPED) and ((WSTOPSIG (x)) != 0x13))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 152
def WIFEXITED(x):
    return ((_WSTATUS (x)) == 0)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 153
def WIFSIGNALED(x):
    return (((_WSTATUS (x)) != _WSTOPPED) and ((_WSTATUS (x)) != 0))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 154
def WTERMSIG(x):
    return (_WSTATUS (x))

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 156
def WCOREDUMP(x):
    return ((_W_INT (x)) & WCOREFLAG)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 158
def W_EXITCODE(ret, sig):
    return ((ret << 8) | sig)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 159
def W_STOPCODE(sig):
    return ((sig << 8) | _WSTOPPED)

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 168
try:
    WEXITED = 0x00000004
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 171
try:
    WSTOPPED = 0x00000008
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 173
try:
    WCONTINUED = 0x00000010
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 174
try:
    WNOWAIT = 0x00000020
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 183
try:
    WAIT_ANY = (-1)
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 184
try:
    WAIT_MYPGRP = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 80
try:
    _QUAD_HIGHWORD = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 81
try:
    _QUAD_LOWWORD = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 87
try:
    __DARWIN_LITTLE_ENDIAN = 1234
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 88
try:
    __DARWIN_BIG_ENDIAN = 4321
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 89
try:
    __DARWIN_PDP_ENDIAN = 3412
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 91
try:
    __DARWIN_BYTE_ORDER = __DARWIN_LITTLE_ENDIAN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 95
try:
    LITTLE_ENDIAN = __DARWIN_LITTLE_ENDIAN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 96
try:
    BIG_ENDIAN = __DARWIN_BIG_ENDIAN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 97
try:
    PDP_ENDIAN = __DARWIN_PDP_ENDIAN
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/endian.h: 99
try:
    BYTE_ORDER = __DARWIN_BYTE_ORDER
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/libkern/_OSByteOrder.h: 43
def __DARWIN_OSSwapConstInt16(x):
    return (__uint16_t (ord_if_char(((((__uint16_t (ord_if_char(x))).value & 0xff00) >> 8) | (((__uint16_t (ord_if_char(x))).value & 0x00ff) << 8))))).value

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/libkern/_OSByteOrder.h: 47
def __DARWIN_OSSwapConstInt32(x):
    return (__uint32_t (ord_if_char(((((((__uint32_t (ord_if_char(x))).value & 0xff000000) >> 24) | (((__uint32_t (ord_if_char(x))).value & 0x00ff0000) >> 8)) | (((__uint32_t (ord_if_char(x))).value & 0x0000ff00) << 8)) | (((__uint32_t (ord_if_char(x))).value & 0x000000ff) << 24))))).value

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/libkern/_OSByteOrder.h: 53
def __DARWIN_OSSwapConstInt64(x):
    return (__uint64_t (ord_if_char(((((((((((__uint64_t (ord_if_char(x))).value & 0xff00000000000000) >> 56) | (((__uint64_t (ord_if_char(x))).value & 0x00ff000000000000) >> 40)) | (((__uint64_t (ord_if_char(x))).value & 0x0000ff0000000000) >> 24)) | (((__uint64_t (ord_if_char(x))).value & 0x000000ff00000000) >> 8)) | (((__uint64_t (ord_if_char(x))).value & 0x00000000ff000000) << 8)) | (((__uint64_t (ord_if_char(x))).value & 0x0000000000ff0000) << 24)) | (((__uint64_t (ord_if_char(x))).value & 0x000000000000ff00) << 40)) | (((__uint64_t (ord_if_char(x))).value & 0x00000000000000ff) << 56))))).value

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 102
try:
    EXIT_FAILURE = 1
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 103
try:
    EXIT_SUCCESS = 0
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 105
try:
    RAND_MAX = 0x7fffffff
except:
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/stdlib.h: 119
try:
    MB_CUR_MAX = __mb_cur_max
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 228
try:
    OM_VERSION = 108
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 434
try:
    OM_MEMORY_HEALTH_ERROR = 1
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 435
try:
    OM_MEMORY_HEALTH_WARNING = 8
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 656
try:
    OM_METADATA_SIZE = 448
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 735
def OmClearDataAndCommit(_deviceId):
    return (OmEraseDataAndCommit (_deviceId, OM_ERASE_QUICKFORMAT))

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 748
def OmCommit(_deviceId):
    return (OmEraseDataAndCommit (_deviceId, OM_ERASE_NONE))

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 756
try:
    OM_ACCEL_DEFAULT_RATE = 100
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 764
try:
    OM_ACCEL_DEFAULT_RANGE = 8
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 843
try:
    OM_MAX_PATH = 256
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1020
try:
    OM_TRUE = 1
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1021
try:
    OM_FALSE = 0
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1022
try:
    OM_OK = 0
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1023
try:
    OM_E_FAIL = (-1)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1024
try:
    OM_E_UNEXPECTED = (-2)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1025
try:
    OM_E_NOT_VALID_STATE = (-3)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1026
try:
    OM_E_OUT_OF_MEMORY = (-4)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1027
try:
    OM_E_INVALID_ARG = (-5)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1028
try:
    OM_E_POINTER = (-6)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1029
try:
    OM_E_NOT_IMPLEMENTED = (-7)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1030
try:
    OM_E_ABORT = (-8)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1031
try:
    OM_E_ACCESS_DENIED = (-9)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1032
try:
    OM_E_INVALID_DEVICE = (-10)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1033
try:
    OM_E_UNEXPECTED_RESPONSE = (-11)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1034
try:
    OM_E_LOCKED = (-12)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1035
def OM_SUCCEEDED(value):
    return (value >= 0)

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1036
def OM_FAILED(value):
    return (value < 0)

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1076
def OM_DATETIME_FROM_YMDHMS(year, month, day, hours, minutes, seconds):
    return ((((((((OM_DATETIME (ord_if_char((year % 100)))).value & 0x3f) << 26) | (((OM_DATETIME (ord_if_char(month))).value & 0x0f) << 22)) | (((OM_DATETIME (ord_if_char(day))).value & 0x1f) << 17)) | (((OM_DATETIME (ord_if_char(hours))).value & 0x1f) << 12)) | (((OM_DATETIME (ord_if_char(minutes))).value & 0x3f) << 6)) | ((OM_DATETIME (ord_if_char(seconds))).value & 0x3f))

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1084
def OM_DATETIME_YEAR(dateTime):
    return ((c_uint (ord_if_char((c_ubyte (ord_if_char(((dateTime >> 26) & 0x3f)))).value))).value + 2000)

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1085
def OM_DATETIME_MONTH(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 22) & 0x0f)))).value

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1086
def OM_DATETIME_DAY(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 17) & 0x1f)))).value

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1087
def OM_DATETIME_HOURS(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 12) & 0x1f)))).value

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1088
def OM_DATETIME_MINUTES(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 6) & 0x3f)))).value

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1089
def OM_DATETIME_SECONDS(dateTime):
    return (c_ubyte (ord_if_char((dateTime & 0x3f)))).value

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1090
try:
    OM_DATETIME_MIN_VALID = (OM_DATETIME_FROM_YMDHMS (2000, 1, 1, 0, 0, 0))
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1091
try:
    OM_DATETIME_MAX_VALID = (OM_DATETIME_FROM_YMDHMS (2063, 12, 31, 23, 59, 59))
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1092
try:
    OM_DATETIME_ZERO = 0
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1093
try:
    OM_DATETIME_INFINITE = (OM_DATETIME (ord_if_char((-1)))).value
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1096
try:
    OM_DATETIME_BUFFER_SIZE = 20
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1137
try:
    OM_MAX_SAMPLES = 120
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1144
try:
    OM_MAX_HEADER_SIZE = (2 * 512)
except:
    pass

# /Users/mcrooks/Desktop/RightStep/RIGHTSTEP/CODE/libomapi/bindings/rs-python/c/omapi.h: 1151
try:
    OM_MAX_DATA_SIZE = 512
except:
    pass

__darwin_pthread_handler_rec = struct___darwin_pthread_handler_rec# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 57

_opaque_pthread_attr_t = struct__opaque_pthread_attr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 63

_opaque_pthread_cond_t = struct__opaque_pthread_cond_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 68

_opaque_pthread_condattr_t = struct__opaque_pthread_condattr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 73

_opaque_pthread_mutex_t = struct__opaque_pthread_mutex_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 78

_opaque_pthread_mutexattr_t = struct__opaque_pthread_mutexattr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 83

_opaque_pthread_once_t = struct__opaque_pthread_once_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 88

_opaque_pthread_rwlock_t = struct__opaque_pthread_rwlock_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 93

_opaque_pthread_rwlockattr_t = struct__opaque_pthread_rwlockattr_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 98

_opaque_pthread_t = struct__opaque_pthread_t# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h: 103

__darwin_i386_thread_state = struct___darwin_i386_thread_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 48

__darwin_fp_control = struct___darwin_fp_control# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 94

__darwin_fp_status = struct___darwin_fp_status# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 152

__darwin_mmst_reg = struct___darwin_mmst_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 196

__darwin_xmm_reg = struct___darwin_xmm_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 215

__darwin_ymm_reg = struct___darwin_ymm_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 231

__darwin_zmm_reg = struct___darwin_zmm_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 247

__darwin_opmask_reg = struct___darwin_opmask_reg# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 261

__darwin_i386_float_state = struct___darwin_i386_float_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 283

__darwin_i386_avx_state = struct___darwin_i386_avx_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 320

__darwin_i386_avx512_state = struct___darwin_i386_avx512_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 366

__darwin_i386_exception_state = struct___darwin_i386_exception_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 577

__darwin_x86_debug_state32 = struct___darwin_x86_debug_state32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 597

__x86_instruction_state = struct___x86_instruction_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 610

__last_branch_record = struct___last_branch_record# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 626

__last_branch_state = struct___last_branch_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 638

__x86_pagein_state = struct___x86_pagein_state# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 704

__darwin_x86_thread_state64 = struct___darwin_x86_thread_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 715

__darwin_x86_thread_full_state64 = struct___darwin_x86_thread_full_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 773

__darwin_x86_float_state64 = struct___darwin_x86_float_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 796

__darwin_x86_avx_state64 = struct___darwin_x86_avx_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 847

__darwin_x86_avx512_state64 = struct___darwin_x86_avx512_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 915

__darwin_x86_exception_state64 = struct___darwin_x86_exception_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1254

__darwin_x86_debug_state64 = struct___darwin_x86_debug_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1274

__darwin_x86_cpmu_state64 = struct___darwin_x86_cpmu_state64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/i386/_structs.h: 1302

__darwin_mcontext32 = struct___darwin_mcontext32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 41

__darwin_mcontext_avx32 = struct___darwin_mcontext_avx32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 49

__darwin_mcontext_avx512_32 = struct___darwin_mcontext_avx512_32# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 58

__darwin_mcontext64 = struct___darwin_mcontext64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 99

__darwin_mcontext64_full = struct___darwin_mcontext64_full# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 107

__darwin_mcontext_avx64 = struct___darwin_mcontext_avx64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 115

__darwin_mcontext_avx64_full = struct___darwin_mcontext_avx64_full# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 123

__darwin_mcontext_avx512_64 = struct___darwin_mcontext_avx512_64# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 132

__darwin_mcontext_avx512_64_full = struct___darwin_mcontext_avx512_64_full# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_mcontext.h: 140

__darwin_sigaltstack = struct___darwin_sigaltstack# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigaltstack.h: 42

__darwin_ucontext = struct___darwin_ucontext# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_ucontext.h: 43

sigval = union_sigval# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 158

sigevent = struct_sigevent# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 168

__siginfo = struct___siginfo# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 188

__sigaction_u = union___sigaction_u# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 269

__sigaction = struct___sigaction# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 276

sigaction = struct_sigaction# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 286

sigvec = struct_sigvec# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 348

sigstack = struct_sigstack# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/signal.h: 367

timeval = struct_timeval# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_timeval.h: 34

rusage = struct_rusage# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 152

rusage_info_v0 = struct_rusage_info_v0# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 202

rusage_info_v1 = struct_rusage_info_v1# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 216

rusage_info_v2 = struct_rusage_info_v2# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 236

rusage_info_v3 = struct_rusage_info_v3# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 258

rusage_info_v4 = struct_rusage_info_v4# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 289

rusage_info_v5 = struct_rusage_info_v5# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 328

rusage_info_v6 = struct_rusage_info_v6# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 368

rlimit = struct_rlimit# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 459

proc_rlimit_control_wakeupmon = struct_proc_rlimit_control_wakeupmon# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/resource.h: 494

wait = union_wait# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/wait.h: 194

# No inserted files

# No prefix-stripping

