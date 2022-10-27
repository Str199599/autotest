import yaml
import os

def readYaml(path):
    with open(path,"r+",encoding="utf-8") as file:
        data = yaml.load(stream=file,Loader=yaml.FullLoader)
        return data

if __name__=='__main__':
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(rootPath,"config\config.yaml")
    print(rootPath)
    print(readYaml(path)["desired_caps"])