# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_1`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 3: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [11–25], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=26.
> - Action 'Action_None' range [11-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [149-165] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [145-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [165-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-38] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-251] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-16] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-215] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-62] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-269] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [11-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-253] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-241] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-269] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-249] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '35' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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