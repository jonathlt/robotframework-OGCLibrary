from owslib.wfs import WebFeatureService
from RequestsLibrary import RequestsLibrary


class OGCServiceLibrary(RequestsLibrary):

    def __init__(self):
        super(OGCServiceLibrary,self).__init__()
        self._result = 0
        self._url = ''
        self._service_type = ''
        self._ogc_version = '1.1.0'

    def connect_to_url(self,url):
        """ Check that we can connect to a given url

        :param url: string -- The url we wish to connect to
        :return: None, raises an assertion error if the return status code is not 200
        """
        RequestsLibrary.create_session(self,"URL",url)
        resp = RequestsLibrary.get(self,"URL","/")
        if str(resp.status_code) != "200":
            raise AssertionError("url: %s Status %s Can't connect" % (url,resp.status_code))

    def set_wfs_service(self,url):
        """ Set up parameters for a wfs service
        :param url: The url of the wfs service
        :return: None, sets up url and the service type

        """
        self._url = url
        self._service_type = 'wfs'

    def get_number_of_layers(self):
        """Get a count of the layers.

        :returns: int -- the number of layers to the _result variable

        """
        if self._service_type == 'wfs':
            wfs = WebFeatureService(self._url, version=self._ogc_version)
            self._result = len(wfs.contents)

    def check_for_layer(self,layer_name):
        """Checks for a layer of a given name.
        :param layer_name: layer to search for
        :returns: int -- the number of layers to the _result variable

        """
        if self._service_type == 'wfs':
            wfs = WebFeatureService(self._url, version=self._ogc_version)
            self._result = layer_name in wfs.contents.keys()

    def result_should_be(self,expected=0):
        """ Compares two values as strings
        :param expected: the expected result
        :return: None, Assertion error raise if expected not the same as result

        """
        if str(self._result) != str(expected):
            raise AssertionError("%s == %s" % (self._result, expected))

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

