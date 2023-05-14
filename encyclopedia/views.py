from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import random
from . import util

class NewEntryForm(forms.Form):
  title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Add a new title'}))
  content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control md-textarea mb-3', 'rows': 3}))

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
      
		new_search = request.POST['q'].strip()
		entry = util.get_entry(new_search)
		entries = util.list_entries()
		search_arr = []
		error_msg = f"{new_search}, there are no matches."
  
		if entry:
			return render(request, "encyclopedia/title-entry.html", {
				"title": new_search,
				"entry": entry
			})
   
		else:
			for search in entries:
				if new_search in search:
					search_arr.append(search)
     
			if not search_arr:
				print(search_arr)
				return render(request, "encyclopedia/match-search.html", {
					"error_msg": error_msg
				})
			
		return render(request, "encyclopedia/match-search.html", {
			"matches": search_arr,
		})
  
def newEntry(request):
  
	titles = util.list_entries()
 
	if request.method == 'POST':
		form = NewEntryForm(request.POST)
  
		if form.is_valid():
			new_title = form.cleaned_data['title']
			new_content = form.cleaned_data['content']
			error_msg = f"The {new_title} title, already exist."
   
			if new_title in titles:
				return render(request, "encyclopedia/new.html", {
      		"form": NewEntryForm(),
					"error_msg": error_msg
				})
     
			else:
				util.save_entry(new_title, new_content)
				return render(request, "encyclopedia/title-entry.html", {
					"title": new_title,
					"entry": new_content
				})
 
	return render(request, "encyclopedia/new.html", {
			"form": NewEntryForm()
	})
 

def editEntry(request, title):
	entry = util.get_entry(title)
 
	if entry is not None:
	
		if request.method == 'POST':
			form = NewEntryForm(request.POST)
			error_msg = f"The {title} must be has a content."
   
			if form.is_valid():
				edited_content = form.cleaned_data['content']

				util.save_entry(title, edited_content)
				return render(request, 'encyclopedia/title-entry.html', {
						"title": title,
						"entry": edited_content
					})
			else:
				return render(request, 'encyclopedia/editEntry.html', {
					"title": title,
					"entry": entry,
					"error_msg": error_msg
				})

		else:
			return render(request, 'encyclopedia/editEntry.html', {
				"title": title,
				"entry": entry
			})
   
	return render(request, "encyclopedia/not-found.html", {
	"title": title,
	})
 
def randomEntry(request):
  
	all_titles = util.list_entries()
	random_title = random.choice(all_titles)
	entry = util.get_entry(random_title)

	return render(request, "encyclopedia/title-entry.html", {
		"title": random_title,
		"entry": entry
	})