from django.shortcuts import render, redirect, get_object_or_404
from .models import User_Profile, Video, PDFNotes
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,VideoForm, PDFNotesForm


@login_required(login_url='login_page')
def Base(request):
    profiles = User_Profile.objects.all()
    videos = Video.objects.all()
    return render(request, 'base.html', {'profiles':profiles, 'videos':videos})

@login_required(login_url='login_page')
def Category_page(request):
    profiles = User_Profile.objects.all()
    return render(request, 'category.html',{'profiles':profiles})


@login_required(login_url='login_page')
def Contact_us(request):
    profiles = User_Profile.objects.all()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'contact.html', {'form':form, 'profiles':profiles})

@login_required(login_url='login_page')
def Edit_profile(request, id):
    profiles = User_Profile.objects.all()
    profile = get_object_or_404(User_Profile, id=id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProfileForm(instance=profile)
    return render(request, 'contact.html',{'form':form, 'profiles':profiles})

@login_required(login_url='login_page')
def Delete_profile(request, id):
    profile = get_object_or_404(User_Profile, id=id)
    if request.method == "POST":
        profile.delete()
        return redirect('home')
    return render(request, 'delete_profile.html',{'profile':profile})

# add videos 

@login_required(login_url='login_page')
def video_upload(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = VideoForm()
    return render(request, 'video_form.html',{'form':form})

# edit videos 
@login_required(login_url='login_page')
def edit_video(request, id):
    video = get_object_or_404(Video,id=id)
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = VideoForm(instance=video)
    return render(request, 'video_form.html',{'form':form})

@login_required(login_url='login_page')
def delete_video(request, id):
    video = get_object_or_404(Video,id=id)
    if request.method == "POST":
        video.delete()
        return redirect('home')

    return render(request, 'delete_video.html',{'video':video})

# play video
@login_required(login_url='login_page')
def video_detail(request,id):
    video = get_object_or_404(Video,id=id)
    return render(request,'video_detail.html',{'video':video})


# note add functions 
@login_required(login_url='login_page')
def Nots_page(request):
    profiles = User_Profile.objects.all()
    notes = PDFNotes.objects.all()
    return render(request, 'notes.html',{'profiles':profiles, 'notes':notes})

# notes Details function
@login_required(login_url='login_page')
def notes_detail(request, id):
    note = get_object_or_404(PDFNotes, id=id)
    return render(request, 'notes_detail.html',{'note':note})

# notes upload function
@login_required(login_url='login_page')
def upload_notes(request):
    if request.method == 'POST':
        form = PDFNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notes')

    else:
        form = PDFNotesForm()
    return render(request, 'pdf_form.html',{'form':form})

# notes Update function
@login_required(login_url='login_page')
def update_notes(request, id):
    note = get_object_or_404(PDFNotes, id=id)
    if request.method == "POST":
        form = PDFNotesForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')

    else:
        form = PDFNotesForm(instance=note)
    return render(request, 'pdf_form.html', {'form':form})

# notes Delete functions
@login_required(login_url='login_page')
def delete_notes(request,id):
    note = get_object_or_404(PDFNotes, id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'delete_notes.html',{'note':note})