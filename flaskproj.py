from flask import Flask, url_for, render_template, request, redirect, flash, jsonify
app = Flask(__name__)
from database_setup import Restaurant, Base, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/main')
def helloWorld():
	return render_template("templates/main.html")

# @app.route('/restaurants')
# def allRestaurants():
# 	rs = session.query(Restaurant).all()
# 	output = ''
# 	for r in rs:
# 		output += '<a href=/restaurants/%s>%s</a>'%(r.id, r.name)
# 		output += '<br>'
# 		output += '<br>'
# 	return output

# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods = ['GET', 'POST'])
# def editMenuItem(restaurant_id, menu_id):
# 	item = session.query(MenuItem).filter_by(id=menu_id).one()
# 	item = [item]
# 	if request.method == 'POST':
# 		oldname = item[0].name
# 		session.delete(item[0])
# 		item[0].name = request.form['newname']
# 		session.add(item[0])
# 		session.commit()
# 		flash("%s renamed to %s"%(oldname, item[0].name))
# 		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
# 	elif request.method == 'GET':
# 		print "METHOD of editMenuItem = GET; restaurant_id=%s, item=%s"%(restaurant_id, item[0].name)
# 		return render_template("editmenuitem.html", restaurant_id=restaurant_id, item=item[0] )

# @app.route('/restaurants/<int:restaurant_id>/new', methods = ['GET', 'POST'])
# def newMenuItem(restaurant_id):
# 	if request.method == 'POST':
# 		newItem = MenuItem(name=request.form['name'], restaurant_id = restaurant_id)
# 		session.add(newItem)
# 		session.commit()
# 		flash("New Menu Item Created! %s"%request.form['name'])
# 		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
# 	elif request.method == 'GET':
# 		return render_template("newmenuitem.html", restaurant_id=restaurant_id)


# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
# def deleteMenuItem(restaurant_id, menu_id):
# 	session.delete(session.query(MenuItem).filter_by(id=menu_id).one())
# 	session.commit()
# 	flash("Item ID %s deleted"%menu_id)
# 	return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))


# @app.route('/restaurants/<int:restaurant_id>/')
# def restaurantMenu(restaurant_id):
# 	r = session.query(Restaurant).filter_by(id = restaurant_id).one()
# 	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
# 	urllist = {}
# 	for i in items:
# 		urllist[i.id] = {}
# 		for a in ("edit", "delete"):
# 			urllist[i.id][a] = url_for('%sMenuItem'%a, restaurant_id = r.id, menu_id = i.id)
# 	return render_template("menu.html", restaurant = r, items = items, urllist = urllist)

# @app.route('/restaurants/<int:restaurant_id>/JSON')
# def restaurantMenuJSON(restaurant_id):
# 	r = session.query(Restaurant).filter_by(id = restaurant_id).one()
# 	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
# 	return jsonify(MenuItems=[i.serialize for i in items])

# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/JSON')
# def restaurantMenuItemJSON(restaurant_id,menu_id):
# 	i = session.query(MenuItem).filter_by(id = menu_id).one()
# 	return jsonify(MenuItems=[i.serialize])

	
if __name__ == '__main__':
	app.secret_key = 'my_foot_smells'
	app.debug = True
	app.run(host='0.0.0.0', port = 5000)