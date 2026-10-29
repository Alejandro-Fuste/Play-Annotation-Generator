# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_180`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_180/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-3] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-82] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-58] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-53] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-61] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-73] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [51-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [58-68] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-61] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-83] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-40] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-65] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-80] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-59] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-75] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-94] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-85] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-87] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-100] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-95] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-100] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-100] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.