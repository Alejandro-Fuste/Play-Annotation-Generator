# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_196`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_196/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 198, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '83,?'.
> - Row 198, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '101,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-63] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-61] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-17] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [80-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-39] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-58] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-120] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-97] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-105] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-111] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-116] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.