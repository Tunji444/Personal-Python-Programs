from ddgs import DDGS
from tkinter import *

#actual code
# Define your search query and number of results to retrieve.
num_results = 10

def search():
    content.grid(row=4, column=0, columnspan=2)
    query = user_input.get()
    with DDGS() as ddgs:
        results = list(ddgs.text(query, region="uk-en", safesearch="moderate", max_results=num_results))

    # Output the results.
    result_text = ""
    for doc in results:
        result_text += f"Title: {doc.get('title', '')}\nContent: {doc.get('body', '')}\n------------\n"
    content.config(text=result_text)
      




#gui
window = Tk()
window.title("Alpha.ai")
window.minsize(700,700)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Alpha_logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, rowspan=2)

#Labels
John_label = Label(text="powered by John's Brain", font=("Consolas", 12, "bold italic"))
John_label.grid(row=0, column=0)
content = Label(text="")
content.grid_forget()
#Entries
user_input = Entry(width=35)
user_input.grid(row=1, column=0, columnspan=2)
user_input.focus()
user_input.insert(0, "What can I search for you today?") #pre-populating the e-mail box


# Buttons
search_button = Button(text="Search", command=search)
search_button.grid(row=3, column=0, columnspan=5)

window.mainloop()
