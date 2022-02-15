# [Backward compatibility]: keep importing modules functions
from .internal.utils.deprecation import deprecated
from .internal.utils.formats import asbool
from .internal.utils.formats import deep_getattr
from .internal.utils.formats import get_env
from .internal.utils.wrappers import safe_patch
from .internal.utils.wrappers import unwrap
from .vendor.debtcollector.removals import removed_module


removed_module(
    module="ddtrace.util",
    replacement="ddtrace.utils",
    removal_version="1.0.0",
)

__all__ = [
    "deprecated",
    "asbool",
    "deep_getattr",
    "get_env",
    "safe_patch",
    "unwrap",
]
