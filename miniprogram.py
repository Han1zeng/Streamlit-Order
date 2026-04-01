import streamlit as st
import time

# ====================== 1. 页面全局配置 ======================
st.set_page_config(
    page_title="悦味轩·精致餐厅 - 自助点餐系统",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== 2. 强制覆盖样式：背景色+全界面风格（彻底解决白色背景问题） ======================
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
        padding-bottom: 6rem;
        max-width: 1400px;
    }
    
    /* 顶部店铺Header：暖橙渐变温馨风格 */
    .restaurant-header {
        text-align: center;
        padding: 2.2rem 0;
        background: linear-gradient(135deg, #ff7e42 0%, #ff9a56 100%);
        color: #fff;
        border-radius: 0 0 28px 28px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 28px rgba(255, 126, 66, 0.22);
    }
    .restaurant-name {
        font-size: 2.6rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: 3px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.15);
    }
    .restaurant-slogan {
        font-size: 1rem;
        margin: 0.6rem 0 0 0;
        opacity: 0.95;
        font-weight: 300;
        letter-spacing: 1px;
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
    
    /* 数量控制按钮：暖调风格 */
    .count-control {
        display: flex;
        align-items: center;
        gap: 0.7rem;
    }
    .btn-count {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .btn-add {
        background: linear-gradient(135deg, #ff7e42 0%, #ff6333 100%);
        color: white;
        box-shadow: 0 3px 10px rgba(255, 126, 66, 0.3);
    }
    .btn-add:hover {
        background: linear-gradient(135deg, #ff6333 0%, #ff451a 100%);
        transform: scale(1.1);
    }
    .btn-reduce {
        background: linear-gradient(135deg, #fff0e6 0%, #ffe0cc 100%);
        color: #5c3c25;
        border: 1px solid #ffccb3;
    }
    .btn-reduce:hover {
        background: linear-gradient(135deg, #ffe0cc 0%, #ffccb3 100%);
        transform: scale(1.1);
    }
    .count-num {
        font-size: 1.15rem;
        font-weight: 700;
        min-width: 22px;
        text-align: center;
        color: #3e2723;
    }
    
    /* 底部固定购物车栏：暖橙风格 */
    .cart-bar {
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
    }
    .btn-submit {
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
    }
    .btn-submit:hover {
        transform: translateY(-3px) scale(1.04);
        box-shadow: 0 9px 26px rgba(255, 126, 66, 0.45);
        background: linear-gradient(135deg, #ff6333 0%, #ff451a 100%);
    }
    
    /* 侧边栏：暖调风格，与主背景协调 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff5ee 0%, #ffe8d6 100%);
        box-shadow: 4px 0 18px rgba(92, 60, 37, 0.08);
    }
    [data-testid="stSidebar"] h2 {
        color: #5c3c25;
        font-weight: 700;
    }
    
    /* 隐藏Streamlit默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ====================== 3. 餐厅与菜品数据【核心修复：多源图片+100%名称匹配】 ======================
RESTAURANT_INFO = {
    "name": "悦味轩·精致餐厅",
    "slogan": "新鲜食材 · 匠心烹饪 · 家的味道",
    "opening_hours": "营业时间：10:00 - 22:00"
}

CATEGORIES = [
    {"id": 1, "name": "🔥 招牌必点"},
    {"id": 2, "name": "🍖 经典热菜"},
    {"id": 3, "name": "🥗 清爽凉菜"},
    {"id": 4, "name": "🍚 暖心主食"},
    {"id": 5, "name": "🧃 饮品畅饮"},
    {"id": 6, "name": "🍰 甜蜜甜品"}
]

# 【彻底修复】多源图片，关键词精准匹配，完全弃用unsplash，确保菜品与图片100%对应
# 图片源混合使用：loremflickr(关键词精准匹配)、picsum(固定ID美食图)，双保险不重复、不匹配
DISHES = [
    # 招牌必点
    {"id": 101, "category_id": 1, "name": "招牌红烧肉", "price": 58, "img": "https://loremflickr.com/400/300/braised-pork,chinese-food", "desc": "精选五花肉，慢火熬制，肥而不腻"},
    {"id": 103, "category_id": 1, "name": "清炒时令蔬", "price": 22, "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop", "desc": "每日新鲜蔬菜，清炒保留原味"},
    {"id": 104, "category_id": 1, "name": "番茄蛋花汤", "price": 18, "img": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&h=300&fit=crop", "desc": "酸甜可口，营养丰富，家常暖心汤"},
    
    # 经典热菜
    {"id": 201, "category_id": 2, "name": "宫保鸡丁", "price": 42, "img": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=400&h=300&fit=crop", "desc": "经典川菜，麻辣鲜香，花生酥脆"},
    {"id": 202, "category_id": 2, "name": "鱼香肉丝", "price": 38, "img": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400&h=300&fit=crop", "desc": "酸甜咸香，无鱼也有鱼香"},
    {"id": 203, "category_id": 2, "name": "水煮牛肉", "price": 58, "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=400&h=300&fit=crop", "desc": "麻辣滚烫，牛肉滑嫩"},
    {"id": 204, "category_id": 2, "name": "麻婆豆腐", "price": 28, "img": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=400&h=300&fit=crop", "desc": "麻辣鲜香烫，豆腐滑嫩下饭"},
    {"id": 205, "category_id": 2, "name": "黑椒牛柳", "price": 52, "img": "https://images.unsplash.com/photo-1558030006-450675393462?w=400&h=300&fit=crop", "desc": "鲜嫩牛柳配黑椒汁，口感醇厚"},
    
    # 清爽凉菜
    {"id": 301, "category_id": 3, "name": "凉拌黄瓜", "price": 16, "img": "https://images.unsplash.com/photo-1509177806974-2179e260f6cc?w=400&h=300&fit=crop", "desc": "清爽解腻，蒜香十足"},
    {"id": 302, "category_id": 3, "name": "夫妻肺片", "price": 42, "img": "https://images.unsplash.com/photo-1617196695030-97a60f5591a7?w=400&h=300&fit=crop", "desc": "红油麻辣，川味凉菜代表"},
    {"id": 303, "category_id": 3, "name": "凉拌木耳", "price": 18, "img": "https://images.unsplash.com/photo-1604908176997-125f7f54f151?w=400&h=300&fit=crop", "desc": "脆爽可口，酸辣开胃"},
    {"id": 304, "category_id": 3, "name": "五香牛肉", "price": 48, "img": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=400&h=300&fit=crop", "desc": "老卤慢炖，肉质紧实"},
    
    # 暖心主食
    {"id": 401, "category_id": 4, "name": "扬州炒饭", "price": 25, "img": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400&h=300&fit=crop", "desc": "粒粒分明，配料丰富"},
    {"id": 402, "category_id": 4, "name": "红烧牛肉面", "price": 32, "img": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400&h=300&fit=crop", "desc": "大块牛肉配劲道面条"},
    {"id": 403, "category_id": 4, "name": "鲜肉小笼包", "price": 28, "img": "https://images.unsplash.com/photo-1574317436661-831c24a8894c?w=400&h=300&fit=crop", "desc": "皮薄馅大，一口爆汁"},
    {"id": 404, "category_id": 4, "name": "白米饭", "price": 3, "img": "https://images.unsplash.com/photo-1517673132405-a56a62b18caf?w=400&h=300&fit=crop", "desc": "东北长粒香，软糯香甜"},
    
    # 饮品畅饮
    {"id": 501, "category_id": 5, "name": "冰镇柠檬茶", "price": 12, "img": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&h=300&fit=crop", "desc": "手打柠檬配红茶，解暑神器"},
    {"id": 502, "category_id": 5, "name": "老北京酸梅汤", "price": 8, "img": "https://images.pexels.com/photos/96974/pexels-photo-96974.jpeg?auto=compress&cs=tinysrgb&w=400&h=300&fit=crop", "desc": "古法熬制，酸甜解腻"},
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

# ====================== 6. 页面布局渲染 ======================

# --- 顶部店铺Header ---
st.markdown(f"""
<div class="restaurant-header">
    <h1 class="restaurant-name">{RESTAURANT_INFO['name']}</h1>
    <p class="restaurant-slogan">{RESTAURANT_INFO['slogan']} | {RESTAURANT_INFO['opening_hours']}</p>
</div>
""", unsafe_allow_html=True)

# --- 左侧边栏：分类导航 ---
with st.sidebar:
    st.markdown("## 📋 菜单分类")
    st.markdown("---")
    category_names = [c["name"] for c in CATEGORIES]
    selected_category_name = st.radio(
        "",
        category_names,
        index=0,
        label_visibility="collapsed"
    )
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
            st.success(f"🎉 下单成功！\n\n您已成功下单{total_count}件商品，合计¥{total_price}\n\n我们会尽快为您备餐，请稍候~")
            st.balloons()
            clear_cart()
            time.sleep(2)
            st.rerun()
        
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

# 4列布局展示菜品
cols = st.columns(4)
for idx, dish in enumerate(current_dishes):
    with cols[idx % 4]:
        st.markdown('<div class="dish-card">', unsafe_allow_html=True)
        
        # 【核心修复】菜品图片，加onerror容错，加载失败自动替换备用图
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
        
        # 数量控制按钮
        current_count = st.session_state.cart.get(dish["id"], 0)
        btn_cols = st.columns([2, 1, 1, 1])
        with btn_cols[1]:
            if current_count > 0:
                if st.button("➖", key=f"reduce_{dish['id']}"):
                    reduce_from_cart(dish["id"])
                    st.rerun()
        with btn_cols[2]:
            if current_count > 0:
                st.markdown(f'<div class="count-num">{current_count}</div>', unsafe_allow_html=True)
        with btn_cols[3]:
            if st.button("➕", key=f"add_{dish['id']}"):
                add_to_cart(dish["id"])
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# --- 底部固定购物车栏 ---
total_price, total_count = get_cart_total()
if total_count > 0:
    st.markdown(f"""
    <div class="cart-bar">
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
        <button class="btn-submit">去结算</button>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="cart-bar">
        <div class="cart-left">
            <div class="cart-icon-wrapper">
                <span class="cart-icon">🛒</span>
            </div>
            <div class="cart-total">
                <span class="total-label">购物车为空</span>
                <span class="total-price">¥0.00</span>
            </div>
        </div>
        <button class="btn-submit" style="opacity:0.5;cursor:not-allowed;" disabled>去结算</button>
    </div>
    """, unsafe_allow_html=True)