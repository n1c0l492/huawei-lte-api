from huawei_lte_api.ApiGroup import ApiGroup, GetResponseType


class Ntwk(ApiGroup):

    def lan_upnp_portmapping(self) -> GetResponseType:
        return self._connection.get('ntwk/lan_upnp_portmapping')

    def celllock(self) -> GetResponseType:
        return self._connection.get('ntwk/celllock')
