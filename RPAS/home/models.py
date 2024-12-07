from django.db import models


class User_Profile(models.Model):
    choice_subjects = [('English','English'),('Hindi','Hindi'),('Science','Science'),('Political','Political'),('Math','Math'),('Reasoning','Reasoning'),('Geography','Geography')]

    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pic/')
    message = models.TextField(max_length=260, default='')
    email = models.EmailField(max_length=254, unique=True)
    subjects = models.CharField(max_length=100, choices=choice_subjects, default='')

    def __str__(self):
        return self.name+'_'+self.email
    

class Video(models.Model):
    title = models.CharField(max_length=200) 
    video_image = models.ImageField(upload_to='video_image/',default='')
    description = models.TextField(blank=True)      
    video_file = models.FileField(upload_to='videos/')    
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.title


class PDFNotes(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdf_notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# username = root
# password = root