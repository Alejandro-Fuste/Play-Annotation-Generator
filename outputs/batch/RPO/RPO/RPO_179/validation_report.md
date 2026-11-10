# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_179`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_179/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 74 |
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
> - Row 328: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 328: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-138] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [47-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-121] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-150] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-93] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-40] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-96] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-39] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-46] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-58] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-66] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-51] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-94] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-122] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-150] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-116] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-133] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-131] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-144] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '32' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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