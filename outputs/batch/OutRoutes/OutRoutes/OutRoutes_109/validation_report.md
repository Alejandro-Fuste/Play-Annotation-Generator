# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_109`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-161] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-94] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-108] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-107] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [123-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-180] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-31] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-42] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-105] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-174] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-180] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-136] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-149] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '32' has 1 frames without a visible bounding box.
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