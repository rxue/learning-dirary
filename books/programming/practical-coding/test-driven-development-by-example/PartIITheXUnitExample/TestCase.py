class TestCase:
    def __init__(self, name):
        self.name= name
    def setUp(self):
        pass
    def run(self):
        method = getattr(self, self.name)
        method()
class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.wasRun= None

    def setUp(self):
        self.wasRun= None
        self.wasSetUp= 1

    def testMethod(self):
        self.wasRun= True

class TestCaseTest(TestCase):
    def setUp(self):
        self.test= WasRun("testMethod")
    def testRunning(self):
        assert(not self.test.wasRun)
        self.test.run()
        assert(self.test.wasRun)
    def testSetUp(self):
        self.test.run()
        assert(self.self.test.wasSetUp)
if __name__ == '__main__':
    t = TestCaseTest("testRunning")
    t.setUp()
    t.run()