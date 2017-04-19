from django.conf.urls import url, include

from ecommerce import views
from tests.ecommerce.views import (
    TestAddToCart, TestChangeCount, TestFlushCart, TestRemoveFromCart
)

from pages.models import Page

test_url = [
    url(r'^cart-add/$', TestAddToCart.as_view(), name='cart_add'),
    url(r'^cart-change/$', TestChangeCount.as_view(), name='cart_set_count'),
    url(r'^cart-flush/$', TestFlushCart.as_view(), name='cart_flush'),
    url(r'^cart-remove/$', TestRemoveFromCart.as_view(), name='cart_remove'),
]

urlpatterns = [
    url(r'^catalog/', include('catalog.urls')),
    url(r'^shop/', include(test_url)),
    url(r'^shop/(?P<page>order)/$', views.OrderPage.as_view(),
        name=Page.CUSTOM_PAGES_URL_NAME),
]