import pickle

class Friend():
  def __init__(self, name, mobile, email, city):
    self._name = name
    self._mobile = mobile
    self._email = email
    self._city = city

  def get_name(self):
    return self._name

  def get_mobile(self):
    return self._mobile

  def get_email(self):
    return self._email

  def get_city(self):
    return self._city
  def set_name(self, name):
    self._name = name

  def set_mobile(self, mobile):
    self._mobile = mobile

  def set_email(self, email):
    self._email = email

  def set_city(self, city):
    self._city = city
class Dictionary():
  def __init__(self, pickle_path):
    self._friend_dictionary = {}
    self._pickle_path = pickle_path

  def add_friend(self, name, mobile, email, city):
    if name in self._friend_dictionary:
      return False
    
    f = Friend(name, mobile, email, city)
    self._friend_dictionary[name] = f
    return True
  def update_friend(self, name, mobile, email, city):
    if name not in self._friend_dictionary:
      return False
    
    f = self._friend_dictionary[name]
    f.set_mobile(mobile)
    f.set_email(email)
    f.set_city(city)
    self._friend_dictionary[name] = f
    return True  

  def delete_friend(self, name):
    if name not in self._friend_dictionary:
      return False
    
    del self._friend_dictionary[name]
    return True
  def display_dictionary(self):
    for name, obj in self._friend_dictionary.items():
      print(obj.get_name(), obj.get_mobile(), obj.get_email(), obj.get_city())

  def save_dictionary(self):
    fp = open(self._pickle_path, 'wb')
    pickle.dump(self._friend_dictionary, fp)
    fp.close()
    
  def load_dictionary(self):
    fp = open(self._pickle_path, 'rb')
    self._friend_dictionary = pickle.load(fp)
    fp.close()
pickle_file = 'dictionary.pickle'
d = Dictionary(pickle_file)
d.add_friend('Ajay', '9638527410', 'ajay@gmail.com', 'Rajkot')
d.add_friend('Ganesh', '9638527410', 'ganesh@gmail.com', 'Gunagad')
d.save_dictionary()
d = Dictionary(pickle_file)
d.load_dictionary()
d.display_dictionary()
d = Dictionary(pickle_file)
d.load_dictionary()
d.add_friend('Raj', '9857463212', 'raj@yahoo.com', 'Surat')
d.update_friend('Ganesh', '9865321470', 'ganesh@gmail.com', 'Vadodara')
d.display_dictionary()
d.save_dictionary()