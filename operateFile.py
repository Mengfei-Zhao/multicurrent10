import os


class OperateFile:
    def getCurrentWorkPath(self):
        """get the directory path of this file, and it is also the current work path.

        Return: 
            workDir\
        """
        currentWorkPath = os.getcwd()
        # print('currentWorkPath is', currentWorkPath)
        return currentWorkPath

    def openDocumentation(self, fileName):
        """open documentation.

        Args:
            fileName (str): such as documentation.md
        Return: 
            None
        """
        # currentWorkPath = self.getCurrentWorkPath()
        # absPathOfDocumentation = os.path.join(
        #     currentWorkPath, "doc", fileName)
        absPathOfDocumentation = os.path.join("doc", fileName)
        # print('absPathOfDocumentation is: ', absPathOfDocumentation)
        os.startfile(str(absPathOfDocumentation))
