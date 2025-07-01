from app import create_app, db
from app.models import Tour, Review
from datetime import datetime

def insert_sample_data():
    app = create_app()
    
    with app.app_context():
        # Очистка существующих данных
        db.session.query(Review).delete()
        db.session.query(Tour).delete()
        db.session.commit()

        # Создаем туры
        tours_data = [
            {
                "name": "Золотое кольцо России",
                "description": "7-дневный тур по древним городам России",
                "price": 45000,
                "duration": "7 дней",
                "image": "golden-ring.jpg",
                "places": "Москва, Сергиев Посад, Ростов Великий, Ярославль, Кострома, Иваново, Владимир"
            },
            {
                "name": "Северное сияние: Путешествие по Карелии",
                "description": "5-дневный тур по живописным местам Карелии",
                "price": 38000,
                "duration": "5 дней",
                "image": "karelia.jpg",
                "places": "Санкт-Петербург, Петрозаводск, Кижи, Сортавала, Рускеала"
            },
            {
                "name": "Сибирское путешествие",
                "description": "10-дневный тур по Сибири",
                "price": 75000,
                "duration": "10 дней",
                "image": "siberia.jpg",
                "places": "Новосибирск, Барнаул, Горно-Алтайск, Алтайский заповедник, Бийск, Томск, Кемерово, Красноярск"
            },
            {
                "name": "Сказочный Алтай",
                "description": "6-дневный тур по Алтаю",
                "price": 45000,
                "duration": "6 дней",
                "image": "altai.jpg",
                "places": "Горно-Алтайск, Алтайский заповедник, Озеро Ая, Шебалино, Чуйский тракт, Курайская степь"
            },
            {
                "name": "Сокровища Дагестана",
                "description": "7-дневный тур по Дагестану",
                "price": 50000,
                "duration": "7 дней",
                "image": "dagestan.jpg",
                "places": "Махачкала, Сулакский каньон, Дербент, Гергебиль, Хунзах, Лезгинский национальный парк"
            },
            {
                "name": "Сокровища Северной Осетии",
                "description": "6-дневный тур по Северной Осетии",
                "price": 45000,
                "duration": "6 дней",
                "image": "north-ossetia.jpg",
                "places": "Владикавказ, Алания, Архонская долина, Цейское ущелье, Казбек, Фарнский водопад"
            },
            {
                "name": "Приключения на Кавказе",
                "description": "7-дневный тур по Кавказу",
                "price": 55000,
                "duration": "7 дней",
                "image": "caucasus.jpg",
                "places": "Владикавказ, Эльбрус, Кисловодск, Приэльбрусье, Железноводск, Архыз"
            },
            {
                "name": "Сокровища Байкала",
                "description": "6-дневный тур по Байкалу",
                "price": 48000,
                "duration": "6 дней",
                "image": "baikal.jpg",
                "places": "Иркутск, Ольхон, Мыс Хобой, Листвянка, Байкальский музей"
            },
            {
                "name": "Сокровища Сахалина",
                "description": "7-дневный тур по Сахалину",
                "price": 55000,
                "duration": "7 дней",
                "image": "sakhalin.jpg",
                "places": "Южно-Сахалинск, Курилы, Невельск, Тихая бухта, Мыс Кекур"
            },
            {
                "name": "Ингушетия",
                "description": "5-дневный тур по Ингушетии",
                "price": 45000,
                "duration": "5 дней",
                "image": "ingushetia.jpg",
                "places": "Магас, Ведучи, Техи, Ингушские башни, Провал"
            },
            {
                "name": "Ивановские озера Хакасии",
                "description": "4-дневный тур по Хакасии",
                "price": 38000,
                "duration": "4 дня",
                "image": "khakassia.jpg",
                "places": "Ивановские озера, Национальный парк, Село Шира, Гора Таганай"
            },
            {
                "name": "Южно-Чуйское кольцо",
                "description": "7-дневный конный тур по Алтаю",
                "price": 55000,
                "duration": "7 дней",
                "image": "chuya-ring.jpg",
                "places": "Чуйский тракт, Гора Белуха, Озеро Аккем, Курган 'Скрижаль'"
            },
            {
                "name": "Приключения на Камчатке",
                "description": "6-дневный тур по Камчатке",
                "price": 70000,
                "duration": "6 дней",
                "image": "kamchatka.jpg",
                "places": "Вулкан Ключевская сопка, Долина гейзеров, Кратер вулкана Мутновский"
            },
            {
                "name": "Загадки Кольского полуострова",
                "description": "5-дневный тур по Кольскому полуострову",
                "price": 55000,
                "duration": "5 дней",
                "image": "kola.jpg",
                "places": "Мурманск, Кировск, Лапландский заповедник, Кола"
            },
            {
                "name": "Солнечный Крым",
                "description": "7-дневный тур по Крыму",
                "price": 45000,
                "duration": "7 дней",
                "image": "crimea.jpg",
                "places": "Симферополь, Ялта, Ливадийский дворец, Севастополь, Балаклава"
            }
        ]

        tours = [Tour(**data) for data in tours_data]
        db.session.add_all(tours)
        db.session.commit()

        # Создаем отзывы
        reviews_data = [
            {
                "author": "Константин",
                "rating": 5,
                "text": "Отличный тур! Всё организовано на высшем уровне.",
                "date": datetime(2024, 8, 15),
                "tour_id": 1,
                "likes": 24
            },
            {
                "author": "Екатерина",
                "rating": 5,
                "text": "Прекрасное путешествие, незабываемые впечатления!",
                "date": datetime(2024, 7, 10),
                "tour_id": 8,
                "likes": 32
            },
            {
                "author": "Андрей",
                "rating": 4,
                "text": "Хороший тур, но хотелось бы больше свободного времени.",
                "date": datetime(2024, 6, 25),
                "tour_id": 2,
                "likes": 15
            },
            {
                "author": "Ольга",
                "rating": 5,
                "text": "Лучший отпуск в моей жизни! Обязательно вернусь снова.",
                "date": datetime(2024, 9, 5),
                "tour_id": 15,
                "likes": 42
            },
            {
                "author": "Дмитрий",
                "rating": 3,
                "text": "Неплохо, но некоторые экскурсии можно было организовать лучше.",
                "date": datetime(2024, 7, 18),
                "tour_id": 3,
                "likes": 8
            },
            {
                "author": "Анна",
                "rating": 5,
                "text": "Всё понравилось! Гид был очень профессиональный.",
                "date": datetime(2024, 8, 22),
                "tour_id": 5,
                "likes": 27
            },
            {
                "author": "Иван",
                "rating": 4,
                "text": "Интересный маршрут, комфортное проживание.",
                "date": datetime(2024, 7, 30),
                "tour_id": 7,
                "likes": 19
            },
            {
                "author": "Мария",
                "rating": 5,
                "text": "Прекрасная организация, отличные впечатления!",
                "date": datetime(2024, 9, 12),
                "tour_id": 12,
                "likes": 35
            }
        ]

        reviews = [Review(**data) for data in reviews_data]
        db.session.add_all(reviews)
        db.session.commit()

        print(f"Успешно добавлено: {len(tours)} туров и {len(reviews)} отзывов")

if __name__ == '__main__':
    insert_sample_data()