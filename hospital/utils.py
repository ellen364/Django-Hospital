from django.db.models.query import QuerySet
from django.test import TestCase


class CustomTestCase(TestCase):
    def assertQuerysetEqual(self, qs, values, transform=repr, **kwargs):
        """A helper method that overrides some of the default behaviour of
        assertQuerysetEqual.
        """
        if qs == "Replace with your query":
            self.fail("Still to do")
        if not isinstance(qs, QuerySet):
            raise TypeError("Argument must be a QuerySet")
        if not isinstance(values, QuerySet):
            raise TypeError(
                "Argument must be a QuerySet. Have you changed the second "
                + "argument passed to assertQuerysetEqual?"
            )

        values = map(transform, values)
        super().assertQuerysetEqual(qs, values, transform, **kwargs)
