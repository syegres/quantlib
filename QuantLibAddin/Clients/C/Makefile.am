
AM_CPPFLAGS = -I${top_srcdir}
LDADD = ../../Addins/C/libQuantLibAddinC.la
LDFLAGS = -lObjectHandler -lQuantLib -lstdc++

EXTRA_DIST = \
    ClientCDemo_vc8.vcproj \
    ClientCDemo_vc7.vcproj

QLADemo_SOURCES = qlademo.c

if BUILD_C
noinst_PROGRAMS = QLADemo
else
EXTRA_PROGRAMS = QLADemo
endif

