# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_55`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 93 frames exceeds threshold 90 frames [start=17, end=109].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 93 frames exceeds threshold 90 frames [start=17, end=109].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 93 frames exceeds threshold 90 frames [start=17, end=109].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [15–27], lower_priority='Action_ZoneBlock' annotated_start=17, effective_Action_ZoneBlock_start=28.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 93 frames exceeds threshold 90 frames [start=17, end=109].
> - Action 'Action_None' range [15-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-160] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-54] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-63] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-178] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-99] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-114] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [48-140] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [15-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-88] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-149] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-179] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.