# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_89`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 90: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-85] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-95] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [73-116] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [118-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-210] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-12] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '26' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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