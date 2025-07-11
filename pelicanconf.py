AUTHOR = 'Janneke Verbeek'
SITENAME = "Janneke's Webpage"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Add a theme
THEME = 'themes/Pelican-Cid' 
USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('About', 'about'),('Publications', 'publications'),('Posts', 'posts'))

PLUGINS=["render_math"]
