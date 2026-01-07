# VisualAnimator

A Python tool for generating animated visualizations I used for presentations, including phase-colored wave animations and neural network structure animations.


## Features

- **Wave Animation**: Creates animated phase-colored wave visualizations (MP4)
- **Network Animation**: Generates animated neural network structure visualizations (GIF)


## Usage

### Wave Animation

```bash
python render.py wave -n 5000 -s 0 -e 5 -p output.mp4
```

- `-n, --numberSteps`: Number of animation steps (default: 5000)
- `-s, --startTime`: Start time (default: 0)
- `-e, --endTime`: End time (default: 5)
- `-p, --path`: Output file path

### Network Animation

```bash
python render.py network -x 24 -y 9 -n 5000 -p output.gif
```

- `-x, --xWidth`: Width of network animation (default: 24)
- `-y, --yHeight`: Height of network animation (default: 9)
- `-n, --numberSteps`: Number of steps (default: 5000)
- `-p, --path`: Output file path

## Dependencies

- matplotlib
- numpy
- seaborn
- scipy

## Project Structure

- `render.py` - Main entry point with CLI
- `visualizations/` - Visualization classes
  - `wave.py` - Wave animation implementation
  - `network.py` - Neural network animation implementation
- `renders/` - Example output animations
