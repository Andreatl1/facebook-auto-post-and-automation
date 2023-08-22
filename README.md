# facebook-auto-post
This project is to do auto post in the marketplace of Facebook. I have tested on Windows 10 //previous owner, now i'm using it on linux.

## Instructions:
1. Fill the config.ini with the right info (check config_example.ini like example).
2. Install the requirements
3. Run create_database.py and fill with some posts to Facebook Marketplace.
4. Need to download the driver for Firefox: https://github.com/mozilla/geckodriver/releases (the firefox driver allows you to use emojis, chrome does not)
5. Run app.py to post in Facebook Marketplace.
6. Run delete.py to delete all your post in Facebook Marketplace. This because in Facebook you cannot post the same post multiple times. (I think Facebook has a bug, because all the time I try to delete a post and refresh the page, appears again) 

Explanation of the code 🖥️⌨️:
https://youtu.be/WPBVR3aGzxk

marketplace_options.json -> I have added only the devices, categories, states, etc, all about in spanish. You need to add more languages right here and maybe more options. I only use to post in Marketplace things about videogames, electronic and cellphones.

The code needs a lot of changes. You could help me with improves. 

Subscribe to Youtube 🎬:
https://www.youtube.com/channel/UCnDCaOvsAMetyHOz9q0iaVA?sub_confirmation=1

For help me 💰:
paypal.me/eselejuanito

Email:
eselejuanito@gmail.com# facebook-marketplace-automation

### Upgrading it with
#### django-site to manage post: add, modify, remove.
#### adjust old features
#### new features like renew, delete one element, add one element for time through one flag
##### making change to the database and marketplace_options.json according to the django model
###### renew features - auto_renew_posts.py can be used with crontab
###### modify posts feature over facebook marketplace
###### adding google photos download through google api
###### ability to choose where to publish a product facebook - subito


per avere l'ordine le foto vengono salvate in base a come sono state selezionate img/article/foto{i}.jpeg mandando ciò da js sulle pagine admin verso il gestore


essendo che marketplace avvolte quando si elimina un annuncio in modo diretto dalla dashboard non lo elimina su alcuni gruppi
cambiare l'implementazione per fare in modo vado su ogni gruppo ad eliminare il dato articolo