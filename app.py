from app import create_app, db
from app.models import Tour, Review  # Импорт моделей для миграций

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Tour': Tour, 'Review': Review}

if __name__ == '__main__':
    app.run(debug=True)