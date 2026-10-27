# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_37`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 35 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 76: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
> - Row 76: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [121-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-58] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-82] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-150] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-28] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [39-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-148] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-84] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [92-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [142-150] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-65] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-26] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-150] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-98] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-148] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-129] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-148] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '35' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
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