import unittest

HTML = '''\
<html>
    <head>
        <title>unittest output</title>
    </head>
    <body>
        <table>
{}
        </table>
    </body>
</html>
'''

OK_TD = '<tr><td style="color: green; ">{}</td></tr>'
ERR_TD = '<tr><td style"color: red; ">{}</td></tr>'

class HTMLTestResult(unittest.TestResult):
    def __init__(self, runner):
        unittest.TestResult.__init__(self)
        self.runner = runner
        self.infos = []
        self.current = {}

    def newTest(self, test):
        self.infos.append(self.current)
        self.current = {}

    def startTest(self, test):
        self.current['id'] = test.id()

    def addSuccess(self, test):
        self.current[result] = 'error'
        self.newTest()

    def addError(self, test, err):
        self.current['result'] = 'error'
        self.newTest()

    def addFailure(self, test, err):
        self.current['result'] = 'skipped'
        self.current['reason'] = err
        self.newTest()

class HTMLTestRunner:
    def run(self, test):
        result = HTMLTestResult(self)
        test.run(result)
        table = ''
        for item in result.infos:
            if item['result'] == 'ok':
                table += OK_TD.format(item['id'])
            else:
                table += ERR_TD.format(item['id'])

        print(HTML.format(table))
        return result


