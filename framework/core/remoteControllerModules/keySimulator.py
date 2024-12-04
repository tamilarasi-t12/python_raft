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
#*
#*   ** Project      : RAFT
#*   ** @addtogroup  : core.remoteControllerModules
#*   ** @date        : 27/11/2024
#*   **
#*   ** @brief : remote keySimulator
#*   **
#* ******************************************************************************
import os
import time
import subprocess
from framework.core.logModule import logModule
from framework.core.commandModules.sshConsole import sshConsole
from framework.core.rcCodes import rcCode as rc


class KeySimulator:

    def __init__(self, log: logModule, remoteConfig: dict):
        """Initialize the KeySimulator class.

        Args:
            log (logModule): Logging module instance.
            remoteConfig (dict): Key simulator configuration.
        """
        self.log = log
        self.remoteConfig = remoteConfig
        self.prompt = r"\$ "

        # Initialize SSH session
        self.session = sshConsole(
            address=self.remoteConfig.get("ip"),
            username=self.remoteConfig.get("username"),
            password=self.remoteConfig.get("password"),
            known_hosts=self.remoteConfig.get("known_hosts"),
            port=int(self.remoteConfig.get("port")),
        )


    def sendKey(self, key: rc, repeat: int , delay: int ):
        """Send a key command with specified repeats and interval.

        Args:
            key (rc): The key to send.
            repeat (int): Number of times to send the key.
            delay (int): Delay between key presses in seconds.

        Returns:
            bool: Result of the command verification.
        """
        result = False
        keyword = "term start init 1"

        # Send the key command
        for _ in range(repeat):
            self.session.write(f"{key}")
            time.sleep(delay)

        # Read output after sending keys
        output = self.session.read_until(self.prompt)

        # Check for the presence of a keyword in the output
        if keyword in output:
            result = True

        return result
