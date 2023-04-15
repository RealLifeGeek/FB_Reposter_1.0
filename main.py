from requests_html import HTMLSession
from bs4 import BeautifulSoup
from unidecode import unidecode
import facebook
import time
import tkinter as tktr
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from tkinter.ttk import *
from tkinter import *
import webbrowser

RELEVANT_ARTICLES = []
NOT_PUBLISHED_ARTICLES = []
PUBLISHED_ARTICLES = []
RESULT_ARTICLES = []
FINAL_ARTICLE = []
SAVED_ARTICLES = []
RELEVANT_URL = []
RESULT_URL = []
FINAL_URL = []
NOT_PUBLISHED_URL = []
PUBLISHED_URL = []
SAVED_URL = []

home_news = "https://www.seznamzpravy.cz/sekce/domaci-13"
world_news = "https://www.seznamzpravy.cz/sekce/zahranicni-11"

def search_articles():
    if len(RELEVANT_ARTICLES) > 0:
        transform_relevant_to_result()
        #messagebox.showerror('Error', 'Articles already searched.')
    else:
        filter_articles()

def filter_articles():
    RELEVANT_KEYWORD = unidecode(keyword_field.get()).lower()
    global RELEVANT_ARTICLES
    global RELEVANT_URL

    try:
        the_value = URL_listbox.get(URL_listbox.curselection())
        session = HTMLSession()
        resp = session.get(the_value)
        resp.html.html
        soup = BeautifulSoup(resp.html.html, "html.parser")
    except:
        messagebox.showerror('Error', 'OOPS! URL not selected. Cannot start filtering.')

    results1 = soup.find_all(
    "div", class_="c_iJ"
    )

    results2 = soup.find_all(
        "div", class_="d_f g_f"
    )
    if len(RELEVANT_KEYWORD) == 0:
        messagebox.showerror('Error', 'OOPS! No keyword inserted.')
    else:
        for add_element1 in results1:
            try:
                links = add_element1.find_all("a")
                for link in links:
                    try:
                        link_url = link["href"]
                        title1_element = add_element1.find("h3")
                        if RELEVANT_KEYWORD in link_url:
                            RELEVANT_ARTICLES += [f"\n{title1_element.text.strip()}\n{link_url}\n"]
                            RELEVANT_URL += [link_url]
                        else:
                            pass
                    except:
                        pass
            except:
                pass
        
        for add_element2 in results2:
            try:
                links = add_element2.find_all("a")
                for link in links:
                    try:
                        link_url = link["href"]
                        title2_element = add_element2.find("h3")
                        if RELEVANT_KEYWORD in link_url:
                            RELEVANT_ARTICLES += [f"\n{title2_element.text.strip()}\n{link_url}\n"]
                            RELEVANT_URL += [link_url]
                        else:
                            pass
                    except:
                         pass
            except:
                 pass
        count_result_articles()
        transform_relevant_to_result()
        transform_relevant_URL_to_result()

def count_result_articles():
    number_of_relevant = str(len(RESULT_ARTICLES)) + "    "

    number_of_result_label = ttk.Label(
        tk,  
        text = number_of_relevant,  
        font = ("Times New Roman", "13", "bold"),  
        background = "#336699",  
        foreground = "#FFFFFF"  
    )
    number_of_result_label.place(x = 150, y = 320)

def transform_relevant_to_result():
    global RELEVANT_ARTICLES
    global NOT_PUBLISHED_ARTICLES
    global PUBLISHED_ARTICLES
    global RESULT_ARTICLES
    global SAVED_ARTICLES

    if len(RELEVANT_ARTICLES) > 0:
        RESULT_ARTICLES [:] = []
        for article in RELEVANT_ARTICLES:
            if article in NOT_PUBLISHED_ARTICLES:
                RELEVANT_ARTICLES.remove(article)
            elif article in SAVED_ARTICLES:
                RELEVANT_ARTICLES.remove(article)
            elif article in PUBLISHED_ARTICLES:
                RELEVANT_ARTICLES.remove(article)
            else:
                RESULT_ARTICLES += [article]
    else:
        new_article_label = ttk.Label(
            tk,
            width = 125,
            text = "No available articles ... \n  \n  ",
            font = ("Times New Roman", "10"),
        )
        new_article_label.place(x = 30, y = 350)
    count_result_articles()
    show_final_arcticle()

def transform_relevant_URL_to_result():
    global RESULT_URL
    global RELEVANT_URL
    global NOT_PUBLISHED_URL
    global PUBLISHED_URL

    RESULT_URL [:] = []
    for link_url in RELEVANT_URL:
        if link_url in NOT_PUBLISHED_URL:
            RELEVANT_URL.remove(link_url)
        elif link_url in SAVED_URL:
            RELEVANT_URL.remove(link_url)
        elif link_url in PUBLISHED_URL:
            RELEVANT_URL.remove(link_url)
        else:
            RESULT_URL += [link_url]
    show_final_URL()

def transform_saved_to_result():
    global SAVED_ARTICLES
    global RESULT_ARTICLES

    if len(SAVED_ARTICLES) > 0:
        RESULT_ARTICLES [:] = []
        for article in SAVED_ARTICLES:
                RESULT_ARTICLES += [article]
    else:
        new_article_label = ttk.Label(
            tk,
            width = 125,
            text = "No saved articles ... \n  \n  ",
            font = ("Times New Roman", "10"),
        )
        new_article_label.place(x = 30, y = 350)
    count_result_articles()
    show_final_arcticle()
    transform_saved_URL_to_result()

def transform_saved_URL_to_result():
    global SAVED_URL
    global RESULT_URL

    RESULT_URL[:] = []
    for link_url in SAVED_URL:
        RESULT_URL += [link_url]
    show_final_URL()

def transform_not_published_to_result():
    global NOT_PUBLISHED_ARTICLES
    global RESULT_ARTICLES

    if len(NOT_PUBLISHED_ARTICLES) > 0:
        RESULT_ARTICLES [:] = []
        for article in NOT_PUBLISHED_ARTICLES:
                RESULT_ARTICLES += [article]
    else:
        new_article_label = ttk.Label(
            tk,
            width = 125,
            text = "No articles in Not Published Arcticles ... \n  \n  ",
            font = ("Times New Roman", "10"),
        )
        new_article_label.place(x = 30, y = 350)
    count_result_articles()
    show_final_arcticle()
    transform_not_published_URL_to_result()

def transform_not_published_URL_to_result():
    global NOT_PUBLISHED_URL
    global RESULT_URL

    RESULT_URL[:] = []
    for link_url in NOT_PUBLISHED_URL:
        RESULT_URL += [link_url]
    show_final_URL()

def transform_published_to_result():
    global PUBLISHED_ARTICLES
    global RESULT_ARTICLES

    RESULT_ARTICLES [:] = []
    if len(PUBLISHED_ARTICLES) > 0:
        for article in PUBLISHED_ARTICLES:
                RESULT_ARTICLES += [article]
    else:
        new_article_label = ttk.Label(
            tk,
            width = 125,
            text = "No articles in Published Arcticles ... \n  \n  ",
            font = ("Times New Roman", "10"),
        )
        new_article_label.place(x = 30, y = 350)
    count_result_articles()
    show_final_arcticle()
    transform_published_URL_to_result()

def transform_published_URL_to_result():
    global PUBLISHED_URL
    global RESULT_URL

    RESULT_URL[:] = []
    for link_url in PUBLISHED_URL:
        RESULT_URL += [link_url]
    show_final_URL()

def show_final_URL():
    global RESULT_URL
    global FINAL_URL

    for final_url in RESULT_URL:
        FINAL_URL += [final_url]
        RESULT_URL.remove(final_url)
        break

def show_final_arcticle():
    global RESULT_ARTICLES
    global FINAL_ARTICLE

    for final_article in RESULT_ARTICLES:
        FINAL_ARTICLE += [final_article]
        final_article_label = ttk.Label(
                tk,
                width = 125,
                text = final_article,
                font = ("Times New Roman", "10"),
        )
        final_article_label.place(x = 30, y = 350)
        RESULT_ARTICLES.remove(final_article)
        break

def publish_article():
    global FINAL_ARTICLE
    global PUBLISHED_ARTICLES
    
    if len(FINAL_ARTICLE) > 0:
        for final_article in FINAL_ARTICLE:
            if final_article not in PUBLISHED_ARTICLES:
                publish_window()
            else:
                messagebox.showinfo('Info', 'Article already published.')
                show_final_arcticle()
                show_final_URL()
                break
    else:
        messagebox.showerror('Error', 'No available article...') 

def publish_on_fb():
    global PUBLISHED_ARTICLES
    global NOT_PUBLISHED_ARTICLES
    global SAVED_ARTICLES
    global FINAL_ARTICLE
    global PUBLISHED_URL
    global NOT_PUBLISHED_ARTICLES
    global SAVED_ARTICLES
    
    if len(FINAL_ARTICLE) > 0:
        for final_article in FINAL_ARTICLE:
            if final_article in NOT_PUBLISHED_ARTICLES:
                try:
                    fb = facebook.GraphAPI(access_token_field.get())
                    fb.put_object(
                        subject_id_field.get(), "feed", message = post_field.get() + "\n" + final_article
                    )
                    messagebox.showinfo('Info', 'Successfully published.')
                    PUBLISHED_ARTICLES += [final_article]
                    NOT_PUBLISHED_ARTICLES.remove(final_article)
                    FINAL_ARTICLE[:] = []
                    show_final_arcticle()
                    publish_URL
                    break
                except:
                    messagebox.showerror('Error', 'OOPS! Something went wrong.\nYour token probably expired.')
                    break
            elif final_article in SAVED_ARTICLES:
                try:
                    fb = facebook.GraphAPI(access_token_field.get())
                    fb.put_object(
                        subject_id_field.get(), "feed", message = post_field.get() + "\n" + final_article
                    )
                    messagebox.showinfo('Info', 'Successfully published.')
                    PUBLISHED_ARTICLES += [final_article]
                    SAVED_ARTICLES.remove(final_article)
                    FINAL_ARTICLE[:] = []
                    show_final_arcticle()
                    publish_URL
                    break
                except:
                    messagebox.showerror('Error', 'OOPS! Something went wrong.\nYour token probably expired.')
                    break
            else:
                try:
                    fb = facebook.GraphAPI(access_token_field.get())
                    fb.put_object(
                    subject_id_field.get(), "feed", message = post_field.get() + "\n" + final_article
                    )
                    messagebox.showinfo('Info', 'Successfully published.')
                    PUBLISHED_ARTICLES += [final_article]
                    FINAL_ARTICLE[:] = []
                    show_final_arcticle()
                    publish_URL
                    break
                except:
                    messagebox.showerror('Error', 'OOPS! Something went wrong.\nYour token probably expired.')
                    break
    else:
        messagebox.showerror('Error', 'No available article...\nYou probably stopped searching.')      

def publish_URL():
    global PUBLISHED_URL
    global FINAL_URL

    for final_url in FINAL_URL:
        if final_url in NOT_PUBLISHED_URL:
            PUBLISHED_URL += [final_url]
            NOT_PUBLISHED_ARTICLES.remove(final_url)
            FINAL_URL[:] = []
            show_final_URL()
        elif final_url in SAVED_URL:
            PUBLISHED_URL += [final_url]
            SAVED_ARTICLES.remove(final_url)
            FINAL_URL[:] = []
            show_final_URL()
        else:
            PUBLISHED_URL += [final_url]
            FINAL_ARTICLE[:] = []
            show_final_URL()

def publish_window():
    global FINAL_ARTICLE

    publish_win = tktr.Tk()
    publish_win.geometry ("800x350")
    publish_win.title("Scraper_Reposter 1.0: PUBLISH ARCTICLE")
    publish_win.resizable(0,0)
    publish_win.configure(bg = "#336699")

    for final_article in FINAL_ARTICLE:
        publish_article_label = ttk.Label(
            publish_win,
            width = 125,
            text = post_field.get() + "\n" + final_article,
            font = ("Times New Roman", "10"),
        )
        publish_article_label.place(x = 30, y = 180)

    publish_header_label = ttk.Label(  
        publish_win,  
        text = "PUBLISH ARTICLE ON FB",  
        font = ("Times New Roman", "15"),  
        background = "#336699",  
        foreground = "#FFFFFF" 
    )
    publish_header_label.place(x = 260, y = 20)

    publish_button = ttk.Button(  
        publish_win,  
        text = "PUBLISH",  
        width = 24,  
        command = publish_on_fb  
    )
    publish_button.place(x = 230, y = 280)

    see_arcticle_button = ttk.Button(  
        publish_win,  
        text = "See Article",  
        width = 24,  
        command = see_article  
    )
    see_arcticle_button.place(x = 400, y = 280)

def do_not_publish_article():
    global PUBLISHED_ARTICLES
    global NOT_PUBLISHED_ARTICLES
    global SAVED_ARTICLES
    global FINAL_ARTICLE

    if len(FINAL_ARTICLE) > 0:
        do_not_publish_URL()
        for final_article in FINAL_ARTICLE:
            if final_article in SAVED_ARTICLES:
                SAVED_ARTICLES.remove(final_article)
                NOT_PUBLISHED_ARTICLES += [final_article]
                messagebox.showinfo('Info', 'Article removed from saved articles.')
            elif final_article in PUBLISHED_ARTICLES:
                messagebox.showinfo('Info', 'Article already published.')
            elif final_article in NOT_PUBLISHED_ARTICLES:
                messagebox.showinfo('Info', 'Article was already moved to Not Published Articles.')
            else:
                NOT_PUBLISHED_ARTICLES += [final_article]
                FINAL_ARTICLE.remove(final_article)
    else:
        messagebox.showerror('Error', 'No available article...')
    show_final_arcticle()

def do_not_publish_URL():
    global PUBLISHED_URL
    global NOT_PUBLISHED_URL
    global SAVED_URL
    global FINAL_URL

    for final_url in FINAL_URL:
        if final_url in SAVED_URL:
            SAVED_URL.remove(final_url)
            NOT_PUBLISHED_URL += [final_url]
        elif final_url in PUBLISHED_URL:
            pass
        elif final_url in NOT_PUBLISHED_URL:
            pass
        else:
            NOT_PUBLISHED_URL += [final_url]
            FINAL_URL.remove(final_url)
    show_final_URL()

def save_article():
    global PUBLISHED_ARTICLES
    global NOT_PUBLISHED_ARTICLES
    global SAVED_ARTICLES
    global FINAL_ARTICLE

    if len(FINAL_ARTICLE) > 0:
        save_URL()
        for final_article in FINAL_ARTICLE:
            if final_article in NOT_PUBLISHED_ARTICLES:
                SAVED_ARTICLES += [final_article]
                FINAL_ARTICLE.remove(final_article)
                NOT_PUBLISHED_ARTICLES.remove(final_article)
            if final_article in PUBLISHED_ARTICLES:
                messagebox.showerror('Error', 'Already published...')
                pass
            if final_article in SAVED_ARTICLES:
                messagebox.showerror('Error', 'Already saved...')
                pass
            else:
                SAVED_ARTICLES += [final_article]
                FINAL_ARTICLE.remove(final_article)
    else:
        messagebox.showerror('Error', 'No available article...') 
    show_final_arcticle()

def save_URL():
    global PUBLISHED_URL
    global NOT_PUBLISHED_URL
    global SAVED_URL
    global FINAL_URL

    for final_url in FINAL_URL:
        if final_url in NOT_PUBLISHED_URL:
            SAVED_URL += [final_url]
            FINAL_URL.remove(final_url)
            NOT_PUBLISHED_URL.remove(final_url)
        if final_url in PUBLISHED_URL:
            pass
        if final_url in SAVED_URL:
            pass
        else:
            SAVED_URL += [final_url]
            FINAL_URL.remove(final_url)
    show_final_URL()

def next_article():
    global FINAL_ARTICLE

    if len(FINAL_ARTICLE) > 0:
        next_URL()
        for final_article in FINAL_ARTICLE:
            FINAL_ARTICLE.remove(final_article)
            new_article_label = ttk.Label(
                tk,
                width = 125,
                text = final_article,
                font = ("Times New Roman", "10"),
            )
            new_article_label.place(x = 30, y = 350)
    else:
        messagebox.showerror('Error', 'No available article...') 
    show_final_arcticle()

def next_URL():
    global FINAL_URL

    for final_url in FINAL_URL:
        FINAL_URL.remove(final_url)
    show_final_URL()

def see_article():
    global FINAL_URL

    if len(FINAL_URL) > 0:
        for final_url in FINAL_URL:
            webbrowser.open(final_url, new=0, autoraise=True)
    else:
        messagebox.showerror('Error', 'No available article...\nThere is no available article or you stopped searching.')

def insert_data_to_list():
    URL_listbox.insert('end', home_news)
    URL_listbox.insert('end', world_news)
    access_token_field.insert('end', "Insert Access Token from www.developers.facebook.com")
    subject_id_field.insert('end', "362860434082902")
    post_field.insert('end', "Created by #fbreposter")

def stop_searching_articles():
    global RESULT_ARTICLES

    if len(RESULT_ARTICLES) > 0:
        RESULT_ARTICLES[:] = []
        count_result_articles()
        FINAL_ARTICLE[:] = []
        FINAL_URL[:] = []

        new_article_label = ttk.Label(
            tk,
            width = 125,
            text = "Articles searching stopped ...\n  \n  ",
            font = ("Times New Roman", "10"),
        )
        new_article_label.place(x = 30, y = 350)

    else:
        messagebox.showerror('Error', 'Unable. Searching have not started...') 

def get_access_token():
    webbrowser.open("https://developers.facebook.com/tools/explorer/", new=0, autoraise=True)

def display_subject_name():
    subject_id = subject_id_field.get()
    if subject_id == "FB NUMBER ID":
        subject_name_label = ttk.Label(
            None,  
            text = "FB PAGE",  
            font = ("Times New Roman", "13", "bold"),  
            background = "#336699",  
            foreground = "#FFFFFF"  
        )
        subject_name_label.place(x = 280, y = 568)
    else:
        subject_name_label = ttk.Label(
            None,  
            text = "No Subject Name",  
            font = ("Times New Roman", "13", "bold"),  
            background = "#336699",  
            foreground = "#FFFFFF"  
        )
        subject_name_label.place(x = 280, y = 568)

def clear_all_lists():
    global RELEVANT_ARTICLES
    global NOT_PUBLISHED_ARTICLES
    global PUBLISHED_ARTICLES
    global RESULT_ARTICLES
    global FINAL_ARTICLE
    global SAVED_ARTICLES
    global RELEVANT_URL
    global RESULT_URL
    global FINAL_URL
    global NOT_PUBLISHED_URL
    global PUBLISHED_URL
    global SAVED_URL

    RELEVANT_ARTICLES[:] = []
    NOT_PUBLISHED_ARTICLES[:] = []
    PUBLISHED_ARTICLES[:] = []
    RESULT_ARTICLES[:] = []
    FINAL_ARTICLE[:] = []
    SAVED_ARTICLES[:] = []
    RELEVANT_URL[:] = []
    RESULT_URL[:] = []
    FINAL_URL[:] = []
    NOT_PUBLISHED_URL[:] = []
    PUBLISHED_URL[:] = []
    SAVED_URL[:] = []

    new_article_label = ttk.Label(
        tk,
        width = 125,
        text = "All lists deleted ... \n  \n  ",
        font = ("Times New Roman", "10"),
    )
    new_article_label.place(x = 30, y = 350)
    count_result_articles()


# MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP # MAIN LOOP
if __name__ == "__main__":
    tk = tktr.Tk()
    tk.geometry ("800x600")
    tk.title("Scraper_Reposter 1.0")
    tk.resizable(0,0)
    tk.configure(bg = "#336699")

    fb_img = ImageTk.PhotoImage(
        file = r"C:\Users\kalvo\OneDrive\Dokumenty\Python\Web_Scraper 1.0\Reposter 1.0\fb_logo.png"
    )
    fb_logo_label = Label(
        tk,
        image = fb_img,
    )
    fb_logo_label.place(x = 390, y = 18)

    sz_img = ImageTk.PhotoImage(
        file = r"C:\Users\kalvo\OneDrive\Dokumenty\Python\Web_Scraper 1.0\Reposter 1.0\sz_logo.png"
    )
    sz_logo_label = Label(
        tk,
        image = sz_img,
    )
    sz_logo_label.place(x = 295, y = 18)

    header_label = ttk.Label(  
        None,  
        text = "REPOSTER 1.0",  
        font = ("Castellar", "30"),  
        background = "#336699",  
        foreground = "#FFFFFF" 
    )
    header_label.place(x = 480, y = 10)

    sign_label = ttk.Label(  
        None,  
        text = "by VK",  
        font = ("Edwardian Script ITC", "25"),  
        background = "#336699",  
        foreground = "#FFFFFF" 
    )
    sign_label.place(x = 680, y = 55)

    keyword_label = ttk.Label(
        None,  
        text = "What are you looking for?",  
        font = ("Times New Roman", "13", "bold"),  
        background = "#336699",  
        foreground = "#FFFFFF"  
    )
    keyword_label.place(x = 30, y = 110 )

    keyword_field = ttk.Entry(  
        None,  
        font = ("Times New Roman", "12"),  
        width = 40,  
        background = "#336699",  
        foreground = "#000000"  
    )
    keyword_field.place(x = 30, y = 140)

    URL_listbox_label = ttk.Label(
        None,  
        text = "Where do you want to search?",  
        font = ("Times New Roman", "13", "bold"),  
        background = "#336699",  
        foreground = "#FFFFFF"  
    )
    URL_listbox_label.place(x = 30, y = 180 )

    URL_listbox = tktr.Listbox(
        None,  
        width = 40,  
        height = 3,
        font = ("Times New Roman", "12"),  
        selectmode = "Single",  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#336699"
    )
    URL_listbox.place(x = 30, y = 210)
    
    search_articles_button = Button(  
        tk,
        bg = "#056F2D",
        fg = "#FFFFFF",   
        text = "Search Articles",  
        width = 21,  
        command = search_articles  
    )
    search_articles_button.place(x = 30, y = 280)
    
    stop_searching_button = Button(  
        tk,
        bg = "#D31B1B",
        fg = "#FFFFFF",        
        text = "Stop Searching",  
        width = 21,  
        command = stop_searching_articles  
    )
    stop_searching_button.place(x = 200, y = 280)

    saved_articles_button = Button(  
        tk,
        bg = "#07248F",
        fg = "#FFFFFF",
        text = "Saved Articles",  
        width = 21,  
        command = transform_saved_to_result  
    )
    saved_articles_button.place(x = 410, y = 180)

    not_published_articles_button = Button(  
        tk,
        bg = "#56079B",
        fg = "#FFFFFF",
        text = "Not Published Articles",  
        width = 21,  
        command = transform_not_published_to_result  
    )
    not_published_articles_button.place(x = 575, y = 180)

    published_articles_button = Button(  
        tk,
        bg = "#056F2D",
        fg = "#FFFFFF",
        text = "Published Articles",  
        width = 21,  
        command = transform_published_to_result  
    )
    published_articles_button.place(x = 410, y = 215)

    clear_all_lists_button = Button(  
        tk,
        bg = "#D31B1B",
        fg = "#FFFFFF",
        text = "Clear All Lists",  
        width = 21,  
        command = clear_all_lists  
    )
    clear_all_lists_button.place(x = 575, y = 215)

    publish_button = Button(  
        tk,
        bg = "#056F2D",
        fg = "#FFFFFF",
        text = "PUBLISH",  
        width = 21,  
        command = publish_article  
    )
    publish_button.place(x = 30, y = 425)

    do_not_publish_article_button = Button(  
        tk,
        bg = "#56079B",
        fg = "#FFFFFF",
        text = "DO NOT PUBLISH",  
        width = 21,  
        command = do_not_publish_article  
    )
    do_not_publish_article_button.place(x = 200, y = 425)

    save_article_button = Button(  
        tk,
        bg = "#07248F",
        fg = "#FFFFFF", 
        text = "SAVE",  
        width = 21,  
        command = save_article  
    )
    save_article_button.place(x = 370, y = 425)

    next_img = PhotoImage(
        file = r"C:\Users\kalvo\OneDrive\Dokumenty\Python\Web_Scraper 1.0\Reposter 1.0\img_next.png"
    )
    small_next_img = next_img.subsample(11)
    next_article_button = Button(  
        tk,
        bg = "#DDCACA",
        fg = "#000000", 
        image = small_next_img,  
        width = 55,  
        command = next_article  
    )
    next_article_button.place(x = 550, y = 425)

    see_article_button = Button(  
        tk,
        bg = "#D7D409",
        fg = "#000000",  
        text = "SEE ARTICLE",  
        width = 21,  
        command = see_article  
    )
    see_article_button.place(x = 630, y = 425)

    article_listbox_label = ttk.Label(
        None,  
        text = "Found Articles: ",  
        font = ("Times New Roman", "13", "bold"),  
        background = "#336699",  
        foreground = "#FFFFFF"  
    )
    article_listbox_label.place(x = 30, y = 320)

    article_label = ttk.Label(
        tk,
        width = 125,
        text = "No searched articles ...",
        font = ("Times New Roman", "10"),
    )
    article_label.place(x = 30, y = 350)

    post_label = ttk.Label(
        None,  
        text = "Do you wish to add something to the post?",  
        font = ("Times New Roman", "13", "bold"),  
        background = "#336699",  
        foreground = "#FFFFFF"  
    )
    post_label.place(x = 30, y = 460)

    post_field = ttk.Entry(  
        None,  
        font = ("Times New Roman", "10"),  
        width = 125,  
        background = "#336699",  
        foreground = "#000000"  
    )
    post_field.place(x = 30, y = 490)

    access_token_label = ttk.Label(
        None,  
        text = "Access Token: ",  
        font = ("Times New Roman", "13", "bold"),  
        background = "#336699",  
        foreground = "#FFFFFF"  
    )
    access_token_label.place(x = 30, y = 540 )

    access_token_field = ttk.Entry(  
        None,  
        font = ("Times New Roman", "10", "italic"),  
        width = 70,  
        background = "#336699",  
        foreground = "#000000"  
    )
    access_token_field.place(x = 150, y = 540)

    get_access_token_button = Button(  
        None,
        bg = "#D7D409",
        fg = "#000000",
        text = "Get Access Token",  
        width = 21,  
        command = get_access_token  
    )
    get_access_token_button.place(x = 490, y = 565)

    subject_id_label = ttk.Label(
        None,  
        text = "Subject ID: ",  
        font = ("Times New Roman", "13", "bold"),  
        background = "#336699",  
        foreground = "#FFFFFF"  
    )
    subject_id_label.place(x = 30, y = 570 )

    subject_id_field = ttk.Entry(  
        None,  
        font = ("Times New Roman", "10"),  
        width = 20,  
        background = "#336699",  
        foreground = "#000000"  
    )
    subject_id_field.place(x = 150, y = 570)

    insert_data_to_list()
    count_result_articles()
    #display_subject_name()
tk.mainloop()

