from flask import Flask, request, redirect
import datetime, random

app = Flask(__name__)
orders = []
reviews = [
    {"name": "Mary - Utawala", "stars": "⭐⭐⭐⭐⭐", "text": "Duvet yangu ilirudi safi sana! SashaJey ni best."},
    {"name": "Kevin - Thorojo", "stars": "⭐⭐⭐⭐⭐", "text": "Walinipickia nguo 7am, wakadeliver 6pm same day. Very fast!"},
    {"name": "Grace - Utawala", "stars": "⭐⭐⭐⭐⭐", "text": "Bei ni poa, Wash & Fold 100/Kg tu."},
]
services = [
    {"name": "Wash & Fold", "price": 100, "unit": "/Kg", "time": "24 Hours", "desc": "Wash, dry, fold neatly. Best for everyday clothes."},
    {"name": "Wash & Iron", "price": 250, "unit": "/Kg", "time": "24 Hours", "desc": "Wash + Iron + Fold. For office wear, shirts, uniforms."},
    {"name": "Dry Cleaning", "price": 350, "unit": "per item", "time": "48 Hours", "desc": "For suits, blazers, dresses, delicate fabrics."},
    {"name": "Duvet", "price": 500, "unit": "per duvet", "time": "24-48 Hours", "desc": "Single, Double, King size duvets & blankets."},
    {"name": "Shoes", "price": 400, "unit": "per pair", "time": "24 Hours", "desc": "Sneakers, school shoes, leather shoes."},
    {"name": "Curtains", "price": 200, "unit": "per piece", "time": "48 Hours", "desc": "Curtains, sheers, nets. Gentle wash."},
    {"name": "Baby Clothes", "price": 200, "unit": "/Kg", "time": "24 Hours", "desc": "Baby-safe detergent, gentle wash."},
    {"name": "Towels", "price": 150, "unit": "/Kg", "time": "24 Hours", "desc": "Bath towels, hand towels. Soft wash."},
    {"name": "Leather Jacket / Jackets", "price": 200, "unit": "per jacket", "time": "48 Hours", "desc": "Leather jackets, hoodies, bombers."},
]

def header():
    return """
    <div style="background:#0066cc; padding:15px;">
        <a href="/" style="color:white; text-decoration:none; font-size:22px; font-weight:bold; font-style:italic;">SashaJey <span style="color:#ff7a00;">Lahndry</span></a>
        <span style="float:right;">
            <a href="/" style="color:white; margin:0 8px; text-decoration:none;">Home</a>
            <a href="/prices" style="color:white; margin:0 8px; text-decoration:none;">Prices</a>
            <a href="/book" style="color:white; margin:0 8px; text-decoration:none;">Book</a>
            <a href="/track" style="color:white; margin:0 8px; text-decoration:none;">Track</a>
            <a href="/reviews" style="color:white; margin:0 8px; text-decoration:none;">Reviews</a>
        </span>
    </div>
    """

def footer():
    return """
    <div style="background:#ff7a00; color:white; padding:25px; text-align:center; font-style:italic;">
        <h3>LOCATION: UTAWALA, THOROJO VILLAGE, NAIROBI</h3>
        <p>CALL / WHATSAPP: 0114820564 | Open Mon-Sat 7am-8pm</p>
        <p>Payment: M-Pesa | Cash on Delivery</p>
        <p>© 2026 SashaJey Lahndry - Clean - Fresh - Trusted</p>
    </div>
    """

def base(title, body):
    return f"""<!DOCTYPE html><html><head><title>{title}</title><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body style="font-family:Arial; margin:0; background:#f0f8ff;">{header()}{body}{footer()}</body></html>"""

@app.route('/')
def home():
    cards = ""
    for s in services:
        cards += f"""<div style="background:white; padding:15px; margin:10px; border-radius:12px; width:260px; display:inline-block; vertical-align:top;"><h3>{s['name']}</h3><p style="color:#ff7a00; font-size:20px; font-weight:bold;">KSH {s['price']} {s['unit']}</p><p>{s['time']}</p><p>{s['desc']}</p><a href="/book" style="background:#0066cc; color:white; padding:8px 15px; text-decoration:none; border-radius:20px;">Book This</a></div>"""
    return base("SashaJey Lahndry", f"""
    <div style="text-align:center; padding:30px; background:white;">
        <h1 style="font-size:48px; font-style:italic; color:#0066cc; margin:0;">SashaJey <span style="color:#ff7a00;">Lahndry</span></h1>
        <p style="font-size:20px; font-style:italic;">Your Clothes, Fresh & Clean in 24 Hours!</p>
        <p>⭐⭐⭐⭐⭐ 5.0 | 200+ Happy Customers | FREE Pickup & Delivery</p>
        <a href="/book" style="background:#ff7a00; color:white; padding:15px 35px; text-decoration:none; border-radius:30px; font-weight:bold;">BOOK PICKUP NOW</a>
        <a href="/prices" style="background:white; border:2px solid #0066cc; color:#0066cc; padding:13px 25px; text-decoration:none; border-radius:30px; font-weight:bold; margin-left:10px;">See Prices</a>
    </div>
    <div style="padding:20px; text-align:center;">
        <h2>WHY CHOOSE SASHAJEY?</h2>
        <p>✅ Fast: 24 Hours Turnaround</p><p>✅ Cheap: From KSH 100/Kg Only</p><p>✅ FREE Pickup & Delivery Over KSH 1000</p><p>✅ Quality Detergents, Ironing Crisp</p><p>✅ We Count Your Clothes, No Loss</p>
    </div>
    <div style="padding:20px; text-align:center; background:#e6f2ff;">
        <h2>HOW IT WORKS</h2><p><b>1. BOOK</b> - WhatsApp 0114820564</p><p><b>2. PICKUP</b> - We come to your house</p><p><b>3. WASH</b> - Wash, dry, iron in Thorojo</p><p><b>4. DELIVER</b> - Deliver clean in 24hrs</p>
    </div>
    <div style="padding:20px; text-align:center;">
    <h2> Our Work - Nguo Tulizofua</h2>
    <p style="color:#666">Hivi ndivyo nguo zako zitakavyoonekana!</p>
    <img src="https://raw.githubusercontent.com/joshuaokotho506-sketch/sashajey-laundry/main/Wash1.jpg" style="width:260px;height:220px;object-fit:cover;border-radius:12px;margin:5px">
    <img src="https://raw.githubusercontent.com/joshuaokotho506-sketch/sashajey-laundry/main/Wash2.jpg" style="width:260px;height:220px;object-fit:cover;border-radius:12px;margin:5px">
    <img src="https://raw.githubusercontent.com/joshuaokotho506-sketch/sashajey-laundry/main/Wash3.jpg" style="width:260px;height:220px;object-fit:cover;border-radius:12px;margin:5px">
    <p><b>Wash & Fold - From KSH 150 / Kg | Wash & Iron - From KSH 250 / Kg</b></p>
    <div style="padding:20px; text-align:center;"><h2>OUR SERVICES</h2>{cards}</div>
    <div style="padding:20px; text-align:center; background:white;">
        <h2>AREAS WE SERVE</h2><p>Thorojo | Utawala | Githunguri | Mihango | Ruai | Kamulu | Joska</p>
        <h2>OPENING HOURS</h2><p>Mon-Sat: 7am - 8pm | Sun: Closed</p>
        <h2>CONTACT</h2><p>Phone / WhatsApp: 0114820564<br>Location: Utawala, Thorojo Village, Nairobi</p>
    </div>""")

@app.route('/prices')
def prices():
    rows = ""
    for s in services:
        rows += f"<tr><td>{s['name']}</td><td><b>KSH {s['price']} {s['unit']}</b></td><td>{s['time']}</td><td>{s['desc']}</td></tr>"
    return base("Prices - SashaJey Lahndry", f"""
    <div style="padding:20px; max-width:900px; margin:auto;"><h1 style="text-align:center;">FULL PRICE LIST</h1>
    <table border="1" style="width:100%; background:white; border-collapse:collapse;"><tr style="background:#0066cc; color:white;"><th>Service</th><th>Price</th><th>Time</th><th>Details</th></tr>{rows}</table>
    <h3>OFFERS:</h3><p>🔥 New Customer: 10% OFF</p><p>🔥 Wash 5Kg+, Get 1Kg FREE</p><p>🔥 Over KSH 1000: FREE Pickup & Delivery</p></div>""")

@app.route('/book', methods=['GET','POST'])
def book():
    if request.method == 'POST':
        oid = f"SJ{random.randint(1000,9999)}"
        orders.append({"id": oid, "name": request.form.get('name'), "phone": request.form.get('phone'), "area": request.form.get('area'), "service": request.form.get('service'), "kg": request.form.get('kg'), "status": "Received - Waiting for Pickup", "time": str(datetime.datetime.now())[:19]})
        return base("Booked! - SashaJey Lahndry", f"""<div style="padding:40px; text-align:center;"><h1>✅ ORDER RECEIVED!</h1><h2>Your Order ID: <span style="color:#ff7a00;">{oid}</span></h2><p>Asante {request.form.get('name')}! Tutakupigia {request.form.get('phone')} in 30 mins.</p><a href="/track">Track My Order</a><br><br><a href="/">Back Home</a></div>""")
    options = "".join([f"<option>{s['name']} - KSH {s['price']} {s['unit']}</option>" for s in services])
    return base("Book - SashaJey Lahndry", f"""
    <div style="padding:20px; max-width:550px; margin:auto; background:white; border-radius:15px;"><h1>BOOK FREE PICKUP</h1>
    <form method="POST">
        <p>Your Name:<br><input name="name" required style="width:100%; padding:12px;"></p>
        <p>Phone:<br><input name="phone" placeholder="0114820564" required style="width:100%; padding:12px;"></p>
        <p>Area / House No:<br><input name="area" placeholder="Thorojo, House 12" required style="width:100%; padding:12px;"></p>
        <p>Service:<br><select name="service" style="width:100%; padding:12px;">{options}</select></p>
        <p>Kg / Items:<br><input name="kg" placeholder="e.g. 5 Kg" style="width:100%; padding:12px;"></p>
        <button style="background:#ff7a00; color:white; padding:15px; width:100%; border:none; border-radius:30px; font-weight:bold;">SUBMIT BOOKING</button>
    </form></div>""")

@app.route('/track', methods=['GET','POST'])
def track():
    result = ""
    if request.method == 'POST':
        oid = request.form.get('oid','').strip().upper()
        found = [o for o in orders if o['id']==oid]
        if found:
            o = found[0]
            result = f"<div style='background:#e6ffe6; padding:15px;'><h3>Order {o['id']} Found!</h3><p>{o['name']} - {o['service']} - <b>{o['status']}</b></p></div>"
        else:
            result = f"<p style='color:red;'>Order {oid} not found. WhatsApp 0114820564</p>"
    return base("Track - SashaJey Lahndry", f"""<div style="padding:30px; max-width:500px; margin:auto; text-align:center; background:white; border-radius:15px;"><h1>TRACK YOUR ORDER</h1><form method="POST"><input name="oid" placeholder="SJ...." style="padding:12px; width:70%;"><button style="padding:12px; background:#0066cc; color:white;">Track</button></form>{result}</div>""")

@app.route('/reviews', methods=['GET','POST'])
def reviews_page():
    if request.method == 'POST':
        reviews.append({"name": request.form.get('name'), "stars": "⭐⭐⭐⭐⭐", "text": request.form.get('text')})
        return redirect('/reviews')
    cards = "".join([f"<div style='background:white; padding:15px; margin:10px; border-radius:10px;'><b>{r['name']}</b> {r['stars']}<p>{r['text']}</p></div>" for r in reviews])
    return base("Reviews - SashaJey Lahndry", f"""<div style="padding:20px; max-width:600px; margin:auto;"><h1 style="text-align:center;">CUSTOMER REVIEWS</h1>{cards}<h2>Leave Review:</h2><form method="POST"><input name="name" placeholder="Your Name" required style="width:100%; padding:12px;"><textarea name="text" placeholder="How was service?" required style="width:100%; padding:12px;"></textarea><button style="background:#ff7a00; color:white; padding:12px; width:100%; border:none;">Submit</button></form></div>""")

@app.route('/admin')
def admin():
    rows = "".join([f"<tr><td>{o['id']}</td><td>{o['name']}<br>{o['phone']}</td><td>{o['service']}</td><td>{o['area']}</td><td>{o['status']}</td></tr>" for o in orders]) or "<tr><td colspan='5'>No orders yet</td></tr>"
    return base("Admin - SashaJey Lahndry", f"""<div style="padding:20px;"><h1>ADMIN - ALL ORDERS ({len(orders)})</h1><table border="1" style="width:100%; background:white; border-collapse:collapse;"><tr style="background:#0066cc; color:white;"><th>ID</th><th>Customer</th><th>Service</th><th>Area</th><th>Status</th></tr>{rows}</table></div>""")

import os
# ===== PRICE LIST + WHATSAPP + MORE PHOTOS =====
@app.route('/prices-list')
def prices_page():
    return base("Prices - SashaJey Laundry", """
    <div style="padding:20px;max-width:800px;margin:auto;">
    <h2>💰 Price List - No Hidden Charges</h2>
    <table style="width:100%;border-collapse:collapse;background:white;">
    <tr style="background:#0a7cff;color:white;"><th style="padding:12px;text-align:left;">Service</th><th>Price</th><th>Time</th></tr>
    <tr><td style="padding:12px;">Wash & Fold (per Kg)</td><td><b>KSH 150</b></td><td>24 Hours</td></tr>
    <tr><td style="padding:12px;">Wash & Iron (per Kg)</td><td><b>KSH 250</b></td><td>24 Hours</td></tr>
    <tr><td style="padding:12px;">Dry Cleaning</td><td><b>KSH 350</b></td><td>48 Hours</td></tr>
    <tr><td style="padding:12px;">Duvet - Single</td><td><b>KSH 500</b></td><td>48 Hours</td></tr>
    <tr><td style="padding:12px;">Duvet - Double / King</td><td><b>KSH 800</b></td><td>48 Hours</td></tr>
    <tr><td style="padding:12px;">Shoes / Sneakers</td><td><b>KSH 400</b></td><td>48 Hours</td></tr>
    </table>
    <br>
    <h2>📸 More Of Our Work</h2>
    <img src="https://raw.githubusercontent.com/joshuaokotho506-sketch/sashajey-laundry/main/Wash4.jpg" style="width:260px;height:220px;object-fit:cover;border-radius:12px;margin:5px;">
    <img src="https://raw.githubusercontent.com/joshuaokotho506-sketch/sashajey-laundry/main/Wash5.jpg" style="width:260px;height:220px;object-fit:cover;border-radius:12px;margin:5px;">
    <img src="https://raw.githubusercontent.com/joshuaokotho506-sketch/sashajey-laundry/main/Wash6.jpg" style="width:260px;height:220px;object-fit:cover;border-radius:12px;margin:5px;">
    <br><br>
    <a href="https://wa.me/254700000000?text=Hi%20SashaJey%20Laundry!%20Nataka%20ku-book" style="background:#25D366;color:white;padding:14px 22px;border-radius:30px;font-weight:bold;text-decoration:none;">💬 Order on WhatsApp</a>
    </div>
    """)
if __name__== '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0', port=port) 
