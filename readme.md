**Note: download and store chromedriver in the current folder**

## Download chrome driver from link below

 [chromedriver](https://chromedriver.chromium.org/downloads).

## Available Scripts

Install Selenium using this command:

### `pip install selenium`

```python
#creating an instance
bot = GramBot.chrome()

bot.enter_username(insta_email)

bot.enter_password(insta_pass)

bot.click_login()

bot.scrollUp(40)
bot.scrollDown(40)

bot.homepage()

bot.search_hashtag('topic')

bot.click_on_pic()
bot.next_button()
bot.prev_button()

bot.like()

bot.is_liked()


bot.count_follower_inslide()
bot.follow_on_slide()
bot.unfollow_on_slide()
bot.back_from_slide()


bot.find_people('name of the person')
bot.follow()
bot.unfollow()

bot.comment_on_slide_post('Awesome')
bot.delete_posted_comment()
bot.back_from_slide()

bot.click_setting_button()
bot.back_from_settings()

bot.comment('True')

```

