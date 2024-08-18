from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simulated responses for each category
responses = {
    "علائم شایع": [
        "سردرد، تب و گلودرد از علائم شایع سرماخوردگی هستند.",
        "اگر علائم شدید یا طولانی مدت دارید، با پزشک مشورت کنید.",
    ],
    "تغذیه سالم": [
        "مصرف میوه و سبزیجات را افزایش دهید.",
        "از مصرف غذاهای فرآوری شده و پر نمک خودداری کنید.",
    ],
    "ورزش و تناسب اندام": [
        "روزانه حداقل 30 دقیقه ورزش کنید.",
        "ترکیبی از تمرینات هوازی و قدرتی را در برنامه خود بگنجانید.",
    ],
    "اطلاعات دارویی": [
        "همیشه داروها را طبق دستور پزشک مصرف کنید.",
        "از عوارض جانبی احتمالی داروها آگاه باشید.",
    ],
    "مدیریت استرس": [
        "تکنیک‌های تنفس عمیق را تمرین کنید.",
        "مدیتیشن می‌تواند به کاهش استرس کمک کند.",
    ],
    "بهبود خواب": [
        "سعی کنید هر شب در ساعت مشخصی بخوابید و بیدار شوید.",
        "از استفاده از وسایل الکترونیکی قبل از خواب خودداری کنید.",
    ],
    "واکسیناسیون": [
        "واکسیناسیون یکی از مؤثرترین روش‌های پیشگیری از بیماری‌هاست.",
        "برنامه واکسیناسیون خود را به روز نگه دارید.",
    ],
    "پیشگیری از بیماری‌ها": [
        "دست‌های خود را مرتباً بشویید.",
        "از ماسک در مکان‌های شلوغ استفاده کنید.",
    ],
    "سلامت قلب": [
        "ورزش منظم برای سلامت قلب ضروری است.",
        "رژیم غذایی سرشار از میوه، سبزیجات و غلات کامل داشته باشید.",
    ],
    "آلرژی‌ها": [
        "از عوامل آلرژی‌زا دوری کنید.",
        "در صورت نیاز، از داروهای ضد آلرژی استفاده کنید.",
    ],
    "مراقبت پوست و مو": [
        "روزانه از ضد آفتاب استفاده کنید.",
        "موهای خود را به آرامی شانه کنید تا از آسیب جلوگیری شود.",
    ],
    "سلامت روان": [
        "با دوستان و خانواده در ارتباط باشید.",
        "در صورت نیاز، از کمک متخصصان سلامت روان بهره ببرید.",
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Check if the user message matches any category
    for category, resp in responses.items():
        if category.lower() in user_message.lower():
            return jsonify({'response': random.choice(resp)})
    
    # If no category matches, return a default response
    return jsonify({'response': 'متأسفم، نمی‌توانم به این سؤال پاسخ دهم. لطفاً سؤال دیگری بپرسید یا از گزینه‌های موجود انتخاب کنید.'})

@app.route('/category', methods=['POST'])
def category_response():
    category = request.json['category']
    if category in responses:
        return jsonify({'response': random.choice(responses[category])})
    return jsonify({'response': 'متأسفم، اطلاعاتی در مورد این دسته ندارم.'})

if __name__ == '__main__':
    app.run(debug=True)
