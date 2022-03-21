from sentaku import ImplementationContext as _SentakuImplementationContext
from sentaku import ContextualMethod, ContextualProperty, Element, Collection, ImplementationName

__all__ = ["ContextualMethod", "ContextualProperty", "Element", "Collection", "ImplementationName"]


# subclass to have a custom dectate registration point
class ImplementationContext(_SentakuImplementationContext):
    pass
