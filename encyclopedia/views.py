from django.shortcuts import render
from django.http import HttpResponse

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    entry = util.get_entry(title)
        
    if entry == None:
        
        return render(request, "encyclopedia/not-found.html", {
            "title": title,
            "entry": entry
        })
        
    else:
        return render(request, "encyclopedia/title-entry.html", {
            "title": title,
            "entry": entry
        })
        
def search(request):
	if request.method == "POST":
      
		newSearch = request.POST['q'].strip()
		entry = util.get_entry(newSearch)
		entries = util.list_entries()
			
		if entry:
    
			return render(request, "encyclopedia/title-entry.html", {
				"title": newSearch,
				"entry": entry
			})
   
		else:
    
			search_arr = []
   
			for search in entries:
				if newSearch in search:
					search_arr.append(search)
	
		return render(request, "encyclopedia/match-search.html", {
			"matches": search_arr
		})
  
def new(request):
  
	titles = util.list_entries()

	if request.method == 'POST':
	
		new_title = request.POST['title'].strip()
		new_content = request.POST['content'].strip()
  
		if len(new_title) == 0 | len(new_content) == 0: return render(request, "encyclopedia/new.html")
  
		if new_title in titles:
  
			print(new_title, new_content)
			
			return HttpResponse(f"<h1>{new_title}</h1> <p>is already exist.</p>")
   
		util.save_entry(new_title, new_content)
  
		return render(request, "encyclopedia/title-entry.html", {
            "title": new_title,
            "entry": new_content
        })

	return render(request, "encyclopedia/new.html")
    
       
        

