from flask import render_template, Blueprint
from app.models import Tour, Review
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Hello World"

@bp.route('/main')
def main():
    return render_template('main.html')

@bp.route('/tours')
def tours():
    tours = Tour.query.all()
    return render_template('tours.html', tours=tours)

@bp.route('/tour/<int:id>')
def tour_detail(id):
    tour = Tour.query.get_or_404(id)
    return render_template('tour-detail.html', tour=tour)

@bp.route('/blog')
def blog():
    return render_template('blog.html')

@bp.route('/reviews')
def reviews():
    reviews = Review.query.order_by(Review.id.desc()).all()
    return render_template('reviews.html', reviews=reviews)

@bp.route('/trends')
def trends():
    trending_tours = Tour.query.order_by(Tour.price.desc()).limit(3).all()
    return render_template('trends.html', tours=trending_tours)