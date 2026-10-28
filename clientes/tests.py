from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from clientes.models import Cliente
from productos.models import Categoria, Producto
from proveedores.models import Proveedor
from ventas.models import DetalleVenta, Venta


class ModulePagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(
            nombre='Cliente de prueba',
            correo='cliente@example.test',
        )
        cls.proveedor = Proveedor.objects.create(
            nombre='Proveedor de prueba',
            correo='proveedor@example.test',
        )
        cls.categoria = Categoria.objects.create(nombre='Categoría de prueba')
        cls.producto = Producto.objects.create(
            nombre='Producto de prueba',
            precio='10.00',
            stock=5,
            categoria=cls.categoria,
            proveedor=cls.proveedor,
        )
        cls.venta = Venta.objects.create(cliente=cls.cliente)
        DetalleVenta.objects.create(
            venta=cls.venta,
            producto=cls.producto,
            cantidad=2,
            precio_unitario='10.00',
        )
        cls.admin = get_user_model().objects.create_superuser(
            username='erp-test-admin',
            email='admin@example.test',
            password='test-password',
        )

    def test_public_module_pages_render(self):
        paths = [
            reverse('inicio'),
            reverse('login'),
            reverse('clientes:inicio'),
            reverse('clientes:lista'),
            reverse('productos:lista'),
            reverse('productos:detalle', kwargs={'pk': self.producto.pk}),
            reverse('proveedores:lista'),
            reverse('proveedores:detalle', kwargs={'proveedor_id': self.proveedor.pk}),
            reverse('ventas:lista'),
            reverse('ventas:detalle', kwargs={'venta_id': self.venta.pk}),
            reverse('reportes:inicio'),
        ]

        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_authenticated_forms_render(self):
        self.client.force_login(self.admin)
        paths = [
            reverse('productos:crear'),
            reverse('productos:editar', kwargs={'producto_id': self.producto.pk}),
            reverse('productos:eliminar', kwargs={'producto_id': self.producto.pk}),
            reverse('proveedores:crear'),
            reverse('proveedores:editar', kwargs={'proveedor_id': self.proveedor.pk}),
            reverse('proveedores:eliminar', kwargs={'proveedor_id': self.proveedor.pk}),
            reverse('ventas:crear'),
            reverse('ventas:eliminar', kwargs={'venta_id': self.venta.pk}),
        ]

        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)
