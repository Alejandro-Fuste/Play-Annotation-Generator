# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_91`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 94: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 94: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 94: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [10-124] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [127-140] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-19] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-185] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [112-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [123-164] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [174-207] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-56] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-209] for track '29' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.