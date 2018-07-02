from . import main
from ..build_spider import *


@main.route('/')
def index():
    crawl_all()
