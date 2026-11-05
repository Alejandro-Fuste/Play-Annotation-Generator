# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_91`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 55 |
| Player Tracks | 55 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 199 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [82-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-197] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [199-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-131] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-194] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-481] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-541] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-264] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-420] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-301] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-498] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-507] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [510-511] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-599] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-132] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-257] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-599] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-178] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-97] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-142] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-189] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-288] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-384] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-410] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-416] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-434] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-131] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [147-160] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-253] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-522] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-134] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-301] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-562] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-572] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-260] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-293] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [82-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [103-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-471] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [473-540] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [546-557] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [563-565] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-572] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-593] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-124] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-247] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-253] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-273] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [275-296] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-314] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-188] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-288] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-309] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-320] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-522] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [536-576] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-225] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-309] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-369] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-483] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-498] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-588] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-564] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-317] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-521] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [524-541] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [544-550] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [570-571] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [577-578] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [580-585] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' range [592-598] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '31' starts at frame 599, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [599-599] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-367] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-495] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [498-565] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [568-570] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-578] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-584] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-593] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-598] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-315] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [321-395] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [398-406] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-528] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-338] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-384] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-508] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-392] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-599] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-340] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-594] for track '43' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [361-536] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-596] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-373] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-395] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-585] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-577] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-581] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-599] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-543] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [550-596] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [552-580] for track '52' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [584-588] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-562] for track '53' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.