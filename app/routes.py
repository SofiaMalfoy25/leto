from flask import render_template, Blueprint, request
from app.models import Tour, Review
from app import db
from flask import jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Hello World"

@bp.route('/main')
def main():
    return render_template('main.html')

@bp.route('/tours')
def tours():
    try:
        # Получаем параметры фильтрации
        region = request.args.get('region', type=str)
        price_min = request.args.get('price_min', type=float)
        price_max = request.args.get('price_max', type=float)
        sort_by = request.args.get('sort_by', default='id', type=str)
        
        # Начинаем запрос
        query = Tour.query
        
        # Применяем фильтры
        if region:
            query = query.filter_by(region=region)
        if price_min is not None:
            query = query.filter(Tour.price >= price_min)
        if price_max is not None:
            query = query.filter(Tour.price <= price_max)
        
        # Применяем сортировку
        if sort_by == 'price_asc':
            query = query.order_by(Tour.price.asc())
        elif sort_by == 'price_desc':
            query = query.order_by(Tour.price.desc())
        else:
            query = query.order_by(Tour.id.asc())
        
        # Получаем уникальные регионы для фильтра
        regions = db.session.query(Tour.region).distinct().all()
        regions = [r[0] for r in regions if r[0]]  # Преобразуем список кортежей
        
        tours = query.all()
        
        return render_template(
            'tours.html',
            tours=tours,
            regions=regions,
            current_region=region,
            price_min=price_min,
            price_max=price_max,
            sort_by=sort_by
        )
        
    except Exception as e:
        # Логирование ошибки
        print(f"Error in tours route: {str(e)}")
        return render_template('error.html', message="Произошла ошибка при загрузке туров"), 500

@bp.route('/tour/<int:tour_id>')
def tour_detail(tour_id):
    tour = Tour.query.get_or_404(tour_id)
    related_tours = Tour.query.filter(Tour.id != tour_id).limit(3).all()
    return render_template('tour-detail.html', tour=tour, related_tours=related_tours)

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

@bp.route('/debug_tours')
def debug_tours():
    tours = Tour.query.all()
    return {
        'tour_count': len(tours),
        'tours': [{'id': t.id, 'name': t.name} for t in tours]
    }

@bp.route('/tours/filter')
def filter_tours():
    region = request.args.get('region')
    tour_type = request.args.get('type')
    price_range = request.args.get('price')
    
    query = Tour.query
    
    if region and region != 'all':
        query = query.filter(Tour.region.ilike(f'%{region}%'))
    
    if tour_type and tour_type != 'all':
        query = query.filter(Tour.type.ilike(f'%{tour_type}%'))
    
    if price_range and price_range != 'all':
        if price_range == '0-40000':
            query = query.filter(Tour.price <= 40000)
        elif price_range == '40000-50000':
            query = query.filter(Tour.price.between(40000, 50000))
        elif price_range == '50000-70000':
            query = query.filter(Tour.price.between(50000, 70000))
        elif price_range == '70000+':
            query = query.filter(Tour.price > 70000)
    
    tours = query.all()
    return jsonify([{
        'id': t.id,
        'name': t.name,
        'region': t.region,
        'type': t.type,
        'price': t.price,
        'image': t.image
    } for t in tours])