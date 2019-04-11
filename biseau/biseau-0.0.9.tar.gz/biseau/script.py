"""Definitions and functions applied to Script object.

The Script object waits for many parameters, detailed in its constructor,
and its main interface is the run_on method.

The run_on method, constituting the main API interface, IS A NIGHTMARE to generate.
From the Script point of view, the inner _run_on method (gotten from the module,
like JSON), maps a context/models and options to a string/generator of string.
The call_script function is uniformizing all of these in a single interface.

When the source_code attribute of a Script is modified, this run a machinery
whose goal is to build the _run_on method.
This machinery is not runned if run_on is given in the Script constructor.
The machinery is basically an extraction of the source code depending
of the language (python, asp, python file or asp file) and generate a standard
_run_on method based on that.
But because the script can also specify a (new) name, a (new) value for erase_context
and other attributes, that are parsed in module_loader.build_script_from_module,
it is necessary to call that function on the new module (induced by a source_code change).
Therefore, a new Script instance is built, from which all attributes are copied in the current instance.
The code is on the verge to lock itself in an infinite loop.

I'm sorry for the ones coming after.


"""
import clyngor
import traceback
from biseau import utils


class Script:

    def __init__(self, name:str, tags:set, description:str, module, options, options_values, input_mode, incompatible, spec_inputs, spec_outputs, inputs, outputs, source_code, language, erase_context, *, run_on:callable or None=None):
        self.name = str(name)  # human readable name
        self.tags = set(map(str, tags))  # set of tags identifying the script
        self.description = str(description)  # human readable and high level description of the script
        self.module = module  # reference to the module itself
        self.options = tuple(options)  # list of (name, type, default, description) describing each option
        self.options_values = dict(options_values)  # mutable mapping allowing to set options value to be used
        self.input_mode = input_mode  # define if run_on must receive the context or the resulting ASP models
        self.incompatible = set(incompatible)  # list of incompatibles modules
        self.spec_inputs = spec_inputs  # function in module to call to get the inputs knowing the parameters
        self.spec_outputs = spec_outputs  # function in module to call to get the outputs knowing the parameters
        self.inputs = inputs  # function in module to call to get all possible inputs
        self.outputs = outputs  # function in module to call to get all possible outputs
        self.language = str(language)  # string indicating the language implementing the source code
        self.erase_context = bool(erase_context)  # true if the script erase the context (default: false, context is kept)

        # creation of run_on function
        self.__source_code = str(source_code) if source_code else None  # don't trigger the setter
        assert source_code != 'None', "this already happened, it was because previous line called str() on source_code, which could be None"
        self._run_on = run_on
        if not self._run_on:
            self._run_on = compile_run_on(self.language, self.__source_code, self._update_from_module)
        else:
            self._run_on._source = self.__source_code

    def run_on(self, context:str, *args, **kwargs):
        return call_script(self, context, *args, **kwargs)

    @property
    def source_code(self) -> str:
        return self.__source_code

    @source_code.setter
    def source_code(self, new_source:str):
        self.__source_code = str(new_source)
        if self._run_on._source != self.source_code:
            self._run_on = compile_run_on(self.language, self.source_code, self._update_from_module)

    def _update_from_module(self, module):
        """Change all self attributes based on those of given module,
        especially language and source_code defining run_on

        This shouldn't be called when run_on is provided.

        """
        from biseau.module_loader import build_script_from_module
        script = build_script_from_module(module, defaults=vars(self))
        for key in vars(self):
            if getattr(script, key, None) is not None:
                setattr(self, key, getattr(script, key))
        if self._run_on:
            self._run_on._source = self.source_code
        # print('\tFROM:', {k: v for k, v in vars(module).items() if not k.startswith('_')})
        # print('\t TO :', {k: v for k, v in vars(self).items() if not k.startswith('_')})

    @staticmethod
    def call(script, context:str, *args, **kwargs):
        return call_script(script, context, *args, **kwargs)

    def __str__(self):
        return f"<Script language={self.language} code={bool(self.source_code)} #lines={len((self.source_code or '').splitlines())} erase={self.erase_context}>"


class Module:
    """Placeholder for a module/namespace.

    It's assumed safe to make them hashable on content. Also, the hashable
    property is only used during validation and initial core treatments.

    """
    def __hash__(self):
        return hash(tuple(self.__dict__.values()))

    @staticmethod
    def from_dict(mapping:dict) -> object:
        "Create Module instance with given dictionnary as members"
        module = Module()
        for key, val in mapping.items():
            setattr(module, key, val)
        return module



def solve_context(context:str, *, nb_model:int=0) -> clyngor.Answers:
    """Uniformized way to solve an ASP context"""
    return clyngor.solve(inline=context, nb_model=nb_model, options='--project').by_predicate.careful_parsing.int_not_parsed


def call_script(script, context:str, verbosity:int=0):
    """Uniformized call to a Script object"""
    if script.input_mode is str:
        input_data = context
    else:  # need a solving
        assert script.input_mode is iter
        input_data = solve_context(context)
    if verbosity >= 2:  print('RUN run_on… ', end='', flush=True)
    new_context = utils.join_on_genstr(script._run_on)(input_data, **script.options_values)
    if verbosity >= 2:  print('OK!')
    if verbosity >= 3:  print('NEW CONTEXT:', new_context)
    return new_context + ('\n' if script.erase_context else ('\n' + context))


def build_module_from_python_code(pycode:str, **module_options:dict):
    """Low level function, expecting some python code in string, and returning a namespace/module.
    """
    try:
        env = {}
        exec(pycode, env)
    except:
        print(f'Imported Python error:\n', traceback.format_exc())
    # env.update(module_options)
    env = {**module_options, **env}
    env['source_code'] = pycode
    env['language'] = 'python'
    # print('OPTIONS:', module_options, {k: v for k, v in env.items() if not k.startswith('_')})
    module = Module.from_dict({k: v for k, v in env.items() if not k.startswith('__')})
    # print('MODULE:', {k: v for k, v in vars(module).items() if not k.startswith('_')})
    return module


def compile_run_on(language:str, code:str, updater:callable=None) -> callable:
    """Return a runner on given language/code, call given updater with a module
    when a new python module is found

    """
    module = None
    if language == 'python':
        # we need to compile the source code to retrieve the run_on function
        module = build_module_from_python_code(code)
        if not hasattr(module, 'run_on'):  # make a phony run_on
            module.run_on = lambda context: ''
            # print('MODULE w/o run_on:', type(module), {k: v for k, v in vars(module).items() if not k.startswith('__')})
        run_on = module.run_on
    elif language == 'python file':
        # initialize
        with open(code) as fd:
            source = fd.read()
        module = build_module_from_python_code(source)
        if not hasattr(module, 'run_on'):  # make a phony run_on
            module.run_on = lambda context: ''
            # print('MODULE w/o run_on:', type(module), {k: v for k, v in vars(module).items() if not k.startswith('__')})
        run_on = module.run_on
    elif language == 'asp':
        def run_on(context:str):
            return code
    elif language == 'asp file':
        def run_on(context:str):
            with open(code) as fd:
                return fd.read()
    else:
        raise NotImplementedError(f"Language {language} is not supported.")

    run_on._source = code
    if updater and module:  updater(module)
    return run_on
