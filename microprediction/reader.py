from microprediction.conventions import MicroConventions
import requests

class MicroReader(MicroConventions):

    def __init__(self,base_url="http://www.microprediction.com"):
        """ Establish connection and adopt configuration parameters from site """
        super().__init__(base_url=base_url)

    def get(self, name):
        res = requests.get(self.base_url + '/live/' + name)
        if res.status_code == 200:
           return res.json()

    def get_current_value(self, name):
        res = requests.get(self.base_url + '/live/' + name)
        if res.status_code == 200:
           return float(res.json())

    def get_streams(self):
        res = requests.get(self.base_url + '/streams')
        if res.status_code == 200:
            return res.json()

    def get_summary(self, name):
        res = requests.get(self.base_url + '/live/summary::' + name)
        if res.status_code == 200:
            return res.json()

    def get_lagged_values(self, name):
        """ Retrieve lagged values of a time series
        :param name:    cop.json   z1~cop.json   z2~cop~qp.json
        :return: [ float ]
        """
        res = requests.get(self.base_url+'/live/lagged_values::'+name )
        if res.status_code==200:
            return res.json()

    def get_lagged_times(self, name):
        """ Retrieve lagged times
        :param name:    cop.json   z1~cop.json   z2~cop~qp.json
        :return: [ float ]
        """
        res = requests.get(self.base_url+'/live/lagged_times::'+name )
        if res.status_code==200:
            return res.json()

    def get_delayed_value(self, name, delay=None):
        """ Retrieve quarantined value
        :param name:    cop.json   z1~cop.json   z2~cop~qp.json
        :return: [ float ]
        """
        delay = delay or self.delays[0]
        res = requests.get(self.base_url + '/live/delayed::'+str(delay)+ "::" + name)
        if res.status_code == 200:
            return res.json()

    def get_cdf(self, name, values=None):
        if values is None:  # Supply x-values at which approximate crowd cdf will be computed. # FIXME... should not be here an also in conventions
            values = [-2.3263478740408408, -1.6368267885518997, -1.330561513178897, -1.1146510149326596,
                      -0.941074530352976, -0.792046894425591, -0.6588376927361878, -0.5364223812298266,
                      -0.4215776353171568, -0.3120533220328322, -0.20615905948527324, -0.10253336200497987, 0.0,
                      0.10253336200497973, 0.20615905948527324, 0.31205332203283237, 0.4215776353171568,
                      0.5364223812298264, 0.6588376927361878, 0.7920468944255913, 0.941074530352976, 1.1146510149326592,
                      1.330561513178897, 1.6368267885519001, 2.3263478740408408]
        comma_sep_values = ",".join([str(v) for v in values])
        res = requests.get(self.base_url + 'cdf/' + name, params={"values", comma_sep_values})
        if res.status_code == 200:
            return res.json()