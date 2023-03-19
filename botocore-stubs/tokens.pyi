import datetime
import logging
from collections.abc import Callable, Iterable
from typing import Any, NamedTuple, Optional, Type

from botocore.credentials import JSONFileCache
from botocore.session import Session

logger: logging.Logger

def create_token_resolver(session: Session) -> TokenProviderChain: ...

class FrozenAuthToken(NamedTuple):
    token: str
    expiration: Optional[datetime.datetime] = ...

class DeferredRefreshableToken:
    def __init__(
        self,
        method: Any,
        refresh_using: Callable[[], FrozenAuthToken],
        time_fetcher: Callable[[], datetime.datetime] = ...,
    ) -> None: ...
    def get_frozen_token(self) -> FrozenAuthToken: ...

class TokenProviderChain:
    def __init__(self, providers: Optional[Iterable[Any]] = ...) -> None: ...
    def load_token(self) -> DeferredRefreshableToken: ...

class SSOTokenProvider:
    METHOD: str = ...
    DEFAULT_CACHE_CLS: Type[JSONFileCache] = ...

    def __init__(
        self,
        session: Session,
        cache: Optional[JSONFileCache] = ...,
        time_fetcher: Callable[[], datetime.datetime] = ...,
        profile_name: Optional[str] = ...,
    ) -> None: ...
    def load_token(self) -> DeferredRefreshableToken: ...
