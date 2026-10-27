# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_36`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
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
> - Row 74: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [15-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-125] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-34] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-125] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [18-57] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [59-71] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-125] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [44-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-73] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-47] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-125] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-125] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-18] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-74] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-107] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-53] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-81] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-69] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-78] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-96] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-103] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-107] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-125] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-125] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-125] for track '30' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.