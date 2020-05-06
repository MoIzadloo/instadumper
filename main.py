from modules.scraper import scraper , NoPageException


class main():
    def __init__(self):
        def menu_builder(options):
            for idx,option in enumerate(options,1):
                return f'{idx}- {option}\n'
            
        self.link = ''
        self.cookies = {}
        self.menu_options = ['instagram page dumper']
        self.menu = menu_builder(self.menu_options)
        self.instagram = '''

              ▄█████████████████████████▄
            ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
            ███████████▀▀░░░░░▀▀███████████
            █░░░░░░░██░░▄█████▄░░██░░░░░░░█
            █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
            █░░░░░░░██░██░░░░░██░██░░░░░░░█
            █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
            █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
            █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
            █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
            ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
              ▀█████████████████████████▀

    <==$$$$== CODED BY github.com/moizadloo ==$$$$==>

        '''

    def main(self):
        while True:
            print(self.instagram)
            print(self.menu)
            option = str(input('$>'))
            if option == '1':
                print('insert the page name :')
                page_name = str(input('$>'))
                print('insert your cookie (for private pages) :')
                cookies =  str(input('$>'))
                if cookies == '':
                    cookies = 'no cookies'
                print('[ + ] page name {} selected !'.format(page_name))
                print('[ + ] your cookie {}'.format(cookies))
                try:
                    scraper(page_name,cookies).main()
                except NoPageException:
                    print('[ - ] page {} not found !'.format(page_name))
                print('progress finished !')


if __name__ == "__main__":
    main().main()
