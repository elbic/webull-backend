"""
Module for defining URL patterns for company-related views.

This module imports view classes from .views and defines URL patterns using Django's
path function.
"""

from django.urls import path

from .views import AllCompaniesListView
from .views import CompanyDeleteView
from .views import CompanyDetailView
from .views import CompanyListCreateView
from .views import CompanyUpdateView

urlpatterns = [
    # List/ Create company endpoint
    # GET: Retrieve a list of all companies or create a new company.
    # POST: Create a new company.
    path(
        "companies/",
        CompanyListCreateView.as_view(),
        name="company-list-create",
    ),
    # Detail view endpoint
    # GET: Retrieve the details of a specific company by its primary key (uuid).
    path(
        "companies/<uuid:pk>/",
        CompanyDetailView.as_view(),
        name="company-detail",
    ),
    # All companies list view endpoint
    # GET: Retrieve a list of all companies.
    path(
        "companies/all/",
        AllCompaniesListView.as_view(),
        name="all-companies-list",
    ),
    # Delete company endpoint
    # DELETE: Delete a specific company by its primary key (uuid).
    path(
        "companies/delete/<uuid:pk>/",
        CompanyDeleteView.as_view(),
        name="company-delete",
    ),
    # Update company endpoint
    # PUT: Update the details of a specific company by its primary key (uuid).
    path(
        "companies/update/<uuid:pk>/",
        CompanyUpdateView.as_view(),
        name="company-update",
    ),
]
