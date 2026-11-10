# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_141`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_141/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 256: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-194] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-233] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-191] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-183] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-214] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-224] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-237] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-105] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-206] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-35] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-82] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-225] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-94] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-94] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-204] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-190] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-169] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-189] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-199] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-200] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '32' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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