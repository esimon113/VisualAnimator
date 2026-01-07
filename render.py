import argparse
from visualizations.network import NeuralNetworkAnimation
from visualizations.wave import WaveAnimation


def create_network(w: int, h: int, steps: int, fn: str):
    print("This will create a GIF file with an animated network structure.")

    if w > 0 and h > 0:
        nn_animation = NeuralNetworkAnimation(w, h, steps)

        filename = fn if fn != "" else "neural_network_animation.gif"
        anim = nn_animation.save_as_gif(filename)

        return anim
    else:
        print(f"Expected w, h > 0, received: {w}, {h}")


def create_wave(steps: int, start: int, end: int, fn: str):
    print("This will create a MP4 file with an animated wave.")

    if end > start:
        wave_animation = WaveAnimation(steps, start, end)

        filename = fn if fn != "" else "wave_animation.mp4"
        anim = wave_animation.save_as(filename)

        return anim
    else:
        print(f"Expected start < end, received: start({start}), end({end})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generator for animated visualizations.")

    parser.add_argument("visualization", type=str, default="wave",
                        help="Visualization to generate. Should be one of: [\"wave\", \"network\"]")
    parser.add_argument("-p", "--path", type=str, help="Output file path")
    parser.add_argument("-x", "--xWidth", type=int, default=24, help="Width of network animation")
    parser.add_argument("-y", "--yHeight", type=int, default=9, help="Height of network animation")
    parser.add_argument("-n", "--numberSteps", type=int, default=5000,
                        help="Number of steps in wave animation")
    parser.add_argument("-s", "--startTime", type=int, default=0,
                        help="Start time for the wave animation")
    parser.add_argument("-e", "--endTime", type=int, default=5,
                        help="End time for the wave animation")

    args = parser.parse_args()

    print("Creating Animation...")

    # TODO: input validation

    withSuccess = False

    if args.visualization == "wave":
        p = args.path if args.path else "wave_animation.mp4"
        create_wave(args.numberSteps, args.startTime, args.endTime, p)
    elif args.visualization == "network":
        p = args.path if args.path else "network_animation.gif"
        create_network(args.xWidth, args.yHeight, args.numberSteps, p)
    else:
        print(f"Invalid parameter provided, expected 'wave' or 'network', but received: {
              args.visualization}")

    if withSuccess:
        print(f"\n✅ Success! The Animation has been saved as '{args.path}'")
