# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_15`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 57 |
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
> - Action 'Action_PreSnap' range [0-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-124] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-211] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-216] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-225] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [227-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-232] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-168] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-42] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-211] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '30' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.