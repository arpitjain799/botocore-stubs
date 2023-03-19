from collections.abc import Callable, Iterable, Mapping
from logging import Logger
from typing import Any, Dict, List, Optional, Type

from botocore.config import Config
from botocore.exceptions import BotoCoreError
from botocore.exceptions import ChecksumError as ChecksumError
from botocore.exceptions import ConnectionClosedError as ConnectionClosedError
from botocore.exceptions import ConnectionError as ConnectionError
from botocore.exceptions import EndpointConnectionError as EndpointConnectionError
from botocore.exceptions import ReadTimeoutError as ReadTimeoutError

logger: Logger = ...

EXCEPTION_MAP: Dict[str, List[Type[BotoCoreError]]]

def delay_exponential(base: float, growth_factor: float, attempts: int) -> float: ...
def create_exponential_delay_function(
    base: float, growth_factor: float
) -> Callable[[int], float]: ...
def create_retry_handler(config: Config, operation_name: Optional[str] = ...) -> RetryHandler: ...
def create_retry_action_from_config(
    config: Config, operation_name: Optional[str] = ...
) -> Callable[[int], float]: ...
def create_checker_from_retry_config(
    config: Config, operation_name: Optional[str] = ...
) -> MaxAttemptsDecorator: ...

class RetryHandler:
    def __init__(self, checker: BaseChecker, action: Callable[[int], float]) -> None: ...
    def __call__(
        self, attempts: int, response: Mapping[str, Any], caught_exception: Exception, **kwargs: Any
    ) -> Any: ...

class BaseChecker:
    def __call__(
        self, attempt_number: int, response: Mapping[str, Any], caught_exception: Exception
    ) -> bool: ...

class MaxAttemptsDecorator(BaseChecker):
    def __init__(
        self,
        checker: BaseChecker,
        max_attempts: int,
        retryable_exceptions: Optional[Iterable[Type[Exception]]] = ...,
    ) -> None: ...
    # FIXME: Signature of "__call__" incompatible with supertype "BaseChecker"
    def __call__(  # type: ignore [override]
        self,
        attempt_number: int,
        response: Mapping[str, Any],
        caught_exception: Exception,
        retries_context: Any,
    ) -> bool: ...

class HTTPStatusCodeChecker(BaseChecker):
    def __init__(self, status_code: int) -> None: ...

class ServiceErrorCodeChecker(BaseChecker):
    def __init__(self, status_code: int, error_code: str) -> None: ...

class MultiChecker(BaseChecker):
    def __init__(self, checkers: Iterable[BaseChecker]) -> None: ...

class CRC32Checker(BaseChecker):
    def __init__(self, header: str) -> None: ...

class ExceptionRaiser(BaseChecker): ...
