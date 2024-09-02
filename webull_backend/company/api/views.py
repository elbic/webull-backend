"""
Company views for the Webull backend.
"""

from django.utils.decorators import method_decorator  # pylint: disable=E0402
from django.views.decorators.cache import cache_page  # pylint: disable=E0402
from rest_framework import generics
from rest_framework.response import Response  # pylint: disable=E0401

from webull_backend.company.models import Company  # pylint: disable=E0402
from webull_backend.company.utils import delete_cache  # pylint: disable=E0402

from .serializers import CompanyDetailSerializer  # pylint: disable=E0402
from .serializers import CompanySerializer  # pylint: disable=E0402


class CompanyListCreateView(generics.ListCreateAPIView):
    """
    View to handle listing and creating companies.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to handle retrieving, updating, and deleting a company by UUID.
    Uses cache for 5 minutes (300 seconds).
    """

    CACHE_KEY_PREFIX = "company-view"
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    detail_serializer = CompanyDetailSerializer

    lookup_url_kwarg = "uuid"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def retrieve(self, request, pk):
        """
        Retrieves a company by UUID.

        Args:
            pk (str): The UUID of the company to retrieve.
        Returns:
            Response: A JSON response with the company data.
        """
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = Company.objects.get(uuid=pk)

        serializer = CompanyDetailSerializer(queryset, many=False)
        return Response(serializer.data)

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        """
        Lists all companies.
        Returns:
            Response: A JSON response with the company data.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates a new company.

        Args:
            request (Request): The HTTP request containing the company data.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        Returns:
            Response: A JSON response with the created company data.
        """
        response = super().create(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response


class AllCompaniesListView(generics.ListAPIView):
    """
    View to handle listing all companies.
    Uses cache for 5 minutes (300 seconds).
    """

    CACHE_KEY_PREFIX = "company-view"
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        """
        Lists all companies.
        Returns:
            Response: A JSON response with the company data.
        """
        return super().list(request, *args, **kwargs)


class CompanyUpdateView(generics.RetrieveUpdateAPIView):
    """
    View to handle updating a company by UUID.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    partial = True


class CompanyDeleteView(generics.DestroyAPIView):
    """
    View to handle deleting a company by UUID.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def destroy(self, request, *args, **kwargs):
        """
        Deletes a company.

        Args:
            request (Request): The HTTP request containing the delete data.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        Returns:
            Response: A JSON response indicating success or failure.
        """
        instance = self.get_object()
        instance.delete()
        delete_cache(self.CACHE_KEY_PREFIX)

        return Response(print("delete Company"))
