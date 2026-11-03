# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_83`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 64 |
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
> - Action 'Action_PreSnap' range [0-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [23-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-167] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-107] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-131] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-57] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-115] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-130] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-97] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-110] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-150] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-180] for track '28' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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