# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:22:01 2020

@author: Abdelrahman Ashraf
"""


import requests
import re
from bs4 import BeautifulSoup #to pull all the content of the website
import validators #to check if the URL is valid of or not 
from urllib.parse import urlparse #to break up the URL into meaningful pieces




class GettingToPhilosiphy(object):
    def __init__(self , starting_url):
        self.starting_url = starting_url
        self.visited = set() 
    
    def get_html(self , url):
        valid = validators.url(url)
        if valid == True:
            html = requests.get(url)
            return html.content.decode('latin-1')
        else:
            return None
    
    def get_links(self , url):#to extract links
        html = self.get_html(url)
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html) 
        for i, link in enumerate(links):    
            if not urlparse(link).netloc:    
                link_with_base = base + link    
                links[i] = link_with_base 
                
        return set(filter(lambda x: 'mailto' not in x, links))
    
    def extract_info(self, url):                                
        html = self.get_html(url)                               
        return None  
    
        
    
