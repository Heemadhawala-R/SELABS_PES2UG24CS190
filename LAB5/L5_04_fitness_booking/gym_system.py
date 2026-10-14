
"""Manage bookings for a fitness studio."""

import json
from pathlib import Path

class_capacity = {"Yoga": 3, "HIIT": 2, "Spin": 4}
rosters = {}


def book_class(member_id, class_name, attendance_log=None):
    """Book a member into a class."""
    if attendance_log is None:
        attendance_log = []

    capacity = class_capacity.get(class_name)
    current_members = rosters.get(class_name, [])

    if capacity is not None and len(current_members) >= capacity:
        print(f"Class full: {class_name}")
        return False

    rosters.setdefault(class_name, []).append(member_id)
    attendance_log.append(f"{member_id} -> {class_name}")
    return True


def cancel_booking(member_id, class_name):
    """Cancel a booking if it exists."""
    try:
        rosters[class_name].remove(member_id)
    except (KeyError, ValueError):
        print("Nothing to cancel")


def set_capacity(class_name, seats):
    """Set a non-negative class capacity."""
    if not isinstance(seats, int) or isinstance(seats, bool) or seats < 0:
        raise ValueError("Capacity must be a non-negative integer")
    class_capacity[class_name] = seats


def add_members(class_name, count):
    """Add guest bookings to a class."""
    if not isinstance(count, int) or isinstance(count, bool) or count < 0:
        raise ValueError("Guest count must be a non-negative integer")

    for i in range(count):
        book_class(f"GUEST-{i}", class_name)


def export_roster(file="gym_schedule.json"):
    """Export rosters to a JSON file."""
    with open(file, "w", encoding="utf-8") as roster_file:
        json.dump(rosters, roster_file, indent=4)


def clear_old_exports(prefix="old_"):
    """Delete matching old JSON exports from the current directory."""
    if not prefix or Path(prefix).name != prefix:
        raise ValueError("Prefix must be a non-empty filename prefix")

    for path in Path.cwd().iterdir():
        if (
            path.is_file()
            and path.name.startswith(prefix)
            and path.suffix == ".json"
        ):
            path.unlink()


def show_rosters():
    """Display all class rosters."""
    for class_name, members in rosters.items():
        print(f"{class_name} : {', '.join(str(m) for m in members)}")


def main():
    """Run the booking demonstration."""
    book_class("M1", "Yoga")
    book_class("M2", "Yoga")
    book_class("M3", "Yoga")
    book_class("M4", "Yoga")
    book_class(55, "HIIT")
    book_class("M5", "Pilates")

    set_capacity("Spin", 0)
    add_members("Spin", 3)
    cancel_booking("M9", "Boxing")

    try:
        value = input(
            "How many walk-in guests for HIIT? (Enter for 1): "
        ).strip()
        count = int(value) if value else 1
        add_members("HIIT", count)
    except ValueError:
        print("Please enter a non-negative whole number.")
        return

    clear_old_exports()
    export_roster()
    show_rosters()


if __name__ == "__main__":
    main()
