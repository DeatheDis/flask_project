from app import db


class Agent(db.Model):
    __tablename__ = 'agents'
    id = db.Column(db.Integer, primary_key=True)
    code_name = db.Column(db.String(50), nullable=False, unique=True)
    agent_number = db.Column(db.String(20), nullable=False)
    agent_email = db.Column(db.String(50), nullable=False, unique=True)
    agent_access = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Agent {self.title}>'







