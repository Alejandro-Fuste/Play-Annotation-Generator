# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_1`
- **Input XML**: `output_showcase_pre_generation_check/RPO/RPO_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 4: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 4: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [87-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-185] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-198] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [88-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [103-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [108-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [100-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [88-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [98-103] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [113-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [151-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [156-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [88-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [152-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '27' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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