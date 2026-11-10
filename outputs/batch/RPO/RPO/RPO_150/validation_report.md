# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_150`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_150/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LG', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 274: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-200] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [51-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-221] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-160] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-109] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-155] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-200] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-196] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-201] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-269] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-174] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-207] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-246] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-259] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-185] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-216] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-265] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-245] for track '31' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.