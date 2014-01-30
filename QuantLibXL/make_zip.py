
import sys
import os
import shutil
import datetime
import glob
import zipfile

QLXL_VERSION = "QuantLibXL-1.3.0"
ROOT_DIR = QLXL_VERSION + "/"

def prompt_exit(msg='', status=0):
    if msg:
        print msg
    if sys.platform == 'win32':
        raw_input('press any key to exit')
    sys.exit(status)

def visit(params, dirname, names):
    zfile = params[0]
    exclude = params[1]
    strip = params[2]
    if strip:
        rootDir = dirname[len(strip):]
    else:
        rootDir = dirname
    for name in names:
        if exclude == name: continue
        sourcePath = dirname + "/" + name
        targetPath = rootDir + "/" + name
        zfile.write(sourcePath, ROOT_DIR + targetPath)

zipFilePath = "zip/%s-%s.zip" % (QLXL_VERSION, datetime.datetime.now().strftime("%Y%m%d%H%M"))
zfile = zipfile.ZipFile(zipFilePath, "w", zipfile.ZIP_DEFLATED)

# Zip up some specific files from the QuantLibXL directory.
zfile.write("Docs/QuantLibXL-docs-1.3.0.chm", ROOT_DIR + "Docs/QuantLibXL-docs-1.3.0.chm")
zfile.write("xll/QuantLibXLDynamic-vc90-mt-1_3_0.xll", ROOT_DIR + "xll/QuantLibXLDynamic-vc90-mt-1_3_0.xll")
zfile.write("zip/README.txt", ROOT_DIR + "README.txt")
# Recursively zip some subdirectories of the QuantLibXL directory.
#os.path.walk("Data", visit, (zfile, ".gitignore", None))
os.path.walk("Data2/XLS", visit, (zfile, ".gitignore", None))
os.path.walk("framework", visit, (zfile, "ReadMe.txt", None))
#os.path.walk("Workbooks", visit, (zfile, None, None))
# Zip up some files from other projects in the repo.
zfile.write("../ObjectHandler/xll/ObjectHandler-xll-vc90-mt-1_3_0.xll", ROOT_DIR + "xll/ObjectHandler-xll-vc90-mt-1_3_0.xll")
os.path.walk("../QuantLibAddin/gensrc/metadata", visit, (zfile, None, "../QuantLibAddin/gensrc/"))
zfile.write("../XL-Launcher/bin/Addin/Launcher.xla", ROOT_DIR + "Launcher.xla")
zfile.write("../XL-Launcher/bin/Addin/session_file.zipfile.xml", ROOT_DIR + "session_file.xml")
for fileName in glob.glob("../XL-Launcher/bin/Addin/session_file.*.xml"):
    baseName = os.path.basename(fileName)
    if "session_file.zipfile.xml" == baseName: continue
    zfile.write("../XL-Launcher/bin/Addin/" + baseName, ROOT_DIR + baseName)

zfile.close()

