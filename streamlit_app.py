import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template
import sqlite3

a = st.sidebar.radio('Choose:',[1,2])
conn = sqlite3.connect('poems.db')

def main():
    app_title = "My Streamlit App"

    if a == 1:
        st.markdown('hello')
    else :
        # Your dynamic data — replace this with the select query from poems database
        # change with database later
        # items = ["Item 1", "Item 2", "Item 3"]
        cursor = conn.cursor()
        cursor.execute('select * from poems')
        items = cursor.fetchall()

            # Load the Jinja2 template
        with open("templates/template2.html", "r") as template_file:
                template_content = template_file.read()
                jinja_template = Template(template_content)

        # Render the template with dynamic data
        rendered_html = jinja_template.render(title= app_title, items=items)
        print(rendered_html)

            # Display the HTML in Streamlit app
        components.html(rendered_html, height=1000, scrolling=True)

if __name__ == '__main__':
    main()
