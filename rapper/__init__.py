# -*- coding: utf-8 -*-
from __future__ import absolute_import

version_info = (0, 1, 0)
__version__ = ".".join(map(str, version_info))

try:  # pragma: no cover
    from .persistence import Persistence
    from .mongo import MongoPersistence
    from .memory import MemoryPersistence
    from .hstore import HstorePersistence
    from .embedded import EmbeddedPersistence
    __all__ = ["Persistence", "MongoPersistence", "MemoryPersistence",
               "HstorePersistence", "EmbeddedPersistence"]
except ImportError:  # pragma: no cover
    import traceback
    traceback.print_exc()
