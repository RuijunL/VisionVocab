# VisionVocab

A mobile vocabulary-learning app power by object recognition

# Installation

After clone the repository, run: `pip install -r requirement.txt`

Now you should have Django and other required dependencies installed. Now run `python manage.py runserver`

To test the server, run: `curl -X POST -F 'image=@path/to/your/image.jpg' http://127.0.0.1:8000/caption/`

