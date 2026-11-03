# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_19`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Overlapping action conflict at frame 17 for track '14': 'Action_BallSnap' vs 'Action_PassBlock'. Overriding with 'Action_PassBlock'.
> - Action 'Action_None' range [17-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [29-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-45] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-75] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-120] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-85] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-23] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-120] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-36] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-57] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.