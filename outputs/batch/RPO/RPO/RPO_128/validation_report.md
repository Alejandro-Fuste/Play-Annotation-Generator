# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_128`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 78 |
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
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-16] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-88] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-176] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [44-53] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [98-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-92] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-122] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-78] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-60] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-125] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-140] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-152] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-178] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-178] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '34' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.