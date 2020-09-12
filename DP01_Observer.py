"""
Design Pattern - Behaviour - Observer
   - Observer : Needs the notification of changes in a dependent subject
   - Terminology
      - Subject  : Main Object
      - Observer : One or more objects, that observe the state of the object
      - One-Many : One Subject, Many Observer Relations

Guiding rules: Don't miss out when something interersting happens.
   - Observers are dependent on Subject, as Subject is the sole owner of the data
   - Observer, can subscribe/unsubscribe to the Subject
   - Subject update/notifies the Observers, with standard interface
   - Subject and Observers are decoupled. 
       - Subject does not care, What observer to with Notification.
       - Observer does now are, How article is created.
       - Observer does not bother Subject, Subject does not wait for status from Observer
    - Subject only expects standard notification method like BlogViewer.notify, it does not care who is subscribing.

References: 
    - https://github.com/aarav-tech/design-patterns-python

Common Use Case:
   - Weather Monitoring
   - Publisher/Channel (subject)  + viewers (observer). viewers will be many
   - Headhunter (subject) + Job Seeker (observer).

"""

def print_header(s):
	print( f"\n#{'-='*35}\n# {s} \n#{'-='*35}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Observer
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class BlogViewer:  # Observer class
    '''
    User class will act role of observer to subject
    '''

    def __init__(self, name):
        self.name = name
        self.new_articles = []

    def notify(self, article, blog_writer):
        print(f"{self.name} : Blogger '{blog_writer.name}' added new article '{article}'")
        self.new_articles.append(article)

    def __str__(self):
        return f"{self.__class__.__name__}:{self.name}"

    def read_new_articles(self):

        while(self.new_articles):
            article = self.new_articles.pop()
            print( f"Read new article '{article}'")


class BlogWriter:
    '''
    BlogWriter Write the blogs. 
    Notifies the viewers, when new article is added 
    '''
    def __init__(self, name):
        self.name = name
        self.__viewers = [] # View
        self.__articles = [] # Article is the subject

    def __str__(self):
        return f"{self.__class__.__name__}:{self.name}"

    def subscribe(self, subscriber):
        '''Adds new viewer'''
        print(f"Added {subscriber} to Blogger {self}" )
        self.__viewers.append(subscriber)

    def unsubscribe(self, subscriber):
        '''Removes viewer'''
        print(f"Removed {subscriber} to Blogger {self}" )
        return self.__viewers.remove(subscriber)

    def _notify_viewers(self, article):
        '''Notifying all the subsribers about new addition of an article'''
        for sub in self.__viewers:
            sub.notify(article, self)

    def add_article(self, article):
        '''Add new article and notify viewers'''
        self.__articles.append(article)
        self._notify_viewers(article)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Testing  Observer
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def test_Observer():

    viewer1 = BlogViewer("viewer1")
    viewer2 = BlogViewer("viewer2")
    viewer3 = BlogViewer("viewer3")

    writter1 = BlogWriter("writter1")

    print_header( f"'{viewer1}' and '{viewer2}' subscribed to '{writter1}'" )
    writter1.subscribe(viewer1)
    writter1.subscribe(viewer2)

    print_header( f"'{writter1}' added an article 'Article 1'" )
    writter1.add_article("Article 1")

    print_header( f"'{viewer2}' unsubscribed and '{viewer3}' subscribed to '{writter1}'" )
    writter1.unsubscribe(viewer2)
    writter1.subscribe(viewer3)
    writter1.add_article("Article 2")

    print_header( f"'{viewer1}' reads new articles" )
    viewer1.read_new_articles()


if __name__ == "__main__":
	test_Observer()



