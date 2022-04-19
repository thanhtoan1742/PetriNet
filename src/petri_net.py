import igraph as ig

class PetriNet:
    DEFAULT_GRAPH_VERTEX_ATTTRIBUTES = {
        'size': 70,
        'frame_color': '#000000',
    }

    def __init__(self):
        self.places = {}
        self.transitions = set()
        self.arcs = set()
        self.preset = {}
        self.postset = {}

        self.graph = ig.Graph(directed=True)
        self.graph_layout = None

    def read_from_file(self, filename: str):
        # first line contains the name of places
        # second line contains the name of transitions
        # from third line is the arcs
        with open(filename) as f:
            lines = f.read().strip().split('\n')
            for pct in lines[0].split():
                token, place = pct.split('.')
                token = int(token)
                self.add_place(place, token)
            for transition in lines[1].split():
                self.add_transition(transition)
            for line in lines[2:]:
                b, e = line.split()
                self.add_arc(b, e)


    def add_place(self, place: str, token: int = 0):
        self.places[place] = token
        self.preset[place] = set()
        self.postset[place] = set()
        self.graph.add_vertex(
            place,
            shape='circle',
            **self. DEFAULT_GRAPH_VERTEX_ATTTRIBUTES
         )
        self.graph_layout = None


    def add_transition(self, transition: str):
        self.transitions.add(transition)
        self.preset[transition] = set()
        self.postset[transition] = set()
        self.graph.add_vertex(
            transition,
            shape='square',
            **self. DEFAULT_GRAPH_VERTEX_ATTTRIBUTES
        )
        self.graph_layout = None



    def add_arc(self, source: str, target: str):
        self.arcs.add((source, target))
        self.preset[target].add(source)
        self.postset[source].add(target)
        self.graph.add_edge(source, target)
        self.graph_layout = None


    def is_enabled(self, transition: str) -> bool:
        for place in self.preset[transition]:
            if not self.places[place]:
                return False
        return True


    def get_enabled_transitions(self) -> set:
        res = set()
        for transition in self.transitions:
            if self.is_enabled(transition):
                res.add(transition)
        return res


    def fire_transition(self, transition: str):
        for place in self.preset[transition]:
            self.places[place] -= 1
        for place in self.postset[transition]:
            self.places[place] += 1


    def draw(self, filename='graph.png'):
        labels = []
        colors = []
        for name in self.graph.vs['name']:
            color = '#FFFFFF'
            if name in self.places:
                label = str(self.places[name]) + '.' + name
            else:
                label = name
                if self.is_enabled(name):
                    color = '#EBE859'
            labels.append(label)
            colors.append(color)

        self.graph.vs['label'] = labels
        self.graph.vs['color'] = colors
        if not self.graph_layout:
            self.graph_layout = self.graph.layout('kk')
        ig.plot(
            self.graph,
            bbox=(1000, 1000),
            margin=50,
            target=filename,
            layout=self.graph_layout
        )


    def __str__(self) -> str:
        res = 'places: [' + ', '.join(map(lambda p: str(self.places[p]) + '.' + p, self.places)) + ']\n'
        res += 'transitions: [' + ', '.join(self.transitions) + ']\n'
        res += 'arcs: [\n    ' + ',\n    '.join(map(lambda arc: arc[0] + ' - ' + arc[1], self.arcs)) + '\n]'
        return res




if __name__ == '__main__':
    n = PetriNet()
    n.read_from_file('input.txt')
    n.draw()

    print(n)
    while 1:
        ets = n.get_enabled_transitions()
        if len(ets) == 0:
            break;
        print('enabled transitions:', ', '.join(ets))
        print('input the transition you want to fire:')
        trans = input()
        if not (trans in ets):
            trans = next(iter(ets))
        print('firing:', trans)
        n.fire_transition(trans)
        n.draw()

        print('places: [' + ', '.join(map(lambda p: str(n.places[p]) + '.' + p, n.places)) + ']\n')
        print()


