from account import Account
import networkx as nx
import matplotlib.pyplot as plt

class Network:
    def __init__(self, filename):
        self.network = {}

        with open(filename, 'r') as f:
            lines = [i.strip() for i in f.readlines()]

        for i in range(0, len(lines), 4):
            username = lines[i]
            if username not in self.network:
                self.network[username] = Account(username)

        for i in range(0, len(lines), 4):
            username = lines[i]
            following = [j.strip() for j in lines[i+1].split(',') if j.strip()]
            blocked = [j.strip() for j in lines[i+2].split(',') if j.strip()]
            blockedBy = [j.strip() for j in lines[i+3].split(',') if j.strip()]

            user = self.network[username]

            for f in following:
                if f not in self.network:
                    self.network[f] = Account(f)
                user.follow(self.network[f])  

            for b in blocked:
                if b not in self.network:
                    self.network[b] = Account(b)
                user.block(self.network[b])

            for bb in blockedBy:
                if bb not in self.network:
                    self.network[bb] = Account(bb)
                user.blockedBy.add(self.network[bb])
                self.network[bb].blocked.add(user)

    def toDict(self):
        result = {}
        for username, acc in self.network.items():
            result[username] = {
                "followers": sorted(u.username for u in acc.followers),
                "following": sorted(u.username for u in acc.following),
                "blocked": sorted(u.username for u in acc.blocked),
                "blockedBy": sorted(u.username for u in acc.blockedBy)
            }
        return result
    
    def show(self):
        G = nx.DiGraph()

        for username, account in self.network.items():
            for followed in account.following:
                G.add_edge(username, followed.username, color='blue', style='solid', label='follows')

        for username, account in self.network.items():
            for blocked in account.blocked:
                G.add_edge(username, blocked.username, color='red', style='dashed', label='blocks')

        edge_colors = [G[u][v]['color'] for u, v in G.edges()]
        edge_styles = [G[u][v]['style'] for u, v in G.edges()]

        pos = nx.spring_layout(G, k=0.15, iterations=20)
        plt.figure(figsize=(14, 14))

        nx.draw_networkx_nodes(G, pos, node_size=500)

        nx.draw_networkx_labels(G, pos, font_size=8)

        solid_edges = [(u, v) for u, v in G.edges() if G[u][v]['style'] == 'solid']
        dashed_edges = [(u, v) for u, v in G.edges() if G[u][v]['style'] == 'dashed']

        nx.draw_networkx_edges(G, pos, edgelist=solid_edges, edge_color='blue', arrows=True)

        nx.draw_networkx_edges(G, pos, edgelist=dashed_edges, edge_color='red', style='dashed', arrows=True)

        import matplotlib.lines as mlines
        follow_line = mlines.Line2D([], [], color='blue', label='follows')
        block_line = mlines.Line2D([], [], color='red', linestyle='dashed', label='blocks')
        plt.legend(handles=[follow_line, block_line], loc='best')

        plt.title("Instagram Network: Follows (Blue) vs Blocks (Red)")
        plt.axis('off')
        plt.show()

    def analytics(self):
        print("=== NETWORK ANALYTICS ===")
        total_accounts = len(self.network)
        total_follows = sum(len(acc.following) for acc in self.network.values())
        total_blocks = sum(len(acc.blocked) for acc in self.network.values())

        most_followed = max(self.network.items(), key=lambda x: len(x[1].followers), default=(None, None))
        most_following = max(self.network.items(), key=lambda x: len(x[1].following), default=(None, None))
        most_blocked = max(self.network.items(), key=lambda x: len(x[1].blockedBy), default=(None, None))
        most_blocking = max(self.network.items(), key=lambda x: len(x[1].blocked), default=(None, None))

        print(f"Total users: {total_accounts}")
        print(f"Total follow relationships: {total_follows}")
        print(f"Total block relationships: {total_blocks}")

        if most_followed[0]:
            print(f"Most followed user: @{most_followed[0]} ({len(most_followed[1].followers)} followers)")
        if most_following[0]:
            print(f"Most active follower: @{most_following[0]} ({len(most_following[1].following)} following)")
        if most_blocked[0]:
            print(f"Most blocked user: @{most_blocked[0]} ({len(most_blocked[1].blockedBy)} blockedBy)")
        if most_blocking[0]:
            print(f"Most aggressive blocker: @{most_blocking[0]} ({len(most_blocking[1].blocked)} blocks)")
        print("=========================\n")





    

print('hello')
network = Network('./network.txt')

for username, details in network.toDict().items():
    print('@'+username)
    for key, val in details.items():
        print(key, val)
    print()
network.analytics()
network.show()
