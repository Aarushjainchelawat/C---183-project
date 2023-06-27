from tkinter import *
import requests
import json

root = Tk()
root.title("Capital City App")
root.geometry("500x500")
root.config(bg = "black")

heading_label = Label(root , text = "Capital City Name" , font= ("Helvetica" , 18 , "bold") , bg = "black" , fg = "Cyan")
heading_label.place(relx = 0.5, rely = 0.2 , anchor = CENTER)

entry = Entry(root , bg= "light blue")
entry.place(relx = 0.5 , rely= 0.3 , anchor=CENTER)

country = Label(root , text = "Country : " , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
country.place(relx = 0.3 , rely= 0.5 , anchor = CENTER)

region = Label(root , text = "Region : " , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
region.place(relx = 0.3 , rely= 0.6 , anchor = CENTER)

language = Label(root , text = "Language : " , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
language.place(relx = 0.3 , rely= 0.7 , anchor = CENTER)

population = Label(root , text = "Population : " , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
population.place(relx = 0.3 , rely= 0.8 , anchor = CENTER)

area = Label(root , text = "Area : " , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
area.place(relx = 0.3 , rely= 0.9 , anchor = CENTER)


country_label = Label(root , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
country_label.place(relx = 0.5 , rely= 0.5 , anchor = CENTER)

region_label = Label(root, bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
region_label.place(relx = 0.5 , rely= 0.6 , anchor = CENTER)

language_label = Label(root, bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
language_label.place(relx = 0.5 , rely= 0.7 , anchor = CENTER)

population_label = Label(root  , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
population_label.place(relx = 0.5 , rely= 0.8 , anchor = CENTER)

area_label = Label(root , bg = "black" , fg = "cyan" , font = ("helvetica" , 14 , "bold"))
area_label.place(relx = 0.5 , rely= 0.9 , anchor = CENTER)

def capital_city() :
    api_request =requests.get("https://restcountries.com/v3.1/capital/"+ entry.get())
    api_output_json = json.loads(api_request.content)
    
    country = api_output_json[0]['name']['common']
    region = api_output_json[0]['region']
    language = api_output_json[0]['languages']['fra']
    population = api_output_json[0]['population']
    area = api_output_json[0]['area']
    
    country_label["text"] = " " + country
    region_label["text"] = " " + region
    language_label["text"] = " " + language
    population_label["text"] = " " + str(population)
    area_label["text"] = " " + str(area) + "sq.m"
    
    
    
city_btn = Button(root , text = "City Details" , command = capital_city , bg = "yellow" , fg = "black" , relief= FLAT)
city_btn.place(relx = 0.4 , rely= 0.4 , anchor= CENTER)
    
    

root.mainloop()
