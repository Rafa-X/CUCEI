from factory_pattern import FactoryClass

# handle the service by thread type class
def thread_handler(thread_name):
    #  get and create the object
    factory_obj = FactoryClass.get_class(thread_name)
    
    factory_obj.run()