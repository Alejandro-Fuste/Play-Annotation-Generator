# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `FieldGoalBlock_91`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BlockKick' at frame 62 targets track ID '-', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-48] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-57] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-93] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-137] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-70] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-69] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-92] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-116] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-155] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-151] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '32' has 1 frames without a visible bounding box.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.