from app import app
from models import db, User, Article

with app.app_context():
    print("Seeding database...")

    # Clear old data
    Article.query.delete()
    User.query.delete()

    # Create sample users
    alice = User(username="alice")
    bob = User(username="bob")
    charlie = User(username="charlie")

    db.session.add_all([alice, bob, charlie])
    db.session.commit()

    # Create sample articles
    articles = [
        Article(author="Alice", title="Flask Sessions", content="Learning about sessions in Flask.",
                preview="Intro to Flask sessions", minutes_to_read=5, user_id=alice.id),
        Article(author="Bob", title="React & Flask", content="Connecting React frontend to Flask backend.",
                preview="Frontend meets backend", minutes_to_read=7, user_id=bob.id),
    ]

    db.session.add_all(articles)
    db.session.commit()

    print("Done seeding!")
