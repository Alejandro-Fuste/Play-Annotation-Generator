# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_11`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 18: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_BallCarry' range [107-149] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [156-161] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-112] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-125] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-62] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-70] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-104] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-94] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-109] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [112-120] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [126-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-141] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-47] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-43] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-141] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-21] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-30] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-94] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-128] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [147-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-70] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-86] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-98] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [112-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [123-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-94] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-180] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-92] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-104] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-113] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-121] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-139] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-158] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-179] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-125] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-141] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-123] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-180] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '33' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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