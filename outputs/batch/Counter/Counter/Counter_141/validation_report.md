# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_141`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_141/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 283: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 101 frames exceeds threshold 90 frames [start=70, end=170].
> - Action 'Action_None' range [64-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [70-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [126-140] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-299] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [70-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [98-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-286] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-297] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [70-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [86-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [70-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [109-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [98-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [192-299] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-293] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [70-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [120-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [126-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-234] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-63] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-256] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-214] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '37' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.