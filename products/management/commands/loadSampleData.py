import re
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Load some sample data into the db"
    
    def add_arguments(self, parser):
        parser.add_argument('--file', dest='file', help='File to load')

    def handle(self, **options):
        from products.models import Product
        
        if options['file']:
            print("Importing " + options['file'])
            
            with open(options['file']) as f:
                linecount = 0
                next(f)
                for line in f:
                    linecount += 1
                    fields = line.split(',')
                    
                    data = {
                        'product_name': fields[1],
                        'search_price': fields[3],
                        'aw_image_url': fields[5],
                        'aw_deep_link': fields[0],
                        'merchant_category': fields[2],
                        'category_name': fields[4],
                    }

                    product = Product(**data)
                    product.save()
                
                print("Added {0} products".format(linecount))