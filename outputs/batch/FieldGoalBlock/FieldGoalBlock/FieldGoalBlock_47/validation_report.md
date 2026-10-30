# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_47`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [36-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-65] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-45] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-41] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-70] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 36, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [36-36] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-58] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-70] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 36, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [36-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-12] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-75] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-23] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-43] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-89] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-48] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-63] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-75] for track '25' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.