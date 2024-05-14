#!/usr/bin/env python3
#** *****************************************************************************
# *
# * If not stated otherwise in this file or this component's LICENSE file the
# * following copyright and licenses apply:
# *
# * Copyright 2023 RDK Management
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *
# http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *
#* ******************************************************************************

import os
import sys



# Add the framework path to system
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/../../")

from framework.core.testControl import testController

class saveScreenshotTest(testController):
    def __init__(self, testName="saveScreenshotTest", log=None):
        super().__init__(testName=testName, log=log)
        self.run()

    def testFunction(self):
        webpageControl = self.webpageController

        webpageConfig = self.config.decodeConfigIntoDictionary("./unitTests/framework/webControlTests/webPageTest.yml")
        webpageControl.configureWebpages("https://testpages.herokuapp.com/styled", webpageConfig)

        webpageControl.navigateTo("form_page")

        self.log.stepStart("Attempting to save snapshot of html and checking it exists")
        webpageControl.saveHtmlSnapshot("formPage")
        expectedLocation = f"{self.log.logPath}browser/formPage.html"
        if os.path.isfile(expectedLocation):
            self.log.stepResult(True, "Snapshot has been successfully saved")
        else:
            self.log.stepResult(False, f"Snapshot has not been successfully saved in the expected location: {expectedLocation}")

        self.log.stepStart("Attempting to save screenshot of page and checking it exists")
        webpageControl.saveScreenshot("formPage")
        expectedLocation = f"{self.log.logPath}browser/formPage.png"
        if os.path.isfile(expectedLocation):
            self.log.stepResult(True, "Screenshot has been successfully saved")
        else:
            self.log.stepResult(False, f"Screenshot has not been successfully saved in the expected location: {expectedLocation}")


if __name__ == "__main__":
    test = saveScreenshotTest()

    
