from sqlalchemy.exc import IntegrityError
from flask import render_template, request, url_for, redirect, current_app, flash
from app.forms import ContactForm, AgentForm
from app.models import Agent
from app import db
from codename import codename


@current_app.route('/')
@current_app.route('/agents')
def get_agents():
    search = request.args.get('search')
    access = request.args.get('access')

    query = Agent.query

    if search:
        query = query.filter(Agent.code_name.ilike(f'%{search}%'))

    if access:
        query = query.filter_by(agent_access=access)

    agents = query.all()

    if search or access:
        if not agents:
            flash('Агенты не найдены', 'danger')

    return render_template('agents.html', agents=agents)


@current_app.route('/add', methods=['GET', 'POST'])
def add_agent():
    random_name = codename(capitalize=True)
    form = AgentForm()
    form.code_name.data = random_name

    if form.validate_on_submit():
        new_agent = Agent(
            code_name=form.code_name.data,
            agent_number=form.agent_number.data,
            agent_email=form.agent_email.data,
            agent_access=form.agent_access.data
        )
        db.session.add(new_agent)
        try:
            db.session.commit()
            flash('Агент успешно добавлен', 'success')
            return redirect(url_for('get_agents'))
        except IntegrityError:
            db.session.rollback()
            flash('Ошибка: такой email уже используется', 'danger')

    return render_template('add_agent.html', form=form, button_text='Добавить')


@current_app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)
    form = AgentForm(obj=agent)

    if form.validate_on_submit():
        form.populate_obj(agent)

        try:
            db.session.commit()
            flash('Информация обновлена', 'success')
            return redirect(url_for('get_agents'))
        except IntegrityError:
            db.session.rollback()
            flash('Ошибка: такой email уже используется', 'danger')

    return render_template('edit_agent.html', form=form, agent=agent, button_text='Редактировать')


@current_app.route('/agent_profile/<int:id>', methods=['GET', 'POST'])
def agent_profile(id):
    agent = Agent.query.get_or_404(id)
    return render_template('agent_profile.html', agent=agent)


@current_app.route('/delete/<int:id>')
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('get_agents'))


@current_app.route('/delete_all')
def delete_all_agents():
    Agent.query.delete()
    db.session.commit()
    return redirect(url_for('get_agents'))


@current_app.route('/send_email/<int:id>', methods=['GET', 'POST'])
def send_email(id):
    agent = Agent.query.get_or_404(id)
    form = ContactForm(email=agent.agent_email)

    if form.validate_on_submit():
        flash('Your message has been sent.', 'success')
        return redirect(url_for('send_email', id=id))

    if request.method == 'POST':
        flash('Ошибка отправки сообщения', 'danger')

    return render_template('send_email.html', agent=agent, form=form)





