# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_30`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 62: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 62: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 62: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 62: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 62: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-127] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-204] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-170] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-26] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-75] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-4] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-106] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-109] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-122] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-102] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-178] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-235] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-204] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-234] for track '33' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.