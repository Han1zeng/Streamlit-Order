import streamlit as st
import time

# ====================== 1. 页面全局配置 ======================
st.set_page_config(
    page_title="悦味轩·精致餐厅 - 自助点餐系统",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== 2. 样式优化：修复所有显示/对齐/交互问题 ======================
st.markdown("""
<style>
    /* 【核心修复】强制覆盖Streamlit默认白色背景 */
    .stApp {
        background-color: #fdf6ef !important; /* 暖米色温馨背景，彻底替换纯白 */
    }
    .main, .block-container {
        background-color: #fdf6ef !important;
    }
    /* 全局字体与基础样式 */
    * {
        font-family: "Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", sans-serif;
    }
    .block-container {
        padding-top: 0;
        padding-bottom: 8rem;
        max-width: 1400px;
    }
    
    /* 顶部店铺Header：暖橙渐变温馨风格，修复居中问题 */
    .restaurant-header {
        text-align: center;
        padding: 2.2rem 0;
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
    }
    .restaurant-name {
        font-size: 2.6rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: 3px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.15);
        text-align: center;
        width: 100%;
    }
    .restaurant-slogan {
        font-size: 1rem;
        margin: 0.6rem 0 0 0;
        opacity: 0.95;
        font-weight: 300;
        letter-spacing: 1px;
        text-align: center;
        width: 100%;
    }

    /* 【修复】移动端分类导航：原生按钮样式，修复点击无反应问题 */
    .mobile-category-nav {
        display: none;
        overflow-x: auto;
        gap: 0.8rem;
        padding: 0 1rem 1.5rem;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
        width: 100%;
    }
    .mobile-category-nav::-webkit-scrollbar {
        display: none;
    }
    .mobile-category-nav .stButton>button {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        background: #fff;
        border-radius: 25px;
        border: 1px solid #ff7e42;
        color: #5c3c25;
        font-weight: 600;
        font-size: 0.9rem;
        white-space: nowrap;
        height: fit-content;
        min-height: fit-content;
        width: fit-content;
    }
    .mobile-category-nav .stButton>button:hover {
        transform: scale(1.05);
        border-color: #ff7e42;
        color: #5c3c25;
    }
    .mobile-category-nav .stButton>button:focus:not(:active) {
        border-color: #ff7e42;
        color: #5c3c25;
        box-shadow: none;
    }
    .mobile-category-nav .category-active>button {
        background: linear-gradient(135deg, #ff7e42 0%, #ff6333 100%);
        color: #fff;
        border-color: #ff7e42;
    }
    .mobile-category-nav .category-active>button:hover {
        color: #fff;
    }
    
    /* 分类标题：暖调风格 */
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
    
    /* 菜品卡片：圆角温馨卡片，彻底优化视觉 */
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
    }
    .dish-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }
    .dish-card:hover .dish-img {
        transform: scale(1.1);
    }
    .dish-info {
        padding: 1.3rem;
    }
    .dish-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #3e2723;
        margin: 0 0 0.5rem 0;
    }
    .dish-desc {
        font-size: 0.88rem;
        color: #795548;
        margin: 0 0 1rem 0;
        line-height: 1.5;
    }
    .dish-bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .price-tag {
        color: #d32f2f;
        font-size: 1.45rem;
        font-weight: 800;
    }
    
    /* 【核心修复】增减按钮：完美居中、尺寸协调、符号不偏移 */
    button[key^="reduce_"], button[key^="add_"] {
        width: 40px !important;
        height: 40px !important;
        min-width: 40px !important;
        min-height: 40px !important;
        max-width: 40px !important;
        max-height: 40px !important;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
        margin: 0 auto !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        line-height: 1 !important;
        text-align: center !important;
    }
    /* 减号按钮样式 */
    button[key^="reduce_"] {
        background: linear-gradient(135deg, #fff0e6 0%, #ffe0cc 100%);
        color: #5c3c25;
        border: 1px solid #ffccb3;
    }
    button[key^="reduce_"]:hover {
        background: linear-gradient(135deg, #ffe0cc 0%, #ffccb3 100%);
        transform: scale(1.1);
        color: #5c3c25;
        border: 1px solid #ffccb3;
    }
    /* 加号按钮样式 */
    button[key^="add_"] {
        background: linear-gradient(135deg, #ff7e42 0%, #ff6333 100%);
        color: white;
        box-shadow: 0 3px 10px rgba(255, 126, 66, 0.3);
        border: none;
    }
    button[key^="add_"]:hover {
        background: linear-gradient(135deg, #ff6333 0%, #ff451a 100%);
        transform: scale(1.1);
        color: white;
        border: none;
    }
    button[key^="reduce_"]:focus:not(:active), button[key^="add_"]:focus:not(:active) {
        box-shadow: none;
        border: none;
    }

    /* 【核心修复】菜品数量：圆形外框、固定在按钮中间、完美居中 */
    .count-circle {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #fff0e6;
        border: 1px solid #ffccb3;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.15rem;
        font-weight: 700;
        color: #3e2723;
        margin: 0 auto;
        line-height: 1;
    }
    
    /* 底部固定购物车栏：暖橙风格，响应式适配 */
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
        white-space: nowrap; /* 修复电脑端文字显示不全 */
        min-width: fit-content;
    }
    /* 底部结算按钮原生样式适配 */
    .stButton>button {
        background: linear-gradient(135deg, #ff7e42 0%, #ff6333 100%);
        color: white;
        border: none;
        padding: 1.1rem 3.3rem;
        border-radius: 50px;
        font-size: 1.15rem;
        font-weight: 800;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 18px rgba(255, 126, 66, 0.35);
        letter-spacing: 1px;
        height: fit-content;
    }
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.04);
        box-shadow: 0 9px 26px rgba(255, 126, 66, 0.45);
        background: linear-gradient(135deg, #ff6333 0%, #ff451a 100%);
        color: white;
        border: none;
    }
    .stButton>button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
        transform: none;
    }
    
    /* 【核心修复】侧边栏字体放大：解决分类、购物车、合计字体偏小问题 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff5ee 0%, #ffe8d6 100%);
        box-shadow: 4px 0 18px rgba(92, 60, 37, 0.08);
    }
    [data-testid="stSidebar"] h2 {
        color: #5c3c25;
        font-weight: 700;
        font-size: 1.4rem !important;
        margin-bottom: 0.5rem;
    }
    [data-testid="stSidebar"] .stRadio label {
        font-size: 1.1rem !important;
        font-weight: 500;
        color: #5c3c25;
        padding: 0.3rem 0;
    }
    [data-testid="stSidebar"] .stText p {
        font-size: 1rem !important;
        color: #5c3c25;
        font-weight: 500;
    }
    [data-testid="stSidebar"] h3 {
        font-size: 1.35rem !important;
        color: #5c3c25;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    [data-testid="stSidebar"] .stHorizontalBlock {
        align-items: center;
    }
    
    /* 隐藏Streamlit默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    /* 隐藏按钮默认的点击聚焦边框 */
    button:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    /* ====================== 响应式媒体查询：手机端适配核心 ====================== */
    @media only screen and (max-width: 768px) {
        /* 显示移动端分类导航 */
        .mobile-category-nav {
            display: flex !important;
        }
        /* 【修复】Header文字居中，调整字号避免挤压 */
        .restaurant-header {
            padding: 1.2rem 0.5rem;
            margin-bottom: 0.5rem;
        }
        .restaurant-name {
            font-size: 1.8rem;
            letter-spacing: 1px;
            text-align: center;
        }
        .restaurant-slogan {
            font-size: 0.8rem;
            text-align: center;
            word-break: keep-all;
        }
        /* 分类标题适配 */
        .category-title {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            padding: 0.5rem 1rem;
        }
        /* 菜品卡片列数：手机端2列 */
        [data-testid="column"] {
            flex: 1 1 45% !important;
            max-width: 45% !important;
        }
        .dish-img-container {
            height: 140px;
        }
        .dish-info {
            padding: 1rem;
        }
        .dish-name {
            font-size: 1rem;
        }
        .dish-desc {
            font-size: 0.75rem;
        }
        .price-tag {
            font-size: 1.1rem;
        }
        /* 【修复】手机端增减按钮与数量同行、居中、尺寸适配 */
        button[key^="reduce_"], button[key^="add_"] {
            width: 36px !important;
            height: 36px !important;
            min-width: 36px !important;
            min-height: 36px !important;
            max-width: 36px !important;
            max-height: 36px !important;
            font-size: 1.1rem !important;
        }
        .count-circle {
            width: 36px;
            height: 36px;
            font-size: 1rem;
        }
        /* 底部结算栏适配：减小占比 */
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
        .total-label {
            font-size: 0.75rem;
        }
        .total-count {
            font-size: 0.75rem;
            padding: 0.35rem 0.8rem;
        }
        .stButton>button {
            padding: 0.8rem 1.5rem;
            font-size: 1rem;
        }
        /* 调整页面底部padding */
        .block-container {
            padding-bottom: 7rem;
        }
    }

    /* ====================== 平板端适配 ====================== */
    @media only screen and (min-width: 768px) and (max-width: 1024px) {
        /* 菜品卡片列数：平板端3列 */
        [data-testid="column"] {
            flex: 1 1 30% !important;
            max-width: 30% !important;
        }
        .cart-bar-container {
            padding: 1rem 2rem;
        }
        .stButton>button {
            padding: 1rem 2.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ====================== 3. 餐厅与菜品数据（完全保留原数据，无修改） ======================
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
    {"id": 404, "category_id": 4, "name": "牛肉汉堡", "price": 3, "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=400&h=300&fit=crop", "desc": "外焦里嫩，大口满足"},
    
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
    """统一的下单逻辑，侧边栏和底部按钮共用"""
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

# --- 【修复】移动端顶部分类导航：原生按钮，彻底解决点击无反应问题 ---
category_names = [c["name"] for c in CATEGORIES]
st.markdown('<div class="mobile-category-nav">', unsafe_allow_html=True)
mobile_cat_cols = st.columns(len(CATEGORIES))
for idx, cat in enumerate(CATEGORIES):
    with mobile_cat_cols[idx]:
        is_active = cat["name"] == st.session_state.selected_category
        if st.button(
            cat["name"],
            key=f"mobile_cat_{cat['id']}",
            use_container_width=True,
            type="secondary"
        ):
            st.session_state.selected_category = cat["name"]
            st.rerun()
        # 【核心修复】给激活的按钮添加样式类，修正字符串拼接与CSS大括号转义
        if is_active:
            st.markdown(
                f'<style>.element-container:has(#mobile_cat_{cat["id"]}) .stButton {{ class: category-active; }}</style>',
                unsafe_allow_html=True
            )
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
    # 同步侧边栏选择到session_state
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
        
        # 下单按钮
        if st.button("✅ 确认下单", type="primary", use_container_width=True):
            submit_order()
        
        # 清空购物车按钮
        if st.button("🗑️ 清空购物车", use_container_width=True):
            clear_cart()
            st.rerun()
    else:
        st.info("购物车是空的，快去挑选美食吧~")

# --- 主内容区：菜品列表 ---
current_category = next(c for c in CATEGORIES if c["name"] == selected_category_name)
current_dishes = [d for d in DISHES if d["category_id"] == current_category["id"]]

# 分类标题
st.markdown(f'<h2 class="category-title">{current_category["name"]}</h2>', unsafe_allow_html=True)

# 【修复】菜品列布局，4列适配，调整按钮列比例保证数量居中
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
        </div>
        """, unsafe_allow_html=True)
        
        # 【核心修复】数量控制布局：调整列比例，数量固定在中间，圆形外框
        current_count = st.session_state.cart.get(dish["id"], 0)
        # 调整列比例，让减号、数量、加号均匀分布在右侧
        btn_cols = st.columns([4, 1, 1, 1])
        with btn_cols[1]:
            if current_count > 0:
                st.button("➖", key=f"reduce_{dish['id']}")
        with btn_cols[2]:
            if current_count > 0:
                st.markdown(f'<div class="count-circle">{current_count}</div>', unsafe_allow_html=True)
        with btn_cols[3]:
            st.button("➕", key=f"add_{dish['id']}")
        
        # 按钮点击事件处理
        if st.session_state.get(f"add_{dish['id']}"):
            add_to_cart(dish["id"])
            st.rerun()
        if st.session_state.get(f"reduce_{dish['id']}"):
            reduce_from_cart(dish["id"])
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# --- 底部固定购物车栏 ---
total_price, total_count = get_cart_total()

st.markdown('<div class="cart-bar-container">', unsafe_allow_html=True)
cart_left_col, cart_btn_col = st.columns([4, 1])

# 左侧购物车信息
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

# 右侧去结算按钮
with cart_btn_col:
    if total_count > 0:
        if st.button("去结算", use_container_width=True):
            submit_order()
    else:
        st.button("去结算", disabled=True, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
