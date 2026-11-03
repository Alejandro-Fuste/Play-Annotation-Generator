# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_69`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 140: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-112] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-130] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '8' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-40] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-59] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [51-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [160-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [163-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-113] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-127] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-154] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-23] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-9] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-193] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-46] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-206] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-98] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-144] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-179] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-196] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-186] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '33' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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