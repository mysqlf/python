from scrapy.exceptions import DropItem

class TutorialPipeline(object):

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in item['name']:
                raise DropItem("Contains forbidden word: %s" % word)
            else:
                pass
        return item
class FilterWordsPipeline(object):
    pass