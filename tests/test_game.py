import unittest
from game import (
    new_game, 
    move_player, 
    collect_item, 
    show_inventory,
    make_decision
) 

class TestMovePlayer(unittest.TestCase):
    
    def setUp(self):
        # this creates a fresh player before every test
        self.player = new_game("Chika")

    def test_player_can_move_from_beach_to_jungle(self):
        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_successful_move_reduces_energy_by_one(self):
        move_player(self.player, "Jungle")

        self.assertEqual(self.player["energy"], 4)
    
    def test_player_cannot_move_to_unconnected_location(self):
        success, message = move_player(self.player, "Cave")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
    
    def test_invalid_location_does_not_change_player_state(self):
        success, message = move_player(self.player, "Airport")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
    
    def test_player_cannot_cross_bridge_without_rope(self):
        self.player["location"] = "Old Bridge"

        success, message = move_player(self.player, "Lighthouse")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Old Bridge")
        self.assertEqual(self.player["energy"], 5)

    def test_player_can_cross_bridge_with_rope(self):
        self.player["location"] = "Old Bridge"
        self.player["inventory"].append("Rope")

        success, message = move_player(self.player, "Lighthouse")

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Lighthouse")
        self.assertEqual(self.player["energy"], 4)

    def test_player_loses_when_energy_reaches_zero(self):
        self.player["energy"] = 1

        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(self.player["game_over"])
        self.assertFalse(self.player["won"])

    def test_player_wins_with_rope_and_lantern(self):
        self.player["location"] = "Old Bridge"
        self.player["inventory"] = ["Rope", "Lantern"]

        success, message = move_player(self.player, "Lighthouse")

        self.assertTrue(success)
        self.assertTrue(self.player["won"])
        self.assertTrue(self.player["game_over"])
        self.assertEqual(self.player["location"], "Lighthouse")

    def test_player_cannot_move_after_game_is_over(self):
        self.player["game_over"] = True 

        success, message = move_player(self.player, "Jungle")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_player_can_collect_rope_at_beach(self):
        success, message = collect_item(self.player)

        self.assertTrue(success)
        self.assertIn("Rope", self.player["inventory"])

    def test_player_can_collect_lantern_in_cave(self):
        self.player["location"] = "Cave"

        success, message = collect_item(self.player)

        self.assertTrue(success)
        self.assertIn("Lantern", self.player["inventory"])

    def test_player_cannot_collect_same_item_twice(self):
        collect_item(self.player)

        success, message = collect_item(self.player)

        self.assertFalse(success)
        self.assertEqual(self.player["inventory"].count("Rope"), 1)

    def test_player_cannot_collect_item_at_wrong_location(self):
        success, message = collect_item(self.player)

        # Move to Jungle, where no item is available
        move_player(self.player, "Jungle")

        success, message = collect_item(self.player)

        self.assertFalse(success)
        self.assertEqual(self.player["inventory"], ["Rope"])

    def test_player_cannot_collect_item_after_game_over(self):
        self.player["game_over"] = True

        success, message = collect_item(self.player)

        self.assertFalse(success)
        self.assertEqual(self.player["inventory"], [])

    def test_inventory_is_empty_at_start(self):
        result = show_inventory(self.player)

        self.assertEqual(result, "Your inventory is empty.")

    def test_inventory_displays_collected_items(self):
        collect_item(self.player)

        result = show_inventory(self.player)

        self.assertEqual(result, "Your inventory: Rope")

    def test_player_cannot_win_without_lantern(self):
        self.player["location"] = "Old Bridge"
        self.player["inventory"] = ["Rope"]

        success, message = move_player(self.player, "Lighthouse")

        self.assertTrue(success)
        self.assertFalse(self.player["won"])

    def test_player_wins_with_both_required_items(self):
        self.player["location"] = "Old Bridge"
        self.player["inventory"] = ["Rope", "Lantern"]

        success, message = move_player(self.player, "Lighthouse")

        self.assertTrue(success)
        self.assertTrue(self.player["won"])
        self.assertTrue(self.player["game_over"])

    def test_player_cannot_move_with_zero_energy(self):
        self.player["energy"] = 0

        success, message = move_player(self.player, "Jungle")

        self.assertFalse(success)
        self.assertTrue(self.player["game_over"])
        self.assertEqual(self.player["energy"], 0)

    def test_replay_creates_fresh_player(self):
        self.player["energy"] = 2
        self.player["location"] = "Cave"
        self.player["inventory"] = ["Rope", "Lantern"]

        new_player = new_game("Chika")

        self.assertEqual(new_player["energy"], 5)
        self.assertEqual(new_player["location"], "Beach")
        self.assertEqual(new_player["inventory"], [])
        self.assertFalse(new_player["game_over"])
        self.assertFalse(new_player["won"])

    def test_jungle_safe_route_does_not_reduce_energy(self):
        self.player["location"] = "Jungle"

        success, message = make_decision(
            self.player, "Jungle", "1"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 5)
        self.assertIn("Jungle", self.player["decisions_made"])

    def test_jungle_shortcut_reduces_energy(self):
        self.player["location"] = "Jungle"

        success, message = make_decision(
            self.player, "Jungle", "2"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 4)

    def test_cave_search_collects_lantern(self):
        self.player["location"] = "Cave"

        success, message = make_decision(
            self.player, "Cave", "1"
        )

        self.assertTrue(success)
        self.assertIn("Lantern", self.player["inventory"])

    def test_leaving_cave_does_not_collect_lantern(self):
        self.player["location"] = "Cave"

        success, message = make_decision(
            self.player, "Cave", "2"
        )

        self.assertTrue(success)
        self.assertNotIn("Lantern", self.player["inventory"])
        self.assertIn("Cave", self.player["decisions_made"])

    def test_bridge_careful_choice_does_not_reduce_energy(self):
        self.player["location"] = "Old Bridge"

        success, message = make_decision(
            self.player, "Old Bridge", "1"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 5)

    def test_bridge_rush_choice_reduces_energy(self):
        self.player["location"] = "Old Bridge"

        success, message = make_decision(
            self.player, "Old Bridge", "2"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 4)

    def test_invalid_decision_does_not_change_energy(self):
        self.player["location"] = "Jungle"

        success, message = make_decision(
            self.player, "Jungle", "5"
        )

        self.assertFalse(success)
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["decisions_made"], set())

    def test_player_cannot_make_same_decision_twice(self):
        self.player["location"] = "Jungle"

        make_decision(self.player, "Jungle", "1")

        success, message = make_decision(
            self.player, "Jungle", "2"
        )

        self.assertFalse(success)
        self.assertEqual(self.player["energy"], 5)
    
    def test_cannot_enter_lighthouse_without_rope(self):
        self.player["location"] = "Old Bridge"
        self.player["inventory"] = ["Lantern"]

        success, message = move_player(self.player, "Lighthouse")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Old Bridge")
        self.assertNotIn("Lighthouse", self.player["inventory"])

if __name__ == "__main__":
    unittest.main()
