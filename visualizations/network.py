import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import math
from pathlib import Path


class NeuralNetworkAnimation:
    def __init__(self, w: int, h: int, steps: int):
        if w <= 0 or h <= 0:
            print(f"Width and height should be >0. They are w: {w}, h: {h}")
            return

        self.w = w
        self.h = h

        self.fig, self.ax = plt.subplots(figsize=(w, h))

        # Adjust coordinate system ratio
        self.ax.set_xlim(0, self.w)
        self.ax.set_ylim(0, self.h)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        # Network architecture parameters
        # TODO: Make configurationpip install ipywidgets more user friendly
        self.input_nodes = 3
        self.hidden1_nodes = 5
        self.hidden2_nodes = 6
        self.hidden3_nodes = 5
        self.hidden4_nodes = 6
        self.hidden5_nodes = 5
        self.output_nodes = 3

        # Find maximum nodes for consistent spacing
        self.max_nodes = max(
            self.input_nodes,
            self.hidden1_nodes,
            self.hidden2_nodes,
            self.hidden3_nodes,
            self.hidden4_nodes,
            self.hidden5_nodes,
            self.output_nodes
        )

        # Layer positions - centered
        # TODO: determine automatically
        self.input_x = 3
        self.hidden1_x = 6
        self.hidden2_x = 9
        self.hidden3_x = 12
        self.hidden4_x = 15
        self.hidden5_x = 18
        self.output_x = 21

        # Node positions - all layers use same spacing based on max nodes
        self.input_positions = self.calculate_node_positions(
            self.input_nodes, self.input_x, self.max_nodes
        )
        self.hidden1_positions = self.calculate_node_positions(
            self.hidden1_nodes, self.hidden1_x, self.max_nodes
        )
        self.hidden2_positions = self.calculate_node_positions(
            self.hidden2_nodes, self.hidden2_x, self.max_nodes
        )
        self.hidden3_positions = self.calculate_node_positions(
            self.hidden3_nodes, self.hidden3_x, self.max_nodes
        )
        self.hidden4_positions = self.calculate_node_positions(
            self.hidden4_nodes, self.hidden4_x, self.max_nodes
        )
        self.hidden5_positions = self.calculate_node_positions(
            self.hidden5_nodes, self.hidden5_x, self.max_nodes
        )
        self.output_positions = self.calculate_node_positions(
            self.output_nodes, self.output_x, self.max_nodes
        )

        # Animation parameters
        self.time = 0
        self.animation_speed = 1.0 / steps if steps else 20

        # Store circles and lines for animation
        self.input_circles = []
        self.hidden1_circles = []
        self.hidden2_circles = []
        self.hidden3_circles = []
        self.hidden4_circles = []
        self.hidden5_circles = []
        self.output_circles = []
        self.connections = []

        self.create_network()

    def calculate_node_positions(self, num_nodes, x_pos, max_nodes):
        """Calculate y positions for nodes in a layer with same spacing"""
        if num_nodes == 1:
            return [(x_pos, self.h / 2)]

        # Calculate spacing based on the maximum number of nodes across all layers
        # This ensures all layers have the same vertical spacing
        total_height = math.ceil(self.h * 0.8)  # leave some marign
        spacing = total_height / (max_nodes - 1)

        # Center the nodes vertically
        start_y = (9 - (num_nodes - 1) * spacing) / 2

        positions = []
        for i in range(num_nodes):
            y = start_y + i * spacing
            positions.append((x_pos, y))
        return positions

    def create_network(self):
        self.create_connections()

        for pos in self.input_positions:
            circle = Circle(pos, 0.3, color='blue', alpha=0.7, zorder=10)
            self.input_circles.append(circle)
            self.ax.add_patch(circle)

        for pos in self.hidden1_positions:
            circle = Circle(pos, 0.3, color='green', alpha=0.7, zorder=10)
            self.hidden1_circles.append(circle)
            self.ax.add_patch(circle)

        for pos in self.hidden2_positions:
            circle = Circle(pos, 0.3, color='orange', alpha=0.7, zorder=10)
            self.hidden2_circles.append(circle)
            self.ax.add_patch(circle)

        for pos in self.hidden3_positions:
            circle = Circle(pos, 0.3, color='purple', alpha=0.7, zorder=10)
            self.hidden3_circles.append(circle)
            self.ax.add_patch(circle)

        for pos in self.hidden4_positions:
            circle = Circle(pos, 0.3, color='cyan', alpha=0.7, zorder=10)
            self.hidden4_circles.append(circle)
            self.ax.add_patch(circle)

        for pos in self.hidden5_positions:
            circle = Circle(pos, 0.3, color='magenta', alpha=0.7, zorder=10)
            self.hidden5_circles.append(circle)
            self.ax.add_patch(circle)

        for pos in self.output_positions:
            circle = Circle(pos, 0.3, color='red', alpha=0.7, zorder=10)
            self.output_circles.append(circle)
            self.ax.add_patch(circle)

    def create_connections(self):
        # TODO: rework layer configuration
        node_radius = 0.3

        # Input -> Hidden1
        for i, input_pos in enumerate(self.input_positions):
            for j, hidden1_pos in enumerate(self.hidden1_positions):
                # Calculate connection endpoints that stop at node edges
                start_x, start_y = self.get_connection_endpoint(
                    input_pos, hidden1_pos, node_radius, 'start')
                end_x, end_y = self.get_connection_endpoint(
                    input_pos, hidden1_pos, node_radius, 'end')

                line, = self.ax.plot([start_x, end_x],
                                     [start_y, end_y],
                                     'k-', alpha=0.3, linewidth=0.5, zorder=1)
                self.connections.append(line)

        # Hidden1 -> Hidden2 connections
        for i, hidden1_pos in enumerate(self.hidden1_positions):
            for j, hidden2_pos in enumerate(self.hidden2_positions):
                # Calculate connection endpoints that stop at node edges
                start_x, start_y = self.get_connection_endpoint(
                    hidden1_pos, hidden2_pos, node_radius, 'start')
                end_x, end_y = self.get_connection_endpoint(
                    hidden1_pos, hidden2_pos, node_radius, 'end')

                line, = self.ax.plot([start_x, end_x],
                                     [start_y, end_y],
                                     'k-', alpha=0.3, linewidth=0.5, zorder=1)
                self.connections.append(line)

        # Hidden2 -> Hidden3 connections
        for i, hidden2_pos in enumerate(self.hidden2_positions):
            for j, hidden3_pos in enumerate(self.hidden3_positions):
                # Calculate connection endpoints that stop at node edges
                start_x, start_y = self.get_connection_endpoint(
                    hidden2_pos, hidden3_pos, node_radius, 'start')
                end_x, end_y = self.get_connection_endpoint(
                    hidden2_pos, hidden3_pos, node_radius, 'end')

                line, = self.ax.plot([start_x, end_x],
                                     [start_y, end_y],
                                     'k-', alpha=0.3, linewidth=0.5, zorder=1)
                self.connections.append(line)

        # Hidden3 -> Hidden4 connections
        for i, hidden3_pos in enumerate(self.hidden3_positions):
            for j, hidden4_pos in enumerate(self.hidden4_positions):
                # Calculate connection endpoints that stop at node edges
                start_x, start_y = self.get_connection_endpoint(
                    hidden3_pos, hidden4_pos, node_radius, 'start')
                end_x, end_y = self.get_connection_endpoint(
                    hidden3_pos, hidden4_pos, node_radius, 'end')

                line, = self.ax.plot([start_x, end_x],
                                     [start_y, end_y],
                                     'k-', alpha=0.3, linewidth=0.5, zorder=1)
                self.connections.append(line)

        # Hidden4 -> Hidden5 connections
        for i, hidden4_pos in enumerate(self.hidden4_positions):
            for j, hidden5_pos in enumerate(self.hidden5_positions):
                # Calculate connection endpoints that stop at node edges
                start_x, start_y = self.get_connection_endpoint(
                    hidden4_pos, hidden5_pos, node_radius, 'start')
                end_x, end_y = self.get_connection_endpoint(
                    hidden4_pos, hidden5_pos, node_radius, 'end')

                line, = self.ax.plot([start_x, end_x],
                                     [start_y, end_y],
                                     'k-', alpha=0.3, linewidth=0.5, zorder=1)
                self.connections.append(line)

        # Hidden5 -> Output connections
        for i, hidden5_pos in enumerate(self.hidden5_positions):
            for j, output_pos in enumerate(self.output_positions):
                # Calculate connection endpoints that stop at node edges
                start_x, start_y = self.get_connection_endpoint(
                    hidden5_pos, output_pos, node_radius, 'start')
                end_x, end_y = self.get_connection_endpoint(
                    hidden5_pos, output_pos, node_radius, 'end')

                line, = self.ax.plot([start_x, end_x],
                                     [start_y, end_y],
                                     'k-', alpha=0.3, linewidth=0.5, zorder=1)
                self.connections.append(line)

    def get_connection_endpoint(self, start_pos, end_pos, radius, which_end):
        """Calculate connection endpoint that stops at node edge"""
        x1, y1 = start_pos
        x2, y2 = end_pos

        # Calculate direction vector
        dx = x2 - x1
        dy = y2 - y1
        distance = math.sqrt(dx*dx + dy*dy)

        if distance == 0:
            return (x1, y1)

        # Normalize direction vector
        dx_norm = dx / distance
        dy_norm = dy / distance

        if which_end == 'start':
            # Move from start position towards end by radius distance
            return (x1 + dx_norm * radius, y1 + dy_norm * radius)
        else:  # which_end == 'end'
            # Move from end position towards start by radius distance
            return (x2 - dx_norm * radius, y2 - dy_norm * radius)

    def get_animated_color(self, base_color, time_offset=0):
        """Generate animated RGB color based on time"""
        # Create a wave pattern for each RGB component
        r = (math.sin(self.time + time_offset) + 1) / 2
        g = (math.sin(self.time + time_offset + 2) + 1) / 2
        b = (math.sin(self.time + time_offset + 4) + 1) / 2

        # Blend with base color
        base_r, base_g, base_b = base_color
        final_r = (r + base_r) / 2
        final_g = (g + base_g) / 2
        final_b = (b + base_b) / 2

        return (final_r, final_g, final_b)

    def animate(self, frame):
        """Animation function called by matplotlib"""
        # time for one complete loop: 2π cycle
        total_frames = 120  # frames per complete cycle
        self.time = (frame % total_frames) * 2 * math.pi / total_frames

        for i, circle in enumerate(self.input_circles):
            color = self.get_animated_color(
                (0.2, 0.4, 0.8), i * 0.5)  # Blue base
            circle.set_color(color)

        for i, circle in enumerate(self.hidden1_circles):
            color = self.get_animated_color(
                (0.2, 0.8, 0.4), i * 0.3)  # Green base
            circle.set_color(color)

        for i, circle in enumerate(self.hidden2_circles):
            color = self.get_animated_color(
                (1.0, 0.6, 0.2), i * 0.4)  # Orange base
            circle.set_color(color)

        for i, circle in enumerate(self.hidden3_circles):
            color = self.get_animated_color(
                (0.6, 0.2, 0.8), i * 0.5)  # Purple base
            circle.set_color(color)

        for i, circle in enumerate(self.hidden4_circles):
            color = self.get_animated_color(
                (0.2, 0.8, 0.8), i * 0.4)  # Cyan base
            circle.set_color(color)

        for i, circle in enumerate(self.hidden5_circles):
            color = self.get_animated_color(
                (0.8, 0.2, 0.6), i * 0.6)  # Magenta base
            circle.set_color(color)

        for i, circle in enumerate(self.output_circles):
            color = self.get_animated_color(
                (0.8, 0.4, 0.2), i * 0.7)  # Red base
            circle.set_color(color)

        for i, line in enumerate(self.connections):
            # Pulsing alpha effect:
            pulse = (math.sin(self.time * 2 + i * 0.1) + 1) / 2
            alpha = 0.1 + pulse * 0.4

            # Individual edge weight pattern:
            # Create unique frequency and phase for each edge
            # Vary frequency between 0.8 and 2.0
            edge_freq = 0.8 + (i % 7) * 0.2
            edge_phase = i * 0.3  # Unique phase offset for each edge

            weight_pulse = (math.sin(self.time * edge_freq + edge_phase) + 1) / 2

            # Secondary wave for better optics (different frequency)
            weight_pulse2 = (math.sin(self.time * (edge_freq * 0.6) + edge_phase * 1.3) + 1) / 2

            # Combine waves
            combined_weight = (weight_pulse + weight_pulse2) / 2

            if i % 7 == 0:
                line_width = 0.5 + combined_weight * 1.5
            elif i % 5 == 0:
                line_width = 0.3 + combined_weight * 1.0
            else:
                line_width = 0.1 + combined_weight * 0.6

            line.set_alpha(alpha)
            line.set_linewidth(line_width)

        return self.input_circles + self.hidden1_circles + self.hidden2_circles + \
            self.hidden3_circles + self.hidden4_circles + self.hidden5_circles + \
            self.output_circles + self.connections

    def start_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, interval=50,
                                       blit=False, frames=1000, repeat=True)
        plt.tight_layout()
        plt.show()
        return anim

    def save_as_gif(self, filename="neural_network_animation.gif"):
        print(f"Saving animation as {filename}...")
        print("This may take a moment...")

        anim = animation.FuncAnimation(self.fig, self.animate,
                                       interval=100, blit=False,
                                       frames=120, repeat=True)

        # Save as GIF with endless loop
        anim.save(Path(filename), writer='pillow', fps=12,
                  savefig_kwargs={'facecolor': 'white', 'edgecolor': 'none'})

        print(f"Animation saved as {filename}")
        print("Perfect seamless loop created - animation ends exactly where it started!")
        return anim
