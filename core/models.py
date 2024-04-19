from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
import uuid
import os
from django.conf import settings


def profile_image_file(instance, filename):
    """Generate filename for new object image"""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('uploads', 'profile', filename)


def product_image_file(instance, filename):
    """Generate filename for new object image"""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('uploads', 'product', filename)


PRODUCT_CATEGORIES = [
    ('electronics', 'Electronics'),
    ('clothing_apparel', 'Clothing & Apparel'),
    ('home_kitchen', 'Home & Kitchen'),
    ('health_personal_care', 'Health & Personal Care'),
    ('beauty_cosmetics', 'Beauty & Cosmetics'),
    ('books_literature', 'Books & Literature'),
    ('toys_games', 'Toys & Games'),
    ('sports_outdoors', 'Sports & Outdoors'),
    ('automotive_motorcycles', 'Automotive & Motorcycles'),
    ('furniture_decor', 'Furniture & Decor'),
    ('jewelry_watches', 'Jewelry & Watches'),
    ('baby_toddler', 'Baby & Toddler'),
    ('pet_supplies', 'Pet Supplies'),
    ('food_grocery', 'Food & Grocery'),
    ('tools_home_improvement', 'Tools & Home Improvement'),
    ('office_supplies', 'Office Supplies'),
    ('arts_crafts', 'Arts & Crafts'),
    ('musical_instruments', 'Musical Instruments'),
    ('garden_outdoor', 'Garden & Outdoor'),
    ('luggage_travel', 'Luggage & Travel'),
    ('fitness_exercise', 'Fitness & Exercise'),
    ('party_supplies', 'Party Supplies'),
    ('electronics_accessories', 'Electronics Accessories'),
    ('stationery_writing_supplies', 'Stationery & Writing Supplies'),
    ('appliances', 'Appliances'),
    ('video_games_consoles', 'Video Games & Consoles'),
    ('cameras_photography', 'Cameras & Photography'),
    ('computer_accessories', 'Computer Accessories'),
    ('cell_phones_accessories', 'Cell Phones & Accessories'),
    ('audio_headphones', 'Audio & Headphones'),
    ('software', 'Software'),
    ('movies_tv_shows', 'Movies & TV Shows'),
    ('collectibles_memorabilia', 'Collectibles & Memorabilia'),
    ('shoes_footwear', 'Shoes & Footwear'),
    ('bags_backpacks', 'Bags & Backpacks'),
    ('watches_wearable_technology', 'Watches & Wearable Technology'),
    ('sunglasses_eyewear', 'Sunglasses & Eyewear'),
    ('hats_caps', 'Hats & Caps'),
    ('scarves_wraps', 'Scarves & Wraps'),
    ('gloves_mittens', 'Gloves & Mittens'),
    ('socks_hosiery', 'Socks & Hosiery'),
    ('belts_buckles', 'Belts & Buckles'),
    ('wallets_cardholders', 'Wallets & Cardholders'),
    ('perfumes_fragrances', 'Perfumes & Fragrances'),
    ('skincare_bath', 'Skincare & Bath'),
    ('haircare_styling', 'Haircare & Styling'),
    ('makeup_cosmetics', 'Makeup & Cosmetics'),
    ('nail_care_polish', 'Nail Care & Polish'),
    ('dental_care', 'Dental Care'),
    ('shaving_grooming', 'Shaving & Grooming'),
    ('vitamins_supplements', 'Vitamins & Supplements'),
    ('first_aid_medical_supplies', 'First Aid & Medical Supplies'),
    ('allergy_sinus', 'Allergy & Sinus'),
    ('pain_relief_management', 'Pain Relief & Management'),
    ('sexual_wellness', 'Sexual Wellness'),
    ('books', 'Books'),
    ('magazines', 'Magazines'),
    ('audiobooks', 'Audiobooks'),
    ('ebooks', 'E-books'),
    ('educational_toys_games', 'Educational Toys & Games'),
    ('building_toys', 'Building Toys'),
    ('dolls_accessories', 'Dolls & Accessories'),
    ('action_figures', 'Action Figures'),
    ('board_games', 'Board Games'),
    ('card_games', 'Card Games'),
    ('puzzles', 'Puzzles'),
    ('outdoor_play_equipment', 'Outdoor Play Equipment'),
    ('camping_hiking_gear', 'Camping & Hiking Gear'),
    ('cycling_accessories', 'Cycling Accessories'),
    ('fishing_gear', 'Fishing Gear'),
    ('hunting_equipment', 'Hunting Equipment'),
    ('exercise_fitness_equipment', 'Exercise & Fitness Equipment'),
    ('gymnastics_yoga_equipment', 'Gymnastics & Yoga Equipment'),
    ('team_sports_equipment', 'Team Sports Equipment'),
    ('athletic_apparel', 'Athletic Apparel'),
    ('sports_shoes', 'Sports Shoes'),
    ('camping_furniture', 'Camping Furniture'),
    ('outdoor_cooking_equipment', 'Outdoor Cooking Equipment'),
    ('gardening_tools', 'Gardening Tools'),
    ('patio_furniture', 'Patio Furniture'),
    ('pool_spa_supplies', 'Pool & Spa Supplies'),
    ('party_decorations', 'Party Decorations'),
    ('party_favors', 'Party Favors'),
    ('party_games', 'Party Games'),
    ('baking_supplies', 'Baking Supplies'),
    ('cooking_utensils', 'Cooking Utensils'),
    ('small_appliances', 'Small Appliances'),
    ('cookware_bakeware', 'Cookware & Bakeware'),
    ('kitchen_storage_organization', 'Kitchen Storage & Organization'),
    ('tableware_serveware', 'Tableware & Serveware'),
    ('bedding_linens', 'Bedding & Linens'),
    ('bathroom_accessories', 'Bathroom Accessories'),
    ('home_decor_accents', 'Home Decor Accents'),
    ('lighting_fixtures', 'Lighting Fixtures'),
    ('wall_art_mirrors', 'Wall Art & Mirrors'),
    ('rugs_carpets', 'Rugs & Carpets'),
    ('curtains_window_treatments', 'Curtains & Window Treatments'),
    ('furniture_hardware', 'Furniture Hardware'),
    ('indoor_plants_planters', 'Indoor Plants & Planters'),
    ('fireplaces_accessories', 'Fireplaces & Accessories')
]


# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    username = models.CharField(_('username'), unique=True, max_length=50, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)
    REGISTERATION_CHOICE = [
        ('email', 'Email'),
        ('google', 'Google')
    ]
    registration_method = models.CharField(
        max_length=10,
        choices=REGISTERATION_CHOICE,
        default='email'
    )
    is_admin = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.username


class MerchantProfile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=profile_image_file, null=True, blank=True)
    merchant_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile for {self.user.username}'


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    product_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORIES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    product_image = models.ImageField(upload_to=product_image_file, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0, null=False, blank=False)
    merchant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product name -> {self.product_name}'

    def generate_sharable_link(self):
        return f'/products/{self.id}/'


class Wishlist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wishlist for {self.user.username}"


class Cart(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart of {self.user.username}'


class CartItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductReview(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Checkout(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    STATUS = [
        ('pending', 'pending'),
        ('successful', 'successful'),
        ('failed', 'failed')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for user -> {self.recipient.username}'
