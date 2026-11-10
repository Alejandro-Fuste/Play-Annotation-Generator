# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_95`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 97, Column 'Close On Quarterback': Unknown actor track ID '?' in entry '57,?'.
> - Row 97, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '70,?'.
> - Row 97, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '75,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-100] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-83] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-36] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-157] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-44] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-112] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-47] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-68] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-84] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-72] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-145] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-154] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-131] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-180] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-180] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.