# Tests for strategy

============================= test session starts =============================
collecting ... collected 10 items

test_strategy.py::test_init_small_strategy PASSED                        [ 10%]
test_strategy.py::test_init_bigger_strategy PASSED                       [ 20%]
test_strategy.py::test_get_next_attack_in_range PASSED                   [ 30%]
test_strategy.py::test_register_attack_hit_not_sunk PASSED               [ 40%]
test_strategy.py::test_register_attack_miss PASSED                       [ 50%]
test_strategy.py::test_get_enemy_board_updates PASSED                    [ 60%]
test_strategy.py::test_get_remaining_ships_unchanged_without_sunk PASSED [ 70%]
test_strategy.py::test_all_ships_sunk_unchanged PASSED                   [ 80%]
test_strategy.py::test_sink_first_ship_small_strategy PASSED             [ 90%]
test_strategy.py::test_sink_two_ships_small_strategy PASSED              [100%]

============================= 10 passed in 0.03s ==============================

# Tests for board setup

============================= test session starts =============================
collecting ... collected 12 items

test_board_setup.py::test_board_initialization PASSED                    [  8%]
test_board_setup.py::test_get_board_structure PASSED                     [ 16%]
test_board_setup.py::test_get_tile_in_range PASSED                       [ 25%]
test_board_setup.py::test_get_tile_out_of_range PASSED                   [ 33%]
test_board_setup.py::test_place_ships_empty_board PASSED                 [ 41%]
test_board_setup.py::test_place_ships_one_ship PASSED                    [ 50%]
test_board_setup.py::test_place_ships_all_seven PASSED                   [ 58%]
test_board_setup.py::test_find_ships_of_length PASSED                    [ 66%]
test_board_setup.py::test_find_l_ships PASSED                            [ 75%]
test_board_setup.py::test_reset_board PASSED                             [ 83%]
test_board_setup.py::test_board_stats_before_placement PASSED            [ 91%]
test_board_setup.py::test_board_stats_after_placement PASSED             [100%]

============================= 12 passed in 0.02s ==============================
