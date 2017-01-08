import os
import paths


class Context(object):
    ROOT_DIR = paths.ROOT_DIR
    BASE_URL = None


class AllureWrapper(object):

    DIRECTORY_WITH_RESULTS = 'allure'
    DIRECTORY_WITH_REPORT = 'allure'

    @staticmethod
    def get_allure_command():
        command = 'allure generate ' + \
                  os.path.join(Context.ROOT_DIR, AllureWrapper.DIRECTORY_WITH_REPORT) + \
                  ' ' + \
                  '-o ' + os.path.join(Context.ROOT_DIR, AllureWrapper.DIRECTORY_WITH_RESULTS)

        return command
