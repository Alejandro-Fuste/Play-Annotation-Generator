# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_107`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 114: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [63-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [120-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '28' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.