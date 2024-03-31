import pymysql
import streamlit as st
# from generator import test

# Connecting to mySQL database
db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='', # input your mysql password here,
    db='ecom', # input WRPL ecommerce database name here,
    charset='utf8'
)


cursor = db.cursor()
print('connected to database')

# Fetching data from database
product_highlight = 'SELECT * FROM products LIMIT 10'
cursor.execute(product_highlight)
prod = cursor.fetchall()

store_highlight = 'SELECT * FROM stores LIMIT 10'
cursor.execute(store_highlight)
stores = cursor.fetchall()

def search_product(product_name):
    search_query = f"SELECT * FROM products WHERE ProductName LIKE '%{product_name}%'"
    cursor.execute(search_query)
    results = cursor.fetchall()
    return results

def search_store(store_name):
    search_query = f"SELECT * FROM stores WHERE StoreName LIKE '%{store_name}%'"
    cursor.execute(search_query)
    results = cursor.fetchall()
    return results

# Streamlit App
def main(): 
    st.title('UNIQLY, your indispensable partner.')
    
    option = st.sidebar.selectbox('Pages', ("Main Page", "Stores", "Profile"))
    
    if option == 'Main Page': 
        # st.subheader('*Explore the best, tailored for you.*')
        st.write('*Explore the best, tailored for you.*')
        search_input = st.text_input('Looking for a product?')
        if search_input:
            results = search_product(search_input)
            if results: 
                st.write('Search Results for Products: ')
                for product in results:
                    st.write(f"### *{product[2]}*")
                    st.write(f"Description:")
                    st.write(f"{product[4]}")
                    st.write(f"Category: {product[3]}")
                    st.write(f"Price: ${product[5]}")
                    st.write(f"Stock: {product[6]}")
                    st.write("---")
            else: st.write('Product not found.')
        else :
            for product in prod:
                # st.image(product['product_image'], caption=product['product_name'], width=200)
                st.write(f"### *{product[2]}*")
                st.write(f"Description:")
                st.write(f"{product[4]}")
                st.write(f"Category: {product[3]}")
                st.write(f"Price: ${product[5]}")
                st.write(f"Stock: {product[6]}")
                st.write("---")
        
    elif option == 'Stores':
        st.write('*Check out our stores*')
        search_input = st.text_input('Maybe another store?')
        if search_input:
            results = search_store(search_input)
            if results: 
                st.write('Search results for Stores: ')
                for store in results:
                    st.write(f"### *{store[1]}*")
                    st.write(f"Location: {store[3]}")
                    st.write(f"Contact us: {store[5]}")
                    st.write("---")
            else: st.write('Store not found.')
       
        for store in stores:
            st.write(f"### *{store[1]}*")
            st.write(f"Location: {store[3]}")
            st.write(f"Contact us: {store[5]}")
            st.write("---")
        
    elif option == 'Profile':
        st.subheader('hello, John Smith!')
    
if __name__ == '__main__':
    main()


cursor.close()
db.close()
print('connecton closed.')