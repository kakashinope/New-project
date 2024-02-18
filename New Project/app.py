from flask import Flask, render_template, redirect, request, url_for, session
app = Flask(__name__, template_folder='./home', static_folder='./images')
@app.route('/image/<path:image_path>')
def image_description(image_path):
    # Загальний опис зображення (можна витягнути з бази даних або іншого джерела)
    image_descriptions = {
        "image1.jpg": "Опис першого зображення",
        "image2.jpg": "Опис другого зображення",
        "image3.jpg": "Опис третього зображення"
        # Додайте інші описи зображень, які ви хочете відобразити
    }

    # Перевіряємо, чи є опис для даного шляху зображення
    if image_path in image_descriptions:
        description = image_descriptions[image_path]
    else:
        description = "Опис відсутній"

    return render_template('image_description.html', image_path=image_path, description=description)
# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Сторінка з фактами про космос
@app.route('/facts')
def facts():
    # Тут ви можете додати логіку для отримання фактів з космосу
    facts_list = [

    ]
    return render_template('facts.html', facts=facts_list)
image_list = [(1,"https://searchthisweb.com/wallpaper/thumb1000/main1000_earth_7680x4320_ejea5.jpg", "Земля", "dadada"),
              (2,"https://searchthisweb.com/wallpaper/thumb1000/main1000_mars_3840x2160_jk1uo.jpg", "Марс", "d"),
              (3,"https://preview.free3d.com/img/2015/10/2272980235332880368/zqnrepta.jpg", "Меркурій", "dф"),
              (4,"https://fons.pibig.info/uploads/posts/2023-06/thumbs/1687274049_fons-pibig-info-p-oboi-venera-krasivo-10.jpg", "Венера", "dж"),
              (5,"https://preview.free3d.com/img/2015/10/2272856533563868502/9qi4sllu.jpg", "Юпітер", "dа"),
              (6,"https://preview.free3d.com/img/2017/09/2272956915455624279/qvrtkgyz.jpg", "Сатурн", "dц"),
              (7,"https://i.obozrevatel.com/news/2020/6/4/unnamed.jpg", "Уран", "dв"),
              (8,"https://kartin.papik.pro/uploads/posts/2023-07/thumbs/1688612504_kartin-papik-pro-p-kartinki-planeta-neptun-v-kosmose-14.jpg", "Нептун", "dл"),
              (9,"https://img.freepik.com/premium-photo/pluto-a-planet-in-the-solar-system_297535-4532.jpg", "Плутон", "d"),
              (10,"https://kite.od.ua/wp-content/uploads/scale_1200-10.png", "Седна", "dх"),
              (11,"https://watchers.news/wp-content/uploads/2016/02/sdo_6th_year_sun_2015_f.jpg", "Сонце", "dж"),]
# Сторінка з галереєю
@app.route('/gallery')
def gallery():
    # Тут ви можете додати логіку для отримання списку зображень
    return render_template('gallery.html', images=image_list)
# Сторінка з галереєю
@app.route('/gallery/<id>')
def item_gallery(id):
    for item in image_list:
        if str ( item [0] ) == id:
            return render_template('image_description.html', item=item)
# Сторінка "Про нас"
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
