# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_213`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_213/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-53] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-72] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-88] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-100] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-98] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-27] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-72] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-34] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-58] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [66-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-88] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-94] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-100] for track '27' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.