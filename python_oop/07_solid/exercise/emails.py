from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyML(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class ISender(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def format(self):
        pass


class IMSender(ISender):

    def format(self):
        return ''.join(["I'm ", self.name])


class IReceiver(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def format(self):
        pass


class IMReceiver(IReceiver):

    def format(self):
        return ''.join(["I'm ", self.name])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


email = Email()
im_sender = IMSender('qmal')
im_receiver = IMReceiver('james')
content = MyML('Hello, there!')
email.set_content(content)
email.set_sender(im_sender)
email.set_receiver(im_receiver)
print(email)
