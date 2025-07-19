# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Swathy K S (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Theme Trading',
    'version': '17.0.1.0.0',
    'category': 'Theme/Corporate',
    'summary': 'Theme Trading is an attractive trading Website theme with '
               'customizable shop and homepage layouts. The theme comes with '
               'many useful and stylish snippets for trading websites.',
    'description': '''
        Theme Trading for Odoo Trading Website
        
        Features:
        • Custom homepage with trading-focused sections
        • Enhanced shop page with advanced product cards
        • Trading-specific snippets and components
        • Mobile-responsive design
        • Professional trading aesthetics
        • Image gallery support for products
        • Advanced product filtering
        • Trading dashboard elements
    ''',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': [
        'website',
        'website_sale',  # Added for shop functionality
        'website_blog',  # Optional: for trading blog/news
    ],
    'data': [
        # Core theme templates
        'views/theme_trading_templates.xml',
        'views/theme_trading_investing_templates.xml',
        
        # Layout templates
        'views/header_templates.xml',
        'views/footer_templates.xml',
        'views/website_views.xml',
        'views/contactus_templates.xml',
        
        # Custom shop and homepage templates
        'views/shop_templates.xml',          # New: Custom shop page
        'views/homepage_templates.xml',      # New: Custom homepage
        'views/product_templates.xml',       # New: Product customizations
        
        # Snippet templates
        'views/snippets/snippet_templates.xml',
        'views/snippets/theme_trading_banner_templates.xml',
        'views/snippets/theme_trading_feature_templates.xml',
        'views/snippets/theme_trading_community_templates.xml',
        'views/snippets/theme_trading_asset_classes_templates.xml',
        'views/snippets/theme_trading_aboutus_templates.xml',
        'views/snippets/theme_trading_faq_templates.xml',
        'views/snippets/theme_trading_testimonial_templates.xml',
        
        # New: Trading-specific snippets
        'views/snippets/theme_trading_hero_templates.xml',
        'views/snippets/theme_trading_stats_templates.xml',
        'views/snippets/theme_trading_pricing_templates.xml',
        'views/snippets/theme_trading_gallery_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # Main CSS
            "theme_trading/static/src/css/style.css",
            
            # New: Custom SCSS for enhanced styling
            "theme_trading/static/src/scss/trading_variables.scss",
            "theme_trading/static/src/scss/trading_components.scss",
            "theme_trading/static/src/scss/trading_shop.scss",
            "theme_trading/static/src/scss/trading_homepage.scss",
            "theme_trading/static/src/scss/trading_responsive.scss",
            
            # JavaScript for interactive elements
            "theme_trading/static/src/js/trading_main.js",
            "theme_trading/static/src/js/product_gallery.js",
            "theme_trading/static/src/js/trading_animations.js",
        ],
        'web.assets_backend': [
            # Backend customizations if needed
            "theme_trading/static/src/css/backend.css",
        ],
    },
    'images': [
        'static/description/banner.jpg',
        'static/description/theme_screenshot.jpg',
        
        # New: Additional preview images
        'static/description/homepage_preview.jpg',
        'static/description/shop_preview.jpg',
        'static/description/mobile_preview.jpg',
    ],
    
    # New: Demo data for better theme preview
    'demo': [
        'demo/trading_products_demo.xml',
        'demo/trading_pages_demo.xml',
        'demo/trading_menu_demo.xml',
    ],
    
    # Theme configuration
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    
    # SEO and performance
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    
    # Module metadata
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 1,
    
    # Price and currency (if selling theme)
    'price': 0.00,
    'currency': 'EUR',
    
    # Support and documentation
    'support': 'odoo@cybrosys.com',
    'live_test_url': 'https://www.cybrosys.com/apps/17.0/theme_trading',
    
    # Theme-specific settings
    'theme_color': '#1e3a8a',
    'theme_preview_image': 'static/description/theme_screenshot.jpg',
    
    # Compatibility
    'odoo_version': '17.0',
    'python_requires': '>=3.8',
    
    # Additional metadata
    'contributors': [
        'Swathy K S <odoo@cybrosys.com>',
    ],
    'tags': [
        'theme',
        'trading',
        'finance',
        'ecommerce',
        'corporate',
        'business',
        'responsive',
        'modern',
    ],
}