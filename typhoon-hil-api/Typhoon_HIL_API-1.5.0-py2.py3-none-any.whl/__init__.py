# So that TyphoonTest can also use typhoon namespace being installed from other package
__path__ = __import__('pkgutil').extend_path(__path__, __name__)
