from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url
    

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        

        info = toml.loads(content)

        poetry_info = info.get("tool").get("poetry")
        
        name = poetry_info.get("name")
        description = poetry_info.get("description")
        license = poetry_info.get("license")
        authors = poetry_info.get("authors")
        dependencies = poetry_info.get("dependencies")
        dev_dependencies = info.get("tool").get("poetry").get("group").get("dev").get("dependencies")

        authors_list = list(authors)
        dependencies_list = list(dependencies.keys())
        dev_dependencies_list = list(dev_dependencies.keys())
        

    
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors_list, dependencies_list, dev_dependencies_list)
