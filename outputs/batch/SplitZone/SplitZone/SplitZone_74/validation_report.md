# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_74`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 150: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [99-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-214] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [103-112] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [114-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [144-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-43] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-144] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-168] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-208] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-227] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-106] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-168] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-66] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 99, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [99-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-212] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-131] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-266] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-245] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-268] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '35' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.