# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_286`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_286/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '1' (RT) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
> - Validation warning: Action 'Action_DownBlock' for track '4' (C) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [22–37], lower_priority='Action_DownBlock' annotated_start=25, effective_Action_DownBlock_start=38.
> - Validation warning: Action 'Action_PullBlock' for track '8' (LG) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
> - Action 'Action_None' range [22-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [25-83] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [92-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [72-194] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-232] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-237] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [38-104] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-138] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [25-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-121] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-174] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-239] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-218] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-236] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-238] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '37' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.