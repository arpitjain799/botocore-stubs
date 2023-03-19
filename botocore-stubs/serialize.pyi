from collections.abc import Mapping
from typing import Any, Dict, Type

from botocore import validate as validate
from botocore.compat import formatdate as formatdate
from botocore.model import OperationModel
from botocore.utils import is_json_value_header as is_json_value_header
from botocore.utils import parse_to_aware_datetime as parse_to_aware_datetime
from botocore.utils import percent_encode as percent_encode

DEFAULT_TIMESTAMP_FORMAT: str
ISO8601: str
ISO8601_MICRO: str

def create_serializer(protocol_name: str, include_validation: bool = ...) -> Any: ...

class Serializer:
    DEFAULT_METHOD: str = ...
    MAP_TYPE: Type[Dict[str, Any]] = ...
    DEFAULT_ENCODING: str = ...
    def serialize_to_request(
        self, parameters: Mapping[str, Any], operation_model: OperationModel
    ) -> Dict[str, Any]: ...

class QuerySerializer(Serializer):
    TIMESTAMP_FORMAT: str = ...
    def serialize_to_request(
        self, parameters: Mapping[str, Any], operation_model: OperationModel
    ) -> Dict[str, Any]: ...

class EC2Serializer(QuerySerializer): ...

class JSONSerializer(Serializer):
    TIMESTAMP_FORMAT: str = ...
    def serialize_to_request(
        self, parameters: Mapping[str, Any], operation_model: OperationModel
    ) -> Dict[str, Any]: ...

class BaseRestSerializer(Serializer):
    QUERY_STRING_TIMESTAMP_FORMAT: str = ...
    HEADER_TIMESTAMP_FORMAT: str = ...
    KNOWN_LOCATIONS: Any = ...
    def serialize_to_request(
        self, parameters: Mapping[str, Any], operation_model: OperationModel
    ) -> Dict[str, Any]: ...

class RestJSONSerializer(BaseRestSerializer, JSONSerializer): ...

class RestXMLSerializer(BaseRestSerializer):
    TIMESTAMP_FORMAT: str = ...

SERIALIZERS: Dict[str, Serializer]
