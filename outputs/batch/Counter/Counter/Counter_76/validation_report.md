# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_76`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '6' (RT) duration 102 frames exceeds threshold 90 frames [start=46, end=147].
> - Overlapping action conflict at frame 46 for track '9': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
> - Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 102 frames exceeds threshold 90 frames [start=46, end=147].
> - Validation warning: Action 'Action_PullBlock' for track '10' (LG) duration 102 frames exceeds threshold 90 frames [start=46, end=147].
> - Action 'Action_None' range [46-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [46-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [67-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [82-91] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [111-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [132-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-122] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-139] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-66] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [125-129] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [46-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [69-94] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [97-105] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [108-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-36] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-21] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '29' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.