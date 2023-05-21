
# from webapp import create_app
# from webapp.config import config

# application = create_app(config['testing'])

# if __name__ == '__main__':
#     application.run(debug=True)


from webapp import create_app
from webapp.config import config

application = create_app(config['development'])

if __name__ == '__main__':
    application.run(debug=False)
    
    
    
        
