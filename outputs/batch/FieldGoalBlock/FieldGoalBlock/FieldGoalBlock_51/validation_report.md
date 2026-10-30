# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_51`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 139 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-46] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-310] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [68-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-213] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [219-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-231] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [234-326] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 61, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [61-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-97] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-131] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-311] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-290] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-269] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-279] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-310] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-209] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-283] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-73] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-301] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-111] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-131] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-49] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-270] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [313-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-83] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-145] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-193] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-286] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-295] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-125] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-171] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-310] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-326] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-329] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-259] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-291] for track '41' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [295-301] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-290] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-297] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-304] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-310] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '45' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.