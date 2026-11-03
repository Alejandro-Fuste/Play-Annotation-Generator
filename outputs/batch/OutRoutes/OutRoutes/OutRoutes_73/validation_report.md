# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_73`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 80: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-143] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-69] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-180] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-109] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [123-131] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [140-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-49] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-69] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-69] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [93-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-38] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-48] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-154] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-166] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-180] for track '30' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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