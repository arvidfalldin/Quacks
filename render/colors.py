from engine.chips import ChipColor

# Map the ChipColor enum to hex color codes for visualization
CHIP_PALETTE = {
    ChipColor.WHITE: "#ffffff",
    ChipColor.ORANGE: "#ff7f00",
    ChipColor.BLACK: "#000000",
    ChipColor.RED: "#ff0000",
    ChipColor.BLUE: "#0000ff",
    ChipColor.YELLOW: "#f7ef08ff",
    ChipColor.GREEN: "#00ff00",
    ChipColor.PURPLE: "#800080",
}

TILE_BASE_COLOR = [124 / 255, 208 / 255, 162 / 255]
SPIRAL_COLOR = [187 / 255, 227 / 255, 213 / 255]
VICTORY_POINT_COLOR = "#f2deaaff"
