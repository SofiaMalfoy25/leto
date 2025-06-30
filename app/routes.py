from flask import render_template
from app import app
from app.models import Tour, Review

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/tours')
def tours():
    tours = Tour.query.all()
    return render_template('tours.html', tours=tours)

@app.route('/tour/<int:id>')
def tour_detail(id):
    tour = Tour.query.get_or_404(id)
    return render_template('tour-detail.html', tour=tour)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/reviews')
def reviews():
    reviews = Review.query.order_by(Review.id.desc()).all()
    return render_template('reviews.html', reviews=reviews)

@app.route('/trends')
def trends():
    trending_tours = Tour.query.order_by(Tour.price.desc()).limit(3).all()
    return render_template('trends.html', tours=trending_tours)