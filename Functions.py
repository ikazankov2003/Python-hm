import sys
from collections import defaultdict
from datetime import datetime
from WritingValues import Note
SEPARATOR = 80 * "="


class Oportunities:
    def __init__(self):
        self.notes = {}
        self.last_id = 1

    def create(self, memo, tag, data):
        self.notes[self.last_id] = Note(memo, tag, self.last_id, data)
        self.last_id += 1

    def upgrade(self, id, memo, tag, data=None):
        self.notes[id].modify(id, memo, tag, data)
        for i in range(1, len(self.notes)+1):
            self.notes[i].id = i + 1
        self.notes[id].id = 1
        self.notes[id], self.notes[1] = self.notes[1], self.notes[id]


    def search(self, filter):
        found_results = []
        for i in self.notes:
            result = self.notes[i]
            if filter in result.memo or filter in result.tag:
                found_results.append(result)

    def show(self, notes = None):
        if not notes:
            notes = self.notes
        for note in notes:
            if type(note) == int:
                note = notes[note]
            print(f"""Note id: {note.id} \nNote tags: {note.tag}
Note text: {note.memo} \nNote tags: {note.data}""")

    def sort(self, border1, border2):
        found_results = []
        for note in self.notes:
            if border1 < self.notes[note].data < border2:
                found_results.append(self.notes[note])

    def quit_prog(self):
        print("Thank you for using your Notebook today.\n")
        sys.exit(0)
