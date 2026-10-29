# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_212`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_212/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '8' has invalid range: start=89, end=52. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '15' has invalid range: start=89, end=79. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '22' has invalid range: start=89, end=66. Clamping end to start.
> - Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-91] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-13] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-13] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-72] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-116] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-10] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-79] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-74] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-10] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-94] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-28] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-86] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-66] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-91] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-150] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-79] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-79] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-82] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '33' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.