from mycroft import MycroftSkill, intent_file_handler


class CampusEventFinder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('finder.event.campus.intent')
    def handle_finder_event_campus(self, message):
        self.speak_dialog('finder.event.campus')


def create_skill():
    return CampusEventFinder()

