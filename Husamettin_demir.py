#AD-SOYAD:HÜSAMETTİN DEMİR
#NO:021950796058
#Uygulama, urunler isimli bir listeyi kullanıyor. 
#GET, POST ve DELETE taleplerini nasıl karşılayacağımızı @app.route nitelikleri ile metodlarımızın başında belirtiyoruz.
 #Örneğin get_urunler metodu başında belirtilen nitelik içeriğine göre http://localhost:5000/azon/api/urunler adresine gelecek olan GET taleplerini ele alacak
from flask import Flask, jsonify
from flask import make_response
from flask import request
 
urunler = [
    {
        'id': 1000,
        'title': 'Stabilo kalem seti',
        'description': '16li renk paketi', 
        'price': 50,
        'category':'Kirtasiye',
        'inStock':True
    },
    {
        'id': 1002,
        'title': 'Python Programming',
        'description': 'Python programlama ile ilgili giris seviye kitap', 
        'price': 60,
        'category':'Kitap',
        'inStcok':False
    },
    {
        'id': 1003,
        'title': 'Mini iPod',
        'description': '80 Gb Kapasiteli MP3 Calar', 
        'price': 200,
        'category':'Elektronik',
        'inStock':True
    }
]
 
app = Flask(__name__)
 
@app.route('/azon/api/urunler', methods=['GET'])
def get_urunler():
    return jsonify({'urunler': urunler})
 
@app.route('/azon/api/urunler/<int:urun_id>', methods=['GET'])
def get_urun(urun_id):
    urun = [urun for urun in urunler if urun['id'] == urun_id]
    if len(urun) == 0:
        return jsonify({'urun': 'Not found'}),404
    return jsonify({'urun': urun})
 
@app.route('/azon/api/urunler', methods=['POST'])
def create_urun():
    newProduct = {
        'id': urunler[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'price':request.json.get('price', 1),
        'category':request.json['category'],
        'inStock': request.json.get('inStock', False)
    }
    urunler.append(newProduct)
    return jsonify({'urun': newProduct}), 201
 
@app.route('/azon/api/urunler/<int:urun_id>', methods=['DELETE'])
def delete_urun(urun_id):
    urun = [urun for urun in urunler if urun['id'] == urun_id]
    if len(urun) == 0:
        return jsonify({'urun': 'Not found'}), 404
    urunler.remove(urun[0])
    return jsonify({'result': True})
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'HTTP 404 Error': 'The content you looks for does not exist. Please check your request.'}), 404)
 
if __name__ == '__main__':
    app.run(debug=True)#!flask/bin/python





