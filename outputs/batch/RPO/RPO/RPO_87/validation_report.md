# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_87`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RG'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [91-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-85] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-83] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-103] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-53] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-85] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-92] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-112] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-148] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-116] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-191] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-207] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '27' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.