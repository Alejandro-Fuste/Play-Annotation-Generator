# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_65`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
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
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-75] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [99-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-210] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-22] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-10] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-13] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-66] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-57] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-64] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-52] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-210] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '27' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.