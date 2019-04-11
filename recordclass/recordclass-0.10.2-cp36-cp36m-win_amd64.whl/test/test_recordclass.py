"""Unit tests for recordclass.py."""
import unittest, doctest, operator
from recordclass import recordclass
from collections import OrderedDict
import pickle, copy
import keyword
import re
import sys

try:
    from test import support
except:
    from test import test_support as support


TestNT = recordclass('TestNT', 'x y z')    # type used for pickle tests

class RecordClassTest(unittest.TestCase):

    def test_factory(self):
        Point = recordclass('Point', 'x y')
        self.assertEqual(Point.__name__, 'Point')
        self.assertEqual(Point.__doc__, 'Point(x, y)')
#         self.assertEqual(Point.__slots__, ())
        self.assertEqual(Point.__module__, __name__)
        self.assertEqual(Point.__attrs__, ('x', 'y'))

        self.assertRaises(ValueError, recordclass, 'abc%', 'efg ghi')       # type has non-alpha char
        self.assertRaises(ValueError, recordclass, 'class', 'efg ghi')      # type has keyword
        self.assertRaises(ValueError, recordclass, '9abc', 'efg ghi')       # type starts with digit

        self.assertRaises(ValueError, recordclass, 'abc', 'efg g%hi')       # field with non-alpha char
        self.assertRaises(ValueError, recordclass, 'abc', 'abc class')      # field has keyword
        self.assertRaises(ValueError, recordclass, 'abc', '8efg 9ghi')      # field starts with digit
        self.assertRaises(ValueError, recordclass, 'abc', '_efg ghi')       # field with leading underscore
        self.assertRaises(ValueError, recordclass, 'abc', 'efg efg ghi')    # duplicate field

        recordclass('Point0', 'x1 y2')   # Verify that numbers are allowed in names
        recordclass('_', 'a b c')        # Test leading underscores in a typename

        nt = recordclass('nt', 'the quick brown fox')                       # check unicode input
        self.assertNotIn("u'", repr(nt.__attrs__))
        nt = recordclass('nt', ('the', 'quick'))                           # check unicode input
        self.assertNotIn("u'", repr(nt.__attrs__))

        self.assertRaises(TypeError, Point._make, [11])                     # catch too few args
        self.assertRaises(TypeError, Point._make, [11, 22, 33])             # catch too many args

    @unittest.skipIf(sys.flags.optimize >= 2,
                     "Docstrings are omitted with -O2 and above")
    def test_factory_doc_attr(self):
        Point = recordclass('Point', 'x y')
        self.assertEqual(Point.__doc__, 'Point(x, y)')

    def test_name_fixer(self):
        for spec, renamed in [
            [('efg', 'g%hi'),  ('efg', '_1')],                              # field with non-alpha char
            [('abc', 'class'), ('abc', '_1')],                              # field has keyword
            [('8efg', '9ghi'), ('_0', '_1')],                               # field starts with digit
            [('abc', '_efg'), ('abc', '_1')],                               # field with leading underscore
            [('abc', 'efg', 'efg', 'ghi'), ('abc', 'efg', '_2', 'ghi')],    # duplicate field
            [('abc', '', 'x'), ('abc', '_1', 'x')],                         # fieldname is a space
        ]:
            self.assertEqual(recordclass('NT', spec, rename=True).__attrs__, renamed)

            
    def test_defaults(self):
        Point = recordclass('Point', 'x y', defaults=(10, 20))              # 2 defaults
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(1), Point(1, 20))
        self.assertEqual(Point(), Point(10, 20))

        Point = recordclass('Point', 'x y', defaults=(20,))                 # 1 default
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(1), Point(1, 20))

        Point = recordclass('Point', 'x y', defaults=())                     # 0 defaults
        self.assertEqual(Point(1, 2), Point(1, 2))
        with self.assertRaises(TypeError):
            Point(1)

        with self.assertRaises(TypeError):                                  # catch too few args
            Point()
        with self.assertRaises(TypeError):                                  # catch too many args
            Point(1, 2, 3)
        with self.assertRaises(TypeError):                                  # too many defaults
            Point = recordclass('Point', 'x y', defaults=(10, 20, 30))
        with self.assertRaises(TypeError):                                  # non-iterable defaults
            Point = recordclass('Point', 'x y', defaults=10)
        with self.assertRaises(TypeError):                                  # another non-iterable default
            Point = recordclass('Point', 'x y', defaults=False)

        Point = recordclass('Point', 'x y', defaults=None)                   # default is None
        self.assertIsNone(Point.__new__.__defaults__, None)
        self.assertEqual(Point(10, 20), Point(10, 20))
        with self.assertRaises(TypeError):                                  # catch too few args
            Point(10)

        Point = recordclass('Point', 'x y', defaults=[10, 20])               # allow non-tuple iterable
        self.assertEqual(Point.__new__.__defaults__, (10, 20))
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(1), Point(1, 20))
        self.assertEqual(Point(), Point(10, 20))

        Point = recordclass('Point', 'x y', defaults=iter([10, 20]))         # allow plain iterator
        self.assertEqual(Point.__new__.__defaults__, (10, 20))
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(1), Point(1, 20))
        self.assertEqual(Point(), Point(10, 20))
            
    def test_instance(self):
        Point = recordclass('Point', 'x y')
        p = Point(11, 22)
        self.assertEqual(p, Point(x=11, y=22))
        self.assertEqual(p, Point(11, y=22))
        self.assertEqual(p, Point(y=22, x=11))
        self.assertEqual(p, Point(*(11, 22)))
        self.assertEqual(p, Point(**dict(x=11, y=22)))
        self.assertRaises(TypeError, eval, 'Point(XXX=1, y=2)', locals())   # wrong keyword argument
        self.assertRaises(TypeError, eval, 'Point(x=1)', locals())          # missing keyword argument
        self.assertEqual(repr(p), 'Point(x=11, y=22)')
        #self.assertNotIn('__weakref__', dir(p))
        #print(p)
        self.assertEqual(p, Point._make([11, 22]))                          # test _make classmethod
        self.assertEqual(p.__attrs__, ('x', 'y'))                             # test __attrs__ attribute
        self.assertEqual(p._replace(x=1), Point(1, 22))                          # test _replace method
        self.assertEqual(p._asdict(), dict(x=1, y=22))                     # test _asdict method
        self.assertEqual(vars(p), p._asdict())                              # verify that vars() works

        p.x = 1
        self.assertEqual(p.x, 1)

        # verify that field string can have commas
        Point = recordclass('Point', 'x, y')
        p = Point(x=11, y=22)
        self.assertEqual(repr(p), 'Point(x=11, y=22)')

        # verify that fieldspec can be a non-string sequence
        Point = recordclass('Point', ('x', 'y'))
        p = Point(x=11, y=22)
        self.assertEqual(repr(p), 'Point(x=11, y=22)')
        
#     def test_nogc(self):
#         Point = recordclass('Point', 'x y')
#         Point_nogc = recordclass('Point_nogc', 'x y', gc=False)

    def test_tupleness(self):
        Point = recordclass('Point', 'x y')
        p = Point(11, 22)

        self.assertEqual(tuple(p), (11, 22))                                # coercable to a real tuple
        self.assertEqual(list(p), [11, 22])                                 # coercable to a list
        self.assertEqual(max(p), 22)                                        # iterable
        self.assertEqual(max(*p), 22)                                       # star-able
        x, y = p
        self.assertEqual(tuple(p), (x, y))                                         # unpacks like a tuple
        self.assertEqual((p[0], p[1]), (11, 22))                            # indexable like a tuple
        self.assertRaises(IndexError, p.__getitem__, 3)

        self.assertEqual(p.x, x)
        self.assertEqual(p.y, y)
        self.assertRaises(AttributeError, eval, 'p.z', locals())

    def test_odd_sizes(self):
        Zero = recordclass('Zero', '')
        self.assertEqual(Zero(), Zero())
        self.assertEqual(Zero._make([]), Zero())
        self.assertEqual(repr(Zero()), 'Zero()')
        self.assertEqual(Zero()._asdict(), {})
        self.assertEqual(Zero().__attrs__, ())

        Dot = recordclass('Dot', 'd')
        self.assertEqual(Dot(1), Dot(1,))
        self.assertEqual(Dot._make([1]), Dot(1,))
        self.assertEqual(Dot(1).d, 1)
        self.assertEqual(repr(Dot(1)), 'Dot(d=1)')
        self.assertEqual(Dot(1)._asdict(), {'d':1})
        self.assertEqual(Dot(1)._replace(d=999), Dot(999,))
        self.assertEqual(Dot(1).__attrs__, ('d',))

        # n = 5000
        n = 254 # SyntaxError: more than 255 arguments:
        import string, random
        names = list(set(''.join([random.choice(string.ascii_letters)
                                  for j in range(10)]) for i in range(n)))
        n = len(names)
        Big = recordclass('Big', names)
        b = Big(*range(n))
        self.assertEqual(b, Big(*tuple(range(n))))
        self.assertEqual(Big._make(range(n)), Big(*tuple(range(n))))
        for pos, name in enumerate(names):
            self.assertEqual(getattr(b, name), pos)
        repr(b)                                 # make sure repr() doesn't blow-up
        d = b._asdict()
        d_expected = dict(zip(names, range(n)))
        self.assertEqual(d, d_expected)
        b2 = b._replace(**dict([(names[1], 999),(names[-5], 42)]))
        b2_expected = list(range(n))
        b2_expected[1] = 999
        b2_expected[-5] = 42
        self.assertEqual(b2, Big(*tuple(b2_expected)))
        self.assertEqual(b.__attrs__, tuple(names))
        
    def test_annotations(self):
        C = recordclass('C', [('x',int),('y',int)])
        self.assertEqual(C.__new__.__annotations__, {'x':int, 'y':int})
        D = recordclass('D', [('x',int),'y'])
        self.assertEqual(D.__new__.__annotations__, {'x':int})

    def test_pickle(self):
        p = TestNT(x=10, y=20, z=30)
        for module in (pickle,):
            loads = getattr(module, 'loads')
            dumps = getattr(module, 'dumps')
            for protocol in range(-1, module.HIGHEST_PROTOCOL + 1):
                tmp = dumps(p, protocol)
                q = loads(tmp)
                self.assertEqual(p, q)
                self.assertEqual(p.__attrs__, q.__attrs__)
                self.assertNotIn(b'OrderedDict', dumps(p, protocol))

    def test_copy(self):
        p = TestNT(x=10, y=20, z=30)
        for copier in copy.copy, copy.deepcopy:
            q = copier(p)
            self.assertEqual(p, q)
            self.assertEqual(p.__attrs__, q.__attrs__)

    def test_name_conflicts(self):
        # Some names like "self", "cls", "tuple", "itemgetter", and "property"
        # failed when used as field names.  Test to make sure these now work.
        T = recordclass('T', 'itemgetter property self cls tuple')
        t = T(1, 2, 3, 4, 5)
        self.assertEqual(t, T(1,2,3,4,5))
        newt = t._replace(itemgetter=10, property=20, self=30, cls=40, tuple=50)
        self.assertEqual(newt, T(10,20,30,40,50))

        # Broader test of all interesting names in a template
        with support.captured_stdout() as template:
            T = recordclass('T', 'x')
        words = set(re.findall('[A-Za-z]+', template.getvalue()))
        words -= set(keyword.kwlist)
        words = list(words)
        if 'None' in words:
            words.remove('None')
        T = recordclass('T', words)
        # test __new__
        values = tuple(range(len(words)))
        t = T(*values)
        self.assertEqual(t, T(*values))
        t = T(**dict(zip(T.__attrs__, values)))
        self.assertEqual(t, T(*values))
        # test _make
        t = T._make(values)
        self.assertEqual(t, T(*values))
        # exercise __repr__
        repr(t)
        # test _asdict
        self.assertEqual(t._asdict(), dict(zip(T.__attrs__, values)))
        # test _replace
        t = T._make(values)
        newvalues = tuple(v*10 for v in values)
        newt = t._replace(**dict(zip(T.__attrs__, newvalues)))
        self.assertEqual(newt, T(*newvalues))
        # test __attrs__
        self.assertEqual(T.__attrs__, tuple(words))
        # test __getnewargs__
        #self.assertEqual(t.__getnewargs__(), newvalues)

    def test_repr(self):
        with support.captured_stdout() as template:
            A = recordclass('A', 'x')
        self.assertEqual(repr(A(1)), 'A(x=1)')
        # repr should show the name of the subclass
        class B(A):
            pass
        self.assertEqual(repr(B(1)), 'B(x=1)')
        
    def test_hash(self):
        A = recordclass('A', 'x y', readonly=True)
        a = A(1, 2)
        hash_a = hash(a)
        #self.assertEqual(hash(a), hash(tuple(a)))
        B = recordclass('B', 'x y', hashable=True)
        b = B(1, 2)
        hash_b = hash(b)
        #self.assertEqual(hash_b, hash(tuple(b)))
        b.x = -1
        self.assertNotEqual(hash(b), hash_b)

#     def test_source(self):
#         # verify that _source can be run through exec()
#         tmp = recordclass('NTColor', 'red green blue')
#         globals().pop('NTColor', None)          # remove artifacts from other tests
#         exec(tmp._source, globals())
#         self.assertIn('NTColor', globals())
#         c = NTColor(10, 20, 30)
#         self.assertEqual((c.red, c.green, c.blue), (10, 20, 30))
#         self.assertEqual(NTColor.__attrs__, ('red', 'green', 'blue'))
#         globals().pop('NTColor', None)          # clean-up after this test

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RecordClassTest))
    return suite
