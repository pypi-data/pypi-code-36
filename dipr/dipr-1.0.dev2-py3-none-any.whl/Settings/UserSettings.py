
from shutil import copyfile
from pathlib import Path

from Settings.RepoSettings import RepoSettings


class UserSettings(object):

    DIPRC_DIRECTORY = '.diprc'

    def __init__(self, global_settings):
        self.global_settings = global_settings
        self.user_home = Path.home()

        self.dip_rc_directory_path = Path(self.user_home, UserSettings.DIPRC_DIRECTORY)
        self.dip_src_template_file_path = Path(self.dip_rc_directory_path, RepoSettings.DIPR_SRC_FILE)
        self.dip_dep_template_file_path = Path(self.dip_rc_directory_path, RepoSettings.DIPR_DEP_FILE)
        self.dip_sub_template_file_path = Path(self.dip_rc_directory_path, RepoSettings.DIPR_SUB_FILE)

    @property
    def is_initialized(self):
        return self.dip_rc_directory_path.is_dir() and \
               self.dip_src_template_file_path.is_file() and \
               self.dip_dep_template_file_path.is_file() and \
               self.dip_sub_template_file_path.is_file()

    @staticmethod
    def __init_repo_file(source_path, destination_path, force):
        if force and destination_path.is_file():
            destination_path.unlink()

        if not destination_path.is_file():
            if source_path.is_file():
                copyfile(source_path, destination_path)

    def initialize(self, force=False):
        if not force and self.is_initialized:
            return

        if not self.dip_rc_directory_path.is_dir():
            self.dip_rc_directory_path.mkdir()

        UserSettings.__init_repo_file(self.global_settings.dip_src_template_file_path, self.dip_src_template_file_path, force)
        UserSettings.__init_repo_file(self.global_settings.dip_dep_template_file_path, self.dip_dep_template_file_path, force)
        UserSettings.__init_repo_file(self.global_settings.dip_sub_template_file_path, self.dip_sub_template_file_path, force)



