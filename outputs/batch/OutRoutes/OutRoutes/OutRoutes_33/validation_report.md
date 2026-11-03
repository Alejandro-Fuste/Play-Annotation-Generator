# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_33`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 87 |
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
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-150] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-49] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-51] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [93-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-150] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-81] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-86] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-52] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-59] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-87] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-150] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-74] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-80] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-107] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-95] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-111] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-108] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-150] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-150] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '32' has 1 frames without a visible bounding box.
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