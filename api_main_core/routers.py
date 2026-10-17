from rest_framework import routers
from api_main_core.viewsets.userprofile_viewset import UserProfileViewSet
from api_main_core.viewsets.escritor_viewset import EscritorViewSet
from api_main_core.viewsets.productora_viewset import ProductoraViewSet
from api_main_core.viewsets.contenido_viewset import ContenidoViewSet
from api_main_core.viewsets.review_viewset import ReviewViewSet
from api_main_core.viewsets.comentario_viewset import ComentarioViewSet
from api_main_core.viewsets.favoritos_viewset import FavoritoViewSet
from api_main_core.viewsets.bloqueo_viewset import BloqueoViewSet
from api_main_core.viewsets.seguir_viewset import SeguirViewSet
from api_main_core.viewsets.user_viewset import UserViewSet

router_review = routers.DefaultRouter()

router_review.register(r"userprofile",UserProfileViewSet, basename="userprofile")
router_review.register(r"escritor",EscritorViewSet, basename="escritor")
router_review.register(r"productora",ProductoraViewSet, basename="productora")
router_review.register(r"contenido",ContenidoViewSet, basename="contenido")
router_review.register(r"review",ReviewViewSet, basename="review")
router_review.register(r"comentario",ComentarioViewSet, basename="comentario")
router_review.register(r"favoritos",FavoritoViewSet, basename="favoritos")
router_review.register(r"bloqueos",BloqueoViewSet, basename="bloqueos")
router_review.register(r"seguidores",SeguirViewSet, basename="seguidores")
router_review.register(r"usuarios",UserViewSet, basename="user")