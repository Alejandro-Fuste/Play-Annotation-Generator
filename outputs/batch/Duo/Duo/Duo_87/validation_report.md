# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_87`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 175: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 176: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-156] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-88] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [110-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-230] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-133] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [110-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-218] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [110-137] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-157] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [159-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-239] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-239] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-169] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-239] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-205] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-228] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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