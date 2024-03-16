#!/usr/bin/python3
"""
Lockdown module
"""
# Lockboxes

def canUnlockAll(boxes):
    """
    Lockboxes
    args: boxes is a list of lists
    """
    if len(boxes) == 0:
        return False

    keys = set([0])
    added_keys = True

    while added_keys:
        added_keys = False
        for box_index, box in enumerate(boxes):
            if box_index in keys:  # If we have the key for this box
                for key in box:  # Add any new keys found
                    if key not in keys and key < len(boxes):
                        keys.add(key)
                        added_keys = True

    return len(keys) == len(boxes)  # Return True if all boxes are unlocked
