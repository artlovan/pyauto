import os
import paths


class Context(object):
    class Path:
        ROOT_DIR = paths.ROOT_DIR

    class Url:
        BASE_URL = None

    class Excel:
        excel_data = None
        excel_path = None


class MockContext(Context):
    MOCK_ACTIVATE = False
    ALLURE_REPORT = False


class AllureWrapper(object):

    DIRECTORY_WITH_RESULTS = 'allure'
    DIRECTORY_WITH_REPORT = 'allure'

    @staticmethod
    def get_allure_command():
        command = 'allure generate ' + \
                  os.path.join(Context.Path.ROOT_DIR, AllureWrapper.DIRECTORY_WITH_REPORT) + \
                  ' ' + \
                  '-o ' + os.path.join(Context.Path.ROOT_DIR, AllureWrapper.DIRECTORY_WITH_RESULTS)

        return command
