# encoding:utf-8
import platform

EXECUTE_FLAG = False

def is_windows():
    return 'Windows' == platform.system()


def is_not_windows():
    return not is_windows()


def show_banner():
    print("""
          .o8                       oooo                              
         "888                       `888                              
     .oooo888   .ooooo.  oo.ooooo.   888 .oo.    .ooooo.  ooo. .oo.   
    d88' `888  d88' `88b  888' `88b  888P"Y88b  d88' `88b `888P"Y88b  
    888   888  888   888  888   888  888   888  888   888  888   888  
    888   888  888   888  888   888  888   888  888   888  888   888  
    `Y8bod88P" `Y8bod8P'  888bod8P' o888o o888o `Y8bod8P' o888o o888o 
                          888                                         
                         o888o                                                     
     Author:CallMeE
     Base:Flask
     Url:https://github.com/Ca11MeE/dophon.git
         https://gitee.com/callmee/dophon.git                                                                          
    """)


def module_edge_print(module_name):
    def fun(f):
        def fields(*args, **kwargs):
            global EXECUTE_FLAG
            if not EXECUTE_FLAG:
                print('------------------', module_name, '<start>------------------\n')
            result = f(*args, **kwargs)
            if not EXECUTE_FLAG:
                print('\n------------------', module_name, '<end>------------------\n\n\n')
                EXECUTE_FLAG = not EXECUTE_FLAG
            return result
        return fields

    return fun
