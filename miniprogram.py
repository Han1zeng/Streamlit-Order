import streamlit as st
import time

# ====================== 1. 页面全局配置 ======================
st.set_page_config(
    page_title="悦味轩·精致餐厅 - 自助点餐系统",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== 2. 样式精准修复 ======================
st.markdown("""
<style>
    /* 全局背景与基础样式 */
    .stApp {
        background-color: #fdf6ef !important;
    }
    .main, .block-container {
        background-color: #fdf6ef !important;
    }
    * {
        font-family: "Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", sans-serif;
        box-sizing: border-box;
    }
    .block-container {
        padding-top: 0;
        padding-bottom: 8rem;
        max-width: 1400px;
    }
  
    /* 顶部店铺Header */
    .restaurant-header {
        text-align: center;
        padding: 2.2rem 1rem;
        background: linear-gradient(135deg, #ff7e42 0%, #ff9a56 100%);
        color: #fff;
        border-radius: 0 0 28px 28px;
        margin-bottom: 1rem;
        box-shadow: 0 8px 28px rgba(255, 126, 66, 0.22);
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
    }
    .restaurant-name {
        font-size: 2.6rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: 3px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.15);
        text-align: center;
        width: 100%;
        line-height: 1.2;
    }
    .restaurant-slogan {
        font-size: 1rem;
        margin: 0.6rem 0 0 0;
        opacity: 0.95;
        font-weight: 300;
        letter-spacing: 1px;
        text-align: center;
        width: 100%;
        line-height: 1.4;
    }

    /* 顶部分类按钮 - 字体放大到1.3rem */
    .top-category-nav {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        padding: 0 1rem 1.5rem;
        flex-wrap: wrap;
    }
    .top-category-nav .stButton > button {
        background: linear-gradient(135deg, #ff7e42 0%, #ff9a56 100%) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.7rem 1.8rem !important;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
        min-width: fit-content !important;
        height: auto !important;
    }
    .top-category-nav .stButton > button:hover {
        transform: scale(1.05) !important;
        background: linear-gradient(135deg, #ff6333 0%, #ff451a 100%) !important;
        color: #fff !important;
    }
  
    /* 分类标题 */
    .category-title {
        font-size: 1.7rem;
        font-weight: 700;
        color: #5c3c25;
        margin-bottom: 1.5rem;
        padding: 0.7rem 1.2rem;
        background: linear-gradient(90deg, #ffe8d6 0%, transparent 100%);
        border-radius: 10px;
        border-left: 6px solid #ff7e42;
    }
  
    /* 菜品卡片 */
    .dish-card {
        background-color: #ffffff;
        border-radius: 18px;
        padding: 0;
        margin-bottom: 2rem;
        box-shadow: 0 6px 22px rgba(92, 60, 37, 0.09);
        transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        overflow: hidden;
        height: 100%;
        border: 1px solid #fff0e6;
        display: flex;
        flex-direction: column;
    }
    .dish-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 14px 36px rgba(92, 60, 37, 0.16);
    }
    .dish-img-container {
        width: 100%;
        height: 200px;
        overflow: hidden;
        border-bottom: 2px solid #fff0e6;
        flex-shrink: 0;
    }
    .dish-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
        display: block;
    }
    .dish-card:hover .dish-img {
        transform: scale(1.1);
    }
    .dish-info {
        padding: 1.3rem;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        text-align: left;
    }
    .dish-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #3e2723;
        margin: 0 0 0.5rem 0;
        text-align: left;
    }
    .dish-desc {
        font-size: 0.88rem;
        color: #795548;
        margin: 0 0 1rem 0;
        line-height: 1.5;
        text-align: left;
    }
    .dish-bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .price-tag {
        color: #d32f2f;
        font-size: 1.45rem;
        font-weight: 800;
    }
  
    /* ============= 【核心修复】加减按钮 ============= */
    button[data-testid^="baseButton-reduce_"],
    button[data-testid^="baseButton-add_"] {
        width: 20px !important;
        height: 20px !important;
        min-width: 20px !important;
        min-height: 20px !important;
        max-width: 20px !important;
        max-height: 20px !important;
        border-radius: 50% !important;
        padding: 0px !important;
        margin: 0px !important;
        line-height: 1 !important;
        background: linear-gradient(135deg, #ff7e42 0%, #ff9a56 100%) !important;
        color: #fff !important;
        border: none !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        flex-shrink: 0 !important;
        white-space: nowrap !important;
    }
    
    button[data-testid^="baseButton-reduce_"]:hover,
    button[data-testid^="baseButton-add_"]:hover {
        transform: scale(1.1) !important;
        background: linear-gradient(135deg, #ff6333 0%, #ff451a 100%) !important;
    }
    
    button[data-testid^="baseButton-reduce_"]:focus,
    button[data-testid^="baseButton-add_"]:focus {
        box-shadow: none !important;
        outline: none !important;
    }

    /* 【核心修复】按钮行容器 - 使用原生 flexbox */
    .btn-row-container {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 2.5rem !important;
        width: 100% !important;
        flex-wrap: nowrap !important;
        margin-top: 1rem;
        padding: 0 !important;
    }

    /* 减少按钮容器 */
    .btn-item {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        flex: 0 0 auto !important;
        width: auto !important;
    }

    /* 数字显示容器 */
    .count-display {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 20px !important;
        height: 20px !important;
        flex: 0 0 20px !important;
    }

    /* 菜品数量 */
    .count-number {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: #3e2723 !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1 !important;
        white-space: nowrap !important;
        display: block !important;
    }
  
    /* ============= 【修复】侧边栏字体 ============= */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff5ee 0%, #ffe8d6 100%);
        box-shadow: 4px 0 18px rgba(92, 60, 37, 0.08);
    }
    [data-testid="stSidebar"] h2 {
        color: #5c3c25 !important;
        font-weight: 700 !important;
        font-size: 1.5rem !important;
        margin-bottom: 0.8rem !important;
    }
    /* 【修复】分类条目字体放大到1.5rem */
    [data-testid="stSidebar"] .stRadio > div > label {
        font-size: 1.5rem !important;
        font-weight: 500 !important;
        color: #5c3c25 !important;
    }
    /* 【修复】购物车菜品条目字体放大到1.25rem */
    [data-testid="stSidebar"] [role="region"] > div > div > p {
        font-size: 1.25rem !important;
        color: #5c3c25 !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] .stText p {
        font-size: 1.25rem !important;
        color: #5c3c25 !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
    }
    [data-testid="stSidebar"] h3 {
        font-size: 1.4rem !important;
        color: #5c3c25 !important;
        font-weight: 700 !important;
        margin: 0.8rem 0 !important;
    }
  
    /* 底部固定购物车栏 */
    .cart-bar-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(135deg, #5c3c25 0%, #795548 100%);
        padding: 1.1rem 3rem;
        box-shadow: 0 -8px 28px rgba(92, 60, 37, 0.35);
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .cart-left {
        display: flex;
        align-items: center;
        gap: 1.7rem;
    }
    .cart-icon-wrapper {
        position: relative;
    }
    .cart-icon {
        font-size: 2.1rem;
    }
    .cart-badge {
        position: absolute;
        top: -9px;
        right: -9px;
        background: linear-gradient(135deg, #ff451a 0%, #d32f2f 100%);
        color: white;
        font-size: 0.8rem;
        min-width: 22px;
        height: 22px;
        border-radius: 11px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 5px;
        font-weight: 800;
        box-shadow: 0 2px 6px rgba(211, 47, 47, 0.4);
    }
    .cart-total {
        display: flex;
        flex-direction: column;
    }
    .total-label {
        font-size: 0.9rem;
        color: #fff0e6;
        opacity: 0.9;
    }
    .total-price {
        font-size: 1.9rem;
        color: #ffd700;
        font-weight: 800;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .total-count {
        background: rgba(255, 240, 230, 0.2);
        padding: 0.45rem 1.1rem;
        border-radius: 22px;
        font-size: 0.9rem;
        color: #fff0e6;
        border: 1px solid rgba(255, 240, 230, 0.3);
        white-space: nowrap;
        min-width: fit-content;
    }
    
    /* 底部结算按钮 */
    .stButton > button {
        background: linear-gradient(135deg, #ff7e42 0%, #ff6333 100%) !important;
        color: white !important;
        border: none !important;
        padding: 1.1rem 3.3rem !important;
        border-radius: 50px !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 18px rgba(255, 126, 66, 0.35) !important;
        letter-spacing: 1px !important;
        height: fit-content !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.04) !important;
        box-shadow: 0 9px 26px rgba(255, 126, 66, 0.45) !important;
        background: linear-gradient(135deg, #ff6333 0%, #ff451a 100%) !important;
    }
    .stButton > button:disabled {
        opacity: 0.5 !important;
    }
  
    /* 隐藏Streamlit默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    
    /* ====================== 手机端响应式适配 ====================== */
    @media only screen and (max-width: 768px) {
        .restaurant-header {
            padding: 1.2rem 0.8rem;
            margin-bottom: 0.5rem;
        }
        .restaurant-name {
            font-size: 1.8rem;
            letter-spacing: 1px;
        }
        .restaurant-slogan {
            font-size: 0.8rem;
        }
        .top-category-nav {
            gap: 0.8rem;
            padding: 0 0.5rem 1rem;
        }
        .top-category-nav .stButton > button {
            padding: 0.5rem 1rem !important;
            font-size: 1.05rem !important;
        }
        .category-title {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            padding: 0.5rem 1rem;
        }
        [data-testid="column"] {
            flex: 1 1 100% !important;
            max-width: 100% !important;
        }
        .dish-card {
            flex-direction: row !important;
        }
        .dish-img-container {
            width: 35% !important;
            height: auto !important;
            min-height: 120px !important;
            flex-shrink: 0 !important;
        }
        .dish-info {
            width: 65% !important;
            padding: 1rem !important;
            text-align: left !important;
        }
        .dish-name {
            font-size: 1rem !important;
            text-align: left !important;
        }
        .dish-desc {
            font-size: 0.75rem !important;
            text-align: left !important;
            margin-bottom: 0.5rem !important;
        }
        .price-tag {
            font-size: 1.1rem !important;
        }
        .dish-bottom {
            margin-bottom: 0.8rem !important;
        }
        
        /* 【手机端核心修复】按钮行必须保持水平 */
        .btn-row-container {
            display: flex !important;
            flex-direction: row !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 1.5rem !important;
            width: 100% !important;
            flex-wrap: nowrap !important;
            margin-top: 0.5rem !important;
            padding: 0 !important;
        }
        
        .btn-item {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            flex: 0 0 auto !important;
            width: auto !important;
        }
        
        button[data-testid^="baseButton-reduce_"],
        button[data-testid^="baseButton-add_"] {
            width: 18px !important;
            height: 18px !important;
            min-width: 18px !important;
            min-height: 18px !important;
            max-width: 18px !important;
            max-height: 18px !important;
            font-size: 0.8rem !important;
        }
        .count-display {
            width: 18px !important;
            height: 18px !important;
            flex: 0 0 18px !important;
        }
        .count-number {
            font-size: 1rem !important;
        }
        [data-testid="stSidebar"] .stRadio > div > label {
            font-size: 1.25rem !important;
        }
        [data-testid="stSidebar"] .stText p {
            font-size: 1.05rem !important;
        }
        .cart-bar-container {
            padding: 0.8rem 1rem;
        }
        .cart-left {
            gap: 0.8rem;
        }
        .cart-icon {
            font-size: 1.6rem;
        }
        .total-price {
            font-size: 1.4rem;
        }
        .stButton > button {
            padding: 0.8rem 1.5rem !important;
            font-size: 1rem !important;
        }
        .block-container {
            padding-bottom: 7rem;
        }
    }

    @media only screen and (min-width: 768px) and (max-width: 1024px) {
        [data-testid="column"] {
            flex: 1 1 30% !important;
            max-width: 30% !important;
        }
        .cart-bar-container {
            padding: 1rem 2rem;
        }
        .stButton > button {
            padding: 1rem 2.5rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ====================== 3. 餐厅与菜品数据 ======================
RESTAURANT_INFO = {
    "name": "悦味轩·精致餐厅",
    "slogan": "新鲜食材 · 匠心烹饪 · 家的味道",
    "opening_hours": "营业时间：10:00 - 22:00"
}

CATEGORIES = [
    {"id": 1, "name": "🔥 招牌必点"},
    {"id": 2, "name": "🍖 经典热菜"},
    {"id": 4, "name": "🍚 暖心主食"},
    {"id": 5, "name": "🧃 饮品畅饮"},
    {"id": 6, "name": "🍰 甜蜜甜品"}
]

DISHES = [
    # 招牌必点
    {"id": 101, "category_id": 1, "name": "招牌红烧肉", "price": 58, "img": "https://loremflickr.com/400/300/braised-pork,chinese-food", "desc": "精选五花肉，慢火熬制，肥而不腻"},
    {"id": 103, "category_id": 1, "name": "清炒时令蔬", "price": 22, "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop", "desc": "每日新鲜蔬菜，清炒保留原味"},
    {"id": 104, "category_id": 1, "name": "番茄蛋花汤", "price": 18, "img": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&h=300&fit=crop", "desc": "酸甜可口，营养丰富，家常暖心汤"},
  
    # 经典热菜
    {"id": 201, "category_id": 2, "name": "宫保鸡丁", "price": 42, "img": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=400&h=300&fit=crop", "desc": "经典川菜，麻辣鲜香，花生酥脆"},
    {"id": 205, "category_id": 2, "name": "黑椒牛柳", "price": 52, "img": "https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop", "desc": "鲜嫩牛柳配黑椒汁，口感醇厚"},
  
    # 暖心主食
    {"id": 401, "category_id": 4, "name": "扬州炒饭", "price": 25, "img": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&h=300&fit=crop", "desc": "粒粒分明，配料丰富"},
    {"id": 402, "category_id": 4, "name": "鲜虾鸡蛋面", "price": 32, "img": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400&h=300&fit=crop", "desc": "虾舞金汤，面映暖阳"},
    {"id": 403, "category_id": 4, "name": "鲜肉小笼包", "price": 28, "img": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400&h=300&fit=crop", "desc": "皮薄馅大，浓郁爆汁"},
    {"id": 404, "category_id": 4, "name": "牛肉汉堡", "price": 33, "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=400&h=300&fit=crop", "desc": "外焦里嫩，大口满足"},
  
    # 饮品畅饮
    {"id": 501, "category_id": 5, "name": "冰镇柠檬茶", "price": 12, "img": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&h=300&fit=crop", "desc": "手打柠檬配红茶，解暑神器"},
    {"id": 503, "category_id": 5, "name": "鲜榨橙汁", "price": 18, "img": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=400&h=300&fit=crop", "desc": "新鲜橙子现榨，维C满满"},
    {"id": 504, "category_id": 5, "name": "热奶茶", "price": 15, "img": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop", "desc": "醇香奶茶，丝滑顺口"},
  
    # 甜蜜甜品
    {"id": 601, "category_id": 6, "name": "提拉米苏", "price": 28, "img": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400&h=300&fit=crop", "desc": "意式经典，咖啡酒香"},
    {"id": 602, "category_id": 6, "name": "芒果班戟", "price": 22, "img": "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=400&h=300&fit=crop", "desc": "新鲜芒果配淡奶油"},
    {"id": 603, "category_id": 6, "name": "香草冰淇淋", "price": 18, "img": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400&h=300&fit=crop", "desc": "绵密丝滑，香草浓郁"},
]

# ====================== 4. 购物车状态初始化 ======================
if 'cart' not in st.session_state:
    st.session_state.cart = {}
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = CATEGORIES[0]["name"]

# ====================== 5. 辅助功能函数 ======================
def add_to_cart(dish_id):
    if dish_id in st.session_state.cart:
        st.session_state.cart[dish_id] += 1
    else:
        st.session_state.cart[dish_id] = 1

def reduce_from_cart(dish_id):
    if dish_id in st.session_state.cart:
        if st.session_state.cart[dish_id] > 1:
            st.session_state.cart[dish_id] -= 1
        else:
            del st.session_state.cart[dish_id]

def get_cart_total():
    total_price = 0
    total_count = 0
    for dish_id, count in st.session_state.cart.items():
        dish = next((d for d in DISHES if d["id"] == dish_id), None)
        if dish:
            total_price += dish["price"] * count
            total_count += count
    return round(total_price, 2), total_count

def clear_cart():
    st.session_state.cart = {}

def submit_order():
    total_price, total_count = get_cart_total()
    if total_count > 0:
        st.success(f"🎉 下单成功！\n\n您已成功下单{total_count}件商品，合计¥{total_price}\n\n我们会尽快为您备餐，请稍候~")
        st.balloons()
        clear_cart()
        time.sleep(2)
        st.rerun()

# ====================== 6. 页面布局渲染 ======================

# --- 顶部店铺Header ---
st.markdown(f"""
<div class="restaurant-header">
    <h1 class="restaurant-name">{RESTAURANT_INFO['name']}</h1>
    <p class="restaurant-slogan">{RESTAURANT_INFO['slogan']} | {RESTAURANT_INFO['opening_hours']}</p>
</div>
""", unsafe_allow_html=True)

# --- 顶部分类导航 ---
category_names = [c["name"] for c in CATEGORIES]
st.markdown('<div class="top-category-nav">', unsafe_allow_html=True)
top_cat_cols = st.columns(len(CATEGORIES))
for idx, cat in enumerate(CATEGORIES):
    with top_cat_cols[idx]:
        is_active = cat["name"] == st.session_state.selected_category
        if st.button(
            cat["name"],
            key=f"top_cat_{cat['id']}",
            use_container_width=True
        ):
            st.session_state.selected_category = cat["name"]
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- 左侧边栏：分类导航 ---
with st.sidebar:
    st.markdown("## 📋 菜单分类")
    st.markdown("---")
    selected_category_name = st.radio(
        "",
        category_names,
        index=category_names.index(st.session_state.selected_category),
        label_visibility="collapsed"
    )
    if selected_category_name != st.session_state.selected_category:
        st.session_state.selected_category = selected_category_name
        st.rerun()
    st.markdown("---")
  
    # 购物车明细
    total_price, total_count = get_cart_total()
    if total_count > 0:
        st.markdown(f"## 🛒 购物车 ({total_count})")
        for dish_id, count in st.session_state.cart.items():
            dish = next((d for d in DISHES if d["id"] == dish_id), None)
            if dish:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.text(f"{dish['name']} x{count}")
                with col2:
                    st.text(f"¥{dish['price']*count}")
      
        st.markdown("---")
        st.markdown(f"### 合计：¥{total_price}")
      
        if st.button("✅ 确认下单", type="primary", use_container_width=True):
            submit_order()
      
        if st.button("🗑️ 清空购物车", use_container_width=True):
            clear_cart()
            st.rerun()
    else:
        st.info("购物车是空的，快去挑选美食吧~")

# --- 主内容区：菜品列表 ---
current_category = next(c for c in CATEGORIES if c["name"] == selected_category_name)
current_dishes = [d for d in DISHES if d["category_id"] == current_category["id"]]

st.markdown(f'<h2 class="category-title">{current_category["name"]}</h2>', unsafe_allow_html=True)

# 菜品4列布局
cols = st.columns(4)
for idx, dish in enumerate(current_dishes):
    with cols[idx % 4]:
        st.markdown('<div class="dish-card">', unsafe_allow_html=True)
      
        # 菜品图片
        st.markdown(f"""
        <div class="dish-img-container">
            <img class="dish-img" src="{dish['img']}" alt="{dish['name']}" onerror="this.src='https://picsum.photos/400/300?food={dish['name']}'">
        </div>
        """, unsafe_allow_html=True)
      
        # 菜品信息
        st.markdown(f"""
        <div class="dish-info">
            <h3 class="dish-name">{dish['name']}</h3>
            <p class="dish-desc">{dish['desc']}</p>
            <div class="dish-bottom">
                <span class="price-tag">¥{dish['price']}</span>
            </div>
        """, unsafe_allow_html=True)
      
        # 【核心修复】按钮行 - 使用纯 HTML div 实现
        current_count = st.session_state.cart.get(dish["id"], 0)
        
        st.markdown('<div class="btn-row-container">', unsafe_allow_html=True)
        
        # 使用原生 HTML 来包装按钮，不使用 Streamlit 的列
        if current_count > 0:
            st.markdown('<div class="btn-item">', unsafe_allow_html=True)
            if st.button("➖", key=f"reduce_{dish['id']}", help="减少"):
                reduce_from_cart(dish["id"])
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="btn-item"><div class="count-display"><span class="count-number">{current_count}</span></div></div>', unsafe_allow_html=True)
            
            st.markdown('<div class="btn-item">', unsafe_allow_html=True)
            if st.button("➕", key=f"add_{dish['id']}", help="增加"):
                add_to_cart(dish["id"])
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="btn-item">', unsafe_allow_html=True)
            st.markdown('<div style="visibility: hidden;">➖</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="btn-item"><div class="count-display"></div></div>', unsafe_allow_html=True)
            
            st.markdown('<div class="btn-item">', unsafe_allow_html=True)
            if st.button("➕", key=f"add_{dish['id']}", help="增加"):
                add_to_cart(dish["id"])
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 底部固定购物车栏 ---
total_price, total_count = get_cart_total()

st.markdown('<div class="cart-bar-container">', unsafe_allow_html=True)
cart_left_col, cart_btn_col = st.columns([4, 1])

with cart_left_col:
    if total_count > 0:
        st.markdown(f"""
        <div class="cart-left">
            <div class="cart-icon-wrapper">
                <span class="cart-icon">🛒</span>
                <span class="cart-badge">{total_count}</span>
            </div>
            <div class="cart-total">
                <span class="total-label">合计</span>
                <span class="total-price">¥{total_price}</span>
            </div>
            <span class="total-count">共 {total_count} 件商品</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="cart-left">
            <div class="cart-icon-wrapper">
                <span class="cart-icon">🛒</span>
            </div>
            <div class="cart-total">
                <span class="total-label">购物车为空</span>
                <span class="total-price">¥0.00</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

with cart_btn_col:
    if total_count > 0:
        if st.button("去结算", use_container_width=True):
            submit_order()
    else:
        st.button("去结算", disabled=True, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
