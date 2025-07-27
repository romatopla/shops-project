import pandas as pd  
import os 
import random
import string 
from datetime import datetime,timedelta
from collections import defaultdict

dirname = os.path.dirname(__file__)

# Генерируем идентифекатор чека
def generate_doc_id(len=15):
    chars = string.ascii_uppercase + string.digits
    return ''.join([random.choice(chars) for i in range(len)])

# Категории товаров
categories = [
    'бытовая химия',
    'текстиль',
    'посуда',
    'инструменты',
]

# Генерация данных
data = []
for _ in range(100):  # 100 товаров
    category = random.choice(categories)
    
    # Генерация названия в зависимости от категории
    if category == 'бытовая химия':
        name = f"{random.choice(['гель', 'порошок', 'спрей', 'жидкость'])} {random.choice(['для посуды', 'для стирки', 'универсальный'])}"
    elif category == 'текстиль':
        name = f"{random.choice(['полотенце', 'простыня', 'скатерть', 'плед'])} {random.choice(['хлопковый', 'льняной', 'бамбуковый'])}"
    elif category == 'посуда':
        name = f"{random.choice(['кастрюля', 'сковорода', 'тарелка', 'кружка'])} {random.choice(['керамическая', 'стеклянная', 'металлическая'])}"
    elif category == 'инструменты':
        name = f"{random.choice(['дрель', 'молоток', 'веник', 'пасатижи'])} {random.choice(['для дома', 'для хозяйства', 'универсал'])}"
    
    # Генерация цены и скидки
    base_price = round(random.uniform(50, 5000), 2)
    discount = round(random.uniform(0, base_price*0.3), 2) if random.random() > 0.3 else 0  # 30% вероятность отсутствия скидки
 
    
    data.append({
        'item': name,
        'category': category,
        'price': base_price,
        'discount': discount
    })

# Создание DataFrame
df = pd.DataFrame(data)

today = datetime.today()

nums = [1,2,3,4,5]
lenghts = [random.choice(nums) for x in range(10)]

d = defaultdict(list)

for shop_num in [1,2,3]:
    for cash_num in [5,6,7]:
        if today != 0:
            for lenght in lenghts:
                d['doc_id'] += ([generate_doc_id()] * lenght)
                d['shop_num'] += ([shop_num] * lenght)
                d['cash_num'] += ([cash_num] * lenght)
                for _ in range(lenght):
                    curr_num = random.randint(0,99)
                    d['item'].append(df['item'][curr_num])
                    d['category'].append(df['category'][curr_num])
                    d['amount'].append(random.randint(1,7))
                    d['price'].append(df['price'][curr_num])
                    d['discount'].append(df['discount'][curr_num])
        res_df = pd.DataFrame(d)
        res_df.to_csv(os.path.join(dirname,'data',f'{shop_num}_{cash_num}.csv'),index=False)






