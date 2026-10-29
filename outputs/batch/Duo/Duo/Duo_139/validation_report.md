# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_139`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_139/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 280: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 280: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-238] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-156] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-191] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-213] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [105-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [149-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [105-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [124-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-159] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-164] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-212] for track '32' has 2 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.