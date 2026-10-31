# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_24`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 126 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 33: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '0' has invalid range: start=142, end=122. Clamping end to start.
> - Segment 'Action_PassBlock' for track '15' has invalid range: start=28, end=17. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '16' has invalid range: start=93, end=17. Clamping end to start.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=20, end=14. Clamping end to start.
> - Segment 'Action_PassBlock' for track '19' has invalid range: start=28, end=19. Clamping end to start.
> - Segment 'Action_PassBlock' for track '20' has invalid range: start=28, end=10. Clamping end to start.
> - Action 'Action_RunHitchRoute' range [35-122] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-196] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [200-217] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-45] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-239] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-67] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-51] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 20, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [20-26] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-184] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [187-235] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-22] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-188] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-234] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-48] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-54] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [20-24] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-183] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-141] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-156] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-105] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-177] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-199] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-160] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-193] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-214] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-156] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-195] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-233] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-230] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-184] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-197] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-217] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '43' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.