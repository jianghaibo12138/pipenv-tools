import os
import shutil
import stat

USR_LOCAL_BIN_NAME = "/usr/local/bin"

PIPH_FILE_NAME = "piph.py"
PIPH_FILE_SH_NAME = "piph"

PIPH_FILE_PATH = os.path.join(os.getcwd(), PIPH_FILE_NAME)
PIPH_FILE_SH_PATH = os.path.join(os.getcwd(), PIPH_FILE_SH_NAME)

shutil.copyfile(PIPH_FILE_PATH, PIPH_FILE_SH_PATH)

os.chmod(PIPH_FILE_SH_PATH, stat.S_IXOTH | stat.S_IWOTH | stat.S_IROTH | stat.S_IXUSR | stat.S_IWUSR | stat.S_IRUSR)
shutil.move(PIPH_FILE_SH_PATH, USR_LOCAL_BIN_NAME)
