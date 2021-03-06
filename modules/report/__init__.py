import os
from package.utils import Utils

class ModuleParent:
    def __init__(self, internal_path, external_path, report_path, app_name, app_id):
        # self.report_path = os.path.join(report_path, "report", self.report_name)
        self.report_path = report_path
        Utils.check_and_generate_folder(self.report_path)

        self.internal_cache_path = internal_path
        self.external_cache_path = external_path
        Utils.check_and_generate_folder(self.internal_cache_path)
        Utils.check_and_generate_folder(self.external_cache_path)

        self.databases = self.set_databases()
        self.shared_preferences = self.set_shared_preferences()
        
        self.report = {}
        self.app_name = app_name
        self.app_id = app_id
        
        self.set_header()

    def get_databases(self):
        return self.databases
    
    def get_shared_preferences(self):
        return self.shared_preferences

    def set_databases(self):
        dbs = []
        dbs.extend(Utils.list_files(self.internal_cache_path, [".db"]))
        dbs.extend(Utils.list_files(self.external_cache_path, [".db"]))
        return dbs

    def set_shared_preferences(self):
        files = []
        for xmlfile in Utils.list_files(self.internal_cache_path, [".xml"]):
            if '/shared_prefs/' in xmlfile or '\\shared_prefs\\' in xmlfile:
                files.append(xmlfile)
        
        return files
    
    def set_header(self):
        self.report = {}
        self.report["header"] = {
            "report_name": Utils.get_current_time(),
            "report_date": Utils.get_current_millis(),
            "app_name" : self.app_name,
            "app_id": self.app_id
        }

    def generate_report(self):
        raise NotImplementedError
