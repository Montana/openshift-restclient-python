# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0-alpha3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1LimitRangeItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, default=None, default_request=None, max=None, max_limit_request_ratio=None, min=None, type=None):
        """
        V1LimitRangeItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default': 'dict(str, ResourceQuantity)',
            'default_request': 'dict(str, ResourceQuantity)',
            'max': 'dict(str, ResourceQuantity)',
            'max_limit_request_ratio': 'dict(str, ResourceQuantity)',
            'min': 'dict(str, ResourceQuantity)',
            'type': 'str'
        }

        self.attribute_map = {
            'default': 'default',
            'default_request': 'defaultRequest',
            'max': 'max',
            'max_limit_request_ratio': 'maxLimitRequestRatio',
            'min': 'min',
            'type': 'type'
        }

        self._default = default
        self._default_request = default_request
        self._max = max
        self._max_limit_request_ratio = max_limit_request_ratio
        self._min = min
        self._type = type

    @property
    def default(self):
        """
        Gets the default of this V1LimitRangeItem.
        Default resource requirement limit value by resource name if resource limit is omitted.

        :return: The default of this V1LimitRangeItem.
        :rtype: dict(str, ResourceQuantity)
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this V1LimitRangeItem.
        Default resource requirement limit value by resource name if resource limit is omitted.

        :param default: The default of this V1LimitRangeItem.
        :type: dict(str, ResourceQuantity)
        """

        self._default = default

    @property
    def default_request(self):
        """
        Gets the default_request of this V1LimitRangeItem.
        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.

        :return: The default_request of this V1LimitRangeItem.
        :rtype: dict(str, ResourceQuantity)
        """
        return self._default_request

    @default_request.setter
    def default_request(self, default_request):
        """
        Sets the default_request of this V1LimitRangeItem.
        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.

        :param default_request: The default_request of this V1LimitRangeItem.
        :type: dict(str, ResourceQuantity)
        """

        self._default_request = default_request

    @property
    def max(self):
        """
        Gets the max of this V1LimitRangeItem.
        Max usage constraints on this kind by resource name.

        :return: The max of this V1LimitRangeItem.
        :rtype: dict(str, ResourceQuantity)
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this V1LimitRangeItem.
        Max usage constraints on this kind by resource name.

        :param max: The max of this V1LimitRangeItem.
        :type: dict(str, ResourceQuantity)
        """

        self._max = max

    @property
    def max_limit_request_ratio(self):
        """
        Gets the max_limit_request_ratio of this V1LimitRangeItem.
        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.

        :return: The max_limit_request_ratio of this V1LimitRangeItem.
        :rtype: dict(str, ResourceQuantity)
        """
        return self._max_limit_request_ratio

    @max_limit_request_ratio.setter
    def max_limit_request_ratio(self, max_limit_request_ratio):
        """
        Sets the max_limit_request_ratio of this V1LimitRangeItem.
        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.

        :param max_limit_request_ratio: The max_limit_request_ratio of this V1LimitRangeItem.
        :type: dict(str, ResourceQuantity)
        """

        self._max_limit_request_ratio = max_limit_request_ratio

    @property
    def min(self):
        """
        Gets the min of this V1LimitRangeItem.
        Min usage constraints on this kind by resource name.

        :return: The min of this V1LimitRangeItem.
        :rtype: dict(str, ResourceQuantity)
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this V1LimitRangeItem.
        Min usage constraints on this kind by resource name.

        :param min: The min of this V1LimitRangeItem.
        :type: dict(str, ResourceQuantity)
        """

        self._min = min

    @property
    def type(self):
        """
        Gets the type of this V1LimitRangeItem.
        Type of resource that this limit applies to.

        :return: The type of this V1LimitRangeItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1LimitRangeItem.
        Type of resource that this limit applies to.

        :param type: The type of this V1LimitRangeItem.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1LimitRangeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other