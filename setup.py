from distutils.core import setup, Extension
incs = ['include']
mods = ['ccid', 'emv']
exts = [Extension(x, ['src/py_%s.c'%x],
			library_dirs=['./src/.libs/'],
			libraries=[x],
			include_dirs=incs)
	for x in mods]
setup(name='ccid-utils', version='0.4', ext_modules=exts)
