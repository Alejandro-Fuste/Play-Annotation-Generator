# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_63`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
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
> - Action 'Action_None' range [52-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-60] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-71] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' for track '16' starts at frame 56, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockKick' range [56-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-51] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-45] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-77] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-81] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.