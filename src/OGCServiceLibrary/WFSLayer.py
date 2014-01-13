#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from owslib.wfs import WebFeatureService

__version__ = '0.1'

class WFSLayer():

    def __init__(self):
        self._result = 0
        self._url = ''
        self._ogc_version = '1.1.0'

    def get_number_of_wfs_layers(self):
        """
        Get a count of the WFS layers.
        Fail if the layers returned is not equal to the  expected, example:
        | Get number of layers | expected_number_of_layers |

        """
        wfs = WebFeatureService(self._url, version=self._ogc_version)
        self._result = len(wfs.contents)

    def check_for_wfs_layer(self,layer_name):
        """
        Checks for a WFS layer of a given name.
        Fail if the layer name is not found
        | Check for layer | my_layer_name |

        """
        wfs = WebFeatureService(self._url, version=self._ogc_version)
        self._result = layer_name in wfs.contents.keys()