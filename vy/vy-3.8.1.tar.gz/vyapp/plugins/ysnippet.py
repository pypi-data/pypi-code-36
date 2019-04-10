"""
Overview
========

This plugin is used to store snippets in a sqlite database. 
When it first starts it creates the database on your home directory.

You can store the snippets and retrieve them based on patterns,
Example: django + resolve + url.

The search is done through the snippet title or data.

Key-Commands
============

Mode: ALPHA
Event: <Key-p>
Description: Store in the sqlite database the selected region of text from the
focused AreaVi instance.

Mode: ALPHA
Event: <Key-i>
Description: Perform a search based on a pattern. The pattern looks as follow:
Pattern: str0 + str1 + str2 + ...
The matched snippets will contain each one of the strings either in the title
or in the data attribute.

"""

from os.path import expanduser, join
from vyapp.widgets import OptionWindow
from vyapp.areavi import AreaVi
from tkinter import ACTIVE
from vyapp.ask import Ask
from re import split
from vyapp.app import root
import sqlite3

class SnippetPicker(OptionWindow):
    def __init__(self, conn, cur):
        self.cur  = cur
        self.conn = conn
        OptionWindow.__init__(self)

        self.listbox.bind('<Alt-comma>', self.drop_on_tab, add=True)
        self.listbox.bind('<Return>', self.drop_on_cur)
        self.listbox.bind('<Key-d>', self.delete)

    def  __call__(self, options=[]):
        options = zip(map(lambda ind: ind[1], options),
        map(lambda ind: (ind[0], ind[2]), options))
        super(SnippetPicker, self).__call__(list(options))
        print(self.options)

    def drop_on_tab(self, event):
        area = root.note.create('none')

        index = self.listbox.index(ACTIVE)
        snippet = self.options[index][1][1]

        area.insert('insert', snippet)
        area.see('insert')

        # Select the tab.
        root.note.select(area.master.master.master)
        root.status.set_msg('Snippet: %s!' % self.options[index][0])
        self.close()
        
    def drop_on_cur(self, event):
        index   = self.listbox.index(ACTIVE)
        snippet = self.options[index][1][1]

        AreaVi.INPUT.insert('insert', snippet)
        AreaVi.INPUT.see('insert')
        root.status.set_msg('Snippet: %s!' % self.options[index][0])

        self.close()

    def delete(self, event):
        index   = self.listbox.index(ACTIVE)
        values = (self.options[index][1][0],)

        self.cur.execute('''DELETE FROM snippet where id=?''', values)
        self.conn.commit()
        root.status.set_msg('Snippet deleted!')
        self.listbox.delete(index)
        
        # Otherwise it gets messed up.
        del self.options[index]

class Ysnippet(object):
    nocas   = True
    db_name = join(expanduser('~'), '.ysnippet.db')
    conn    = sqlite3.connect(db_name)
    cur     = conn.cursor()
    picker  = SnippetPicker(conn, cur)

    def __init__(self, area):
        """

        """

        self.area   = area

        area.install('ysnippet',
        ('ALPHA', '<Key-p>', self.put),
        ('ALPHA', '<Control-i>', self.reload),
        ('ALPHA', '<Key-i>', self.find),)

        # Create table
        self.cur.execute('''CREATE TABLE if not exists 
        snippet (id integer PRIMARY KEY, title text, data text);''')

    def put(self, event):
        """
        In order to update a snippet it has to contain
        a field @(id)
        """

        ask = Ask()

        if not ask.data: 
            return

        values = (ask.data, self.area.join_ranges('sel', '\n'))

        self.area.tag_remove('sel', 'sel.first', 'sel.last')
        
        self.cur.execute('''INSERT INTO snippet 
        (title, data) VALUES (?, ?)''', values)

        self.conn.commit()
        self.area.chmode('NORMAL')

        root.status.set_msg('Snippet saved!')

    def find(self, event):
        """
        """
        ask = Ask()

        # If it is none then the user canceled the entry.
        # It should accept '' as a valid entry.
        if ask.data == None: return
        
        matches = self.build_sql(ask.data)

        if not len(matches):
            root.status.set_msg('No snippet found')
        else:
            self.choices(matches)
        self.area.chmode('NORMAL')

    def build_sql(self, pattern):
        tmp = '(title LIKE ? or data LIKE ?)'
        chks = split(' *\+ *', pattern)

        attrs = ['%' + '%s' % indi + '%' for indi in chks
            for indj in range(0, 2)]

        sql = "SELECT * FROM snippet WHERE %s" % ' and '.join([tmp] * len(chks))

        print('Ysnipet dropping sql:', sql)
        print('Ysnipet dropping attrs:', attrs)

        self.cur.execute(sql, attrs)
        matches = self.cur.fetchall()
        return matches

    def reload(self, event):
        self.picker.display()
        self.area.chmode('NORMAL')

    def choices(self, matches):
        root.status.set_msg('Found snippets!')
        self.picker(matches)


install = Ysnippet




