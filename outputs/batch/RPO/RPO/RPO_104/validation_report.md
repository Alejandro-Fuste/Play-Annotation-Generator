# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_104`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [10-70] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [102-106] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-116] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-183] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-123] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-172] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-52] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-61] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-40] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [43-44] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [46-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-16] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-78] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-127] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-93] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-15] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-114] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-16] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-90] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-97] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-98] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-143] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-209] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-227] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-255] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-175] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-265] for track '28' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.