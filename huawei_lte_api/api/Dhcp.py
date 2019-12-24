from huawei_lte_api.ApiGroup import ApiGroup, GetResponseType


class Dhcp(ApiGroup):
    def settings(self) -> GetResponseType:
        return self._connection.get('dhcp/settings')

    def feature_switch(self) -> GetResponseType:
        return self._connection.get('dhcp/feature-switch')
