# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_220`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_220/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 442: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 442: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 442: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 442: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
> - Row 442: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 442: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-87] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-60] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [33-58] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-125] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [33-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-125] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-78] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-113] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-92] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-108] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-122] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.