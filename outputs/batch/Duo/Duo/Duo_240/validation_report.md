# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_240`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_240/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-216] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [119-173] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-225] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-131] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [149-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [181-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-239] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-138] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-184] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-192] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-185] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-168] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-187] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-208] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-223] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-238] for track '34' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.