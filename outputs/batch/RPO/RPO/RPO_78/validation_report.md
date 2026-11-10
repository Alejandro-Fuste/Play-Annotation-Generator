# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_78`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 28 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [80-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-238] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-171] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [140-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-90] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-168] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-166] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-92] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-105] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-155] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-199] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-201] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-232] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.