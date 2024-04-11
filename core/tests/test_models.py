from django.test import TestCase
from core.models import CustomUser, Profile, Merchant, Product, Cart, CartItem, ProductReview, Payment, Checkout
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    '''Test models'''
    def setUp(self):
        """Set up test data"""
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        self.merchant = Merchant.objects.create(
            email='merchant@example.com',
            username='unique_username',
            password='testpass123456',
            merchant_name='Test Merchant',
            description='Test description for merchant',
        )
        self.product = Product.objects.create(
            product_name='Test Product',
            description='Test description for product',
            price=10.99,
            stock=100,
            merchant=self.merchant,
        )
        self.cart = Cart.objects.create(
            user=self.user
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )
        self.product_review = ProductReview.objects.create(
            user=self.user,
            product=self.product,
            rating=4,
            comment='Test review comment',
        )
        self.payment = Payment.objects.create(
            user=self.user,
            amount=20.00,
            payment_method='Test Payment Method',
        )
        self.checkout = Checkout.objects.create(
            user=self.user,
            cart=self.cart,
            payment=self.payment,
            status='Completed',
        )

    def test_user_creation(self):
        """Test user creation"""
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))
    
    def test_merchant_creation(self):
        """Test merchant creation"""
        self.assertEqual(self.merchant.email, 'merchant@example.com')
        # self.assertTrue(self.merchant.check_password('testpass123456'))
        self.assertEqual(self.merchant.merchant_name, 'Test Merchant')
        self.assertEqual(self.merchant.description, 'Test description for merchant')

    def test_product_creation(self):
        """Test product creation"""
        self.assertEqual(self.product.product_name, 'Test Product')
        self.assertEqual(self.product.description, 'Test description for product')
        self.assertEqual(self.product.price, 10.99)
        self.assertEqual(self.product.stock, 100)
        self.assertEqual(self.product.merchant, self.merchant)
    
    def test_profile_creation(self):
        """Test profile creation"""
        profile = Profile.objects.create(user=self.user, profile_image='DRF_atsuko_clone.png')
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.profile_image, 'DRF_atsuko_clone.png')


    def test_cart_creation(self):
        """Test cart creation"""
        self.assertEqual(self.cart.user, self.user)

    def test_cart_item_creation(self):
        """Test cart item creation"""
        self.assertEqual(self.cart_item.cart, self.cart)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 2)

    def test_product_review_creation(self):
        """Test product review creation"""
        self.assertEqual(self.product_review.user, self.user)
        self.assertEqual(self.product_review.product, self.product)
        self.assertEqual(self.product_review.rating, 4)
        self.assertEqual(self.product_review.comment, 'Test review comment')

    def test_payment_creation(self):
        """Test payment creation"""
        self.assertEqual(self.payment.user, self.user)
        self.assertEqual(self.payment.amount, 20.00)
        self.assertEqual(self.payment.payment_method, 'Test Payment Method')

    def test_checkout_creation(self):
        """Test checkout creation"""
        self.assertEqual(self.checkout.user, self.user)
        self.assertEqual(self.checkout.cart, self.cart)
        self.assertEqual(self.checkout.payment, self.payment)
        self.assertEqual(self.checkout.status, 'Completed')

