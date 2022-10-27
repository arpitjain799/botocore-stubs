from typing import Any, Mapping
from urllib.request import Request

from botocore import retryhandler as retryhandler
from botocore import translate as translate
from botocore import utils as utils
from botocore.compat import MD5_AVAILABLE as MD5_AVAILABLE
from botocore.compat import OrderedDict as OrderedDict
from botocore.compat import XMLParseError as XMLParseError
from botocore.compat import ensure_bytes as ensure_bytes
from botocore.compat import get_md5 as get_md5
from botocore.compat import unquote as unquote
from botocore.compat import unquote_str as unquote_str
from botocore.compat import urlsplit as urlsplit
from botocore.compat import urlunsplit as urlunsplit
from botocore.exceptions import AliasConflictParameterError as AliasConflictParameterError
from botocore.exceptions import MissingServiceIdError as MissingServiceIdError
from botocore.exceptions import ParamValidationError as ParamValidationError
from botocore.exceptions import UnsupportedTLSVersionWarning as UnsupportedTLSVersionWarning
from botocore.signers import add_generate_db_auth_token as add_generate_db_auth_token
from botocore.signers import add_generate_presigned_post as add_generate_presigned_post
from botocore.signers import add_generate_presigned_url as add_generate_presigned_url
from botocore.utils import SAFE_CHARS as SAFE_CHARS
from botocore.utils import conditionally_calculate_md5 as conditionally_calculate_md5
from botocore.utils import hyphenize_service_id as hyphenize_service_id
from botocore.utils import percent_encode as percent_encode
from botocore.utils import switch_host_with_param as switch_host_with_param

REGISTER_FIRST: Any
REGISTER_LAST: Any
VALID_BUCKET: Any
VALID_S3_ARN: Any
VERSION_ID_SUFFIX: Any
SERVICE_NAME_ALIASES: Any

def handle_service_name_alias(service_name: str, **kwargs: Any) -> Any: ...
def add_recursion_detection_header(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def escape_xml_payload(params: Mapping[str, Any], **kwargs: Any) -> Any: ...
def check_for_200_error(response: Any, **kwargs: Any) -> None: ...
def set_operation_specific_signer(context: Any, signing_name: str, **kwargs: Any) -> Any: ...
def decode_console_output(parsed: Mapping[str, Any], **kwargs: Any) -> None: ...
def generate_idempotent_uuid(params: Mapping[str, Any], model: Any, **kwargs: Any) -> None: ...
def decode_quoted_jsondoc(value: Any) -> Any: ...
def json_decode_template_body(parsed: Mapping[str, Any], **kwargs: Any) -> None: ...
def validate_bucket_name(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def sse_md5(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def copy_source_sse_md5(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def disable_signing(**kwargs: Any) -> Any: ...
def add_expect_header(model: Any, params: Mapping[str, Any], **kwargs: Any) -> None: ...

class DeprecatedServiceDocumenter:
    def __init__(self, replacement_service_name: str) -> None: ...
    def inject_deprecation_notice(self, section: Any, event_name: str, **kwargs: Any) -> None: ...

def document_copy_source_form(section: Any, event_name: str, **kwargs: Any) -> None: ...
def handle_copy_source_param(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def inject_presigned_url_ec2(
    params: Mapping[str, Any], request_signer: Any, model: Any, **kwargs: Any
) -> None: ...
def inject_presigned_url_rds(
    params: Mapping[str, Any], request_signer: Any, model: Any, **kwargs: Any
) -> None: ...
def json_decode_policies(parsed: Mapping[str, Any], model: Any, **kwargs: Any) -> None: ...
def parse_get_bucket_location(
    parsed: Mapping[str, Any], http_response: Any, **kwargs: Any
) -> None: ...
def base64_encode_user_data(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def document_base64_encoding(param: Mapping[str, Any]) -> Any: ...
def validate_ascii_metadata(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def fix_route53_ids(params: Mapping[str, Any], model: Any, **kwargs: Any) -> None: ...
def inject_account_id(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def add_glacier_version(model: Any, params: Mapping[str, Any], **kwargs: Any) -> None: ...
def add_accept_header(model: Any, params: Mapping[str, Any], **kwargs: Any) -> None: ...
def add_glacier_checksums(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def document_glacier_tree_hash_checksum() -> Any: ...
def document_cloudformation_get_template_return_type(
    section: Any, event_name: str, **kwargs: Any
) -> None: ...
def switch_host_machinelearning(request: Any, **kwargs: Any) -> None: ...
def check_openssl_supports_tls_version_1_2(**kwargs: Any) -> None: ...
def change_get_to_post(request: Request, **kwargs: Any) -> None: ...
def set_list_objects_encoding_type_url(
    params: Mapping[str, Any], context: Any, **kwargs: Any
) -> None: ...
def decode_list_object(parsed: Mapping[str, Any], context: Any, **kwargs: Any) -> None: ...
def decode_list_object_v2(parsed: Mapping[str, Any], context: Any, **kwargs: Any) -> None: ...
def decode_list_object_versions(parsed: Mapping[str, Any], context: Any, **kwargs: Any) -> None: ...
def convert_body_to_file_like_object(params: Mapping[str, Any], **kwargs: Any) -> None: ...

class ParameterAlias:
    def __init__(self, original_name: str, alias_name: str) -> None: ...
    def alias_parameter_in_call(
        self, params: Mapping[str, Any], model: Any, **kwargs: Any
    ) -> None: ...
    def alias_parameter_in_documentation(
        self, event_name: str, section: Any, **kwargs: Any
    ) -> None: ...

class ClientMethodAlias:
    def __init__(self, actual_name: str) -> None: ...
    def __call__(self, client: Any, **kwargs: Any) -> Any: ...

class HeaderToHostHoister:
    def __init__(self, header_name: str) -> None: ...
    def hoist(self, params: Mapping[str, Any], **kwargs: Any) -> None: ...

def inject_api_version_header_if_needed(
    model: Any, params: Mapping[str, Any], **kwargs: Any
) -> None: ...
def remove_lex_v2_start_conversation(
    class_attributes: Mapping[str, Any], **kwargs: Any
) -> None: ...
def add_retry_headers(request: Request, **kwargs: Any) -> None: ...
def remove_bucket_from_url_paths_from_model(
    params: Mapping[str, Any], model: Any, context: Any, **kwargs: Any
) -> None: ...
def remove_accid_host_prefix_from_model(
    params: Mapping[str, Any], model: Any, context: Any, **kwargs: Any
) -> None: ...
def remove_arn_from_signing_path(request: Request, **kwargs: Any) -> None: ...
def customize_endpoint_resolver_builtins(
    builtins: Mapping[str, Any], model: Any, params: Mapping[str, Any], context: Any, **kwargs: Any
) -> None: ...

BUILTIN_HANDLERS: Any
